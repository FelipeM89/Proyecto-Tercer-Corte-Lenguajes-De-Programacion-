#!/usr/bin/env python3
"""
ascii_table.py

Función para renderizar tablas en ASCII al estilo de la representación
de pandas.DataFrame en consola, sin librerías externas.

Características:
- Acepta:
  - list[dict] (lista de filas como dicts, claves = columnas)
  - dict[str, list] (mapping columnas -> listas)
  - list[sequence] (matriz) + headers opcional
- Soporta truncado de filas/columnas (head/tail) como pandas.
- Alineación automática (números a la derecha, texto a la izquierda) o personalizada.
- Control de anchos máximos por columna, truncado con '...'.
- Devuelve la representación como string (no imprime directamente) para mayor control.

Ejemplo rápido:
  s = ascii_table(data, headers=None, max_rows=10, max_cols=8)
  print(s)
"""
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple, Union

TableData = Union[List[Dict[str, Any]], Dict[str, Sequence[Any]], List[Sequence[Any]]]


def _is_number(val: Any) -> bool:
    try:
        if val is None:
            return False
        # bool is subclass of int; treat bool as non-number for alignment
        if isinstance(val, bool):
            return False
        float(val)
        return True
    except Exception:
        return False


def _format_cell(val: Any, floatfmt: str) -> str:
    if val is None:
        return "NaN"
    if isinstance(val, float):
        # use general format similar to pandas' default repr
        return format(val, floatfmt)
    if isinstance(val, (int, bool)):
        return str(val)
    return str(val)


def _collect_from_list_of_dicts(rows: List[Dict[str, Any]]) -> Tuple[List[str], List[List[Any]]]:
    # preserve column order by first occurrence
    cols: List[str] = []
    for r in rows:
        for k in r.keys():
            if k not in cols:
                cols.append(k)
    table_rows: List[List[Any]] = []
    for r in rows:
        row = [r.get(c, None) for c in cols]
        table_rows.append(row)
    return cols, table_rows


def _collect_from_dict_of_lists(d: Dict[str, Sequence[Any]]) -> Tuple[List[str], List[List[Any]]]:
    cols = list(d.keys())
    # check equal lengths
    lengths = {len(v) for v in d.values()}
    if len(lengths) == 0:
        return cols, []
    if len(lengths) != 1:
        raise ValueError("All columns must have the same number of rows")
    n = next(iter(lengths))
    rows: List[List[Any]] = []
    for i in range(n):
        rows.append([d[c][i] for c in cols])
    return cols, rows


def _collect_from_matrix(mat: List[Sequence[Any]], headers: Optional[List[str]]) -> Tuple[List[str], List[List[Any]]]:
    if headers is None:
        ncols = len(mat[0]) if mat else 0
        headers = [str(i) for i in range(ncols)]
    rows = [list(r) for r in mat]
    return headers, rows


def _truncate_text(s: str, maxw: int) -> str:
    if len(s) <= maxw:
        return s
    if maxw <= 3:
        return s[:maxw]
    return s[: maxw - 3] + "..."


def ascii_table(
    data: TableData,
    headers: Optional[List[str]] = None,
    *,
    max_rows: int = 20,
    max_cols: int = 20,
    max_col_width: int = 30,
    floatfmt: str = ".6g",
    show_index: bool = True,
    index_name: Optional[str] = None,
    align: Optional[Sequence[str]] = None,
) -> str:
    """
    Renderiza una tabla ASCII estilo pandas.

    Parámetros principales:
    - data: list[dict] | dict[column->list] | list[sequence]
    - headers: lista de nombres de columna si data es matriz (list of sequences).
    - max_rows: máximo filas a mostrar; si hay más, muestra head/tail con '...'.
    - max_cols: máximo columnas a mostrar; si hay más, muestra primeras/últimas con '...'.
    - max_col_width: ancho máximo por columna (texto truncado con ...).
    - floatfmt: formato para floats (passed to format()).
    - show_index: si True añade columna de índice a la izquierda.
    - index_name: nombre para la columna índice.
    - align: secuencia de 'left'|'right'|'center' por columna (si proporcionada).
    """

    # Normalizar entrada a headers + rows (list of lists)
    if isinstance(data, list) and data and isinstance(data[0], dict):
        cols, rows = _collect_from_list_of_dicts(data)  # type: ignore[arg-type]
    elif isinstance(data, dict):
        cols, rows = _collect_from_dict_of_lists(data)  # type: ignore[arg-type]
    else:
        # assume list of sequences (possibly empty)
        mat = data if isinstance(data, list) else []
        cols, rows = _collect_from_matrix(mat, headers)  # type: ignore[arg-type]

    nrows = len(rows)
    ncols = len(cols)

    # Decide columns to show (handle many columns)
    if ncols > max_cols:
        left = max_cols // 2
        right = max_cols - left - 1  # reserve one col for '...'
        show_col_idx = list(range(left)) + list(range(ncols - right, ncols))
        col_spans_ellipsis = True
    else:
        show_col_idx = list(range(ncols))
        col_spans_ellipsis = False

    shown_cols = [cols[i] for i in show_col_idx]

    # Decide rows to show (head/tail)
    if nrows > max_rows:
        top = max_rows // 2
        bottom = max_rows - top - 1  # reserve one row for '...'
        show_row_idx = list(range(top)) + list(range(nrows - bottom, nrows))
        row_spans_ellipsis = True
    else:
        show_row_idx = list(range(nrows))
        row_spans_ellipsis = False

    # Build display matrix for sampled cells
    display_rows: List[List[str]] = []
    for r_i in show_row_idx:
        row = []
        for c_i in show_col_idx:
            val = rows[r_i][c_i] if c_i < len(rows[r_i]) else None
            row.append(_format_cell(val, floatfmt))
        display_rows.append(row)

    # Compute column widths
    col_widths: List[int] = []
    for j, col_name in enumerate(shown_cols):
        max_cell = len(col_name)
        for r in display_rows:
            max_cell = max(max_cell, len(r[j]))
        w = min(max_cell, max_col_width)
        col_widths.append(w)

    # Index column width
    index_width = 0
    if show_index:
        # determine index labels we will show (numbers or original)
        if nrows == 0:
            index_labels = []
        else:
            index_labels = [str(i) for i in show_row_idx]
        if row_spans_ellipsis:
            index_labels.insert(len(index_labels) // 2, "...")
        index_width = max((len(index_name) if index_name else 0), *(len(l) for l in index_labels) if index_labels else [0])
        index_width = min(index_width, max_col_width)

    # Alignment per column
    aligns: List[str] = []
    if align:
        # expand/clip to number of columns to show
        aligns = list(align[: len(shown_cols)])
        if len(aligns) < len(shown_cols):
            aligns += ["left"] * (len(shown_cols) - len(aligns))
    else:
        # autodetect per shown column using sampled cells
        for j in range(len(shown_cols)):
            # if all or majority are numbers, right-align
            num_count = 0
            total_count = 0
            for r in display_rows:
                s = r[j]
                if s and _is_number(s):
                    num_count += 1
                total_count += 1
            aligns.append("right" if total_count > 0 and num_count / (total_count or 1) >= 0.6 else "left")

    # Helper to pad/truncate cell according to width and alignment
    def _render_cell(s: str, width: int, alignment: str) -> str:
        s_trunc = _truncate_text(s, width)
        if alignment == "right":
            return s_trunc.rjust(width)
        if alignment == "center":
            return s_trunc.center(width)
        return s_trunc.ljust(width)

    # Build header row
    header_cells: List[str] = []
    for j, col_name in enumerate(shown_cols):
        header_cells.append(_render_cell(col_name, col_widths[j], "center"))

    # Compose lines: header, separator, data rows, footer ticks (like pandas no borders)
    parts: List[str] = []
    # Header with index name
    header_line = ""
    if show_index:
        idx_name = index_name if index_name is not None else ""
        header_line += idx_name.rjust(index_width) + " "
    header_line += " ".join(header_cells)
    parts.append(header_line)

    # Separator line under header (use dashes)
    sep = ""
    if show_index:
        sep += "-" * index_width + " "
    sep += " ".join("-" * w for w in col_widths)
    parts.append(sep)

    # Data rows, with possible ellipsis row
    row_counter = 0
    for i, r_idx in enumerate(show_row_idx):
        if row_spans_ellipsis and i == len(show_row_idx) // 2:
            # ellipsis row
            ell_line = ""
            if show_index:
                ell_line += "..." .rjust(index_width) + " "
            ell_cells = []
            for w in col_widths:
                ell_cells.append("..." .center(w) if w >= 3 else "." * w)
            ell_line += " ".join(ell_cells)
            parts.append(ell_line)
            continue
        cells = display_rows[row_counter]
        rowline = ""
        if show_index:
            idx_label = str(r_idx)
            rowline += idx_label.rjust(index_width) + " "
        rendered = [_render_cell(cells[j], col_widths[j], aligns[j]) for j in range(len(shown_cols))]
        rowline += " ".join(rendered)
        parts.append(rowline)
        row_counter += 1

    # If columns hidden, add a footer indicating omitted columns
    if col_spans_ellipsis:
        omitted = ncols - len(shown_cols)
        parts.append(f"... and {omitted} more column(s)")

    # If rows hidden, add footer indicating omitted rows
    if row_spans_ellipsis:
        omitted_r = nrows - len(show_row_idx)
        parts.append(f"... and {omitted_r} more row(s)")

    return "\n".join(parts)


if __name__ == "__main__":
    
    data = [
        [1, "Alice", 85.5, "A"],
        [2, "Bob", 92.3, "A+"],
        [3, "Carlos", 78.0, "B"],
        [4, "Diana", 88.7, "A"],
        [5, "Eve", 95.2, "A+"]
    ]

    # Headers para las columnas
    #headers = ["ID", "Nombre", "Nota", "Calificación","hola"]

    # Renderizar tabla
    tabla = ascii_table(data, headers=None)
    print(tabla)