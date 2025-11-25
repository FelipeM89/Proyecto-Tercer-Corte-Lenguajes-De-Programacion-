from typing import List, Optional
""" Genera una grafica de puntos en ASCII dado un conjunto de datos (x,y) """


def _map_to_grid(x_val, y_val, xmin, xmax, ymin, ymax, width, height):

    if xmax == xmin:
        col = width // 2
    else:
        col = int((x_val - xmin) / (xmax - xmin) * (width - 1))
        col = max(0, min(width - 1, col))
    if ymax == ymin:
        row = height // 2
    else:

        row = int((ymax - y_val) / (ymax - ymin) * (height - 1))
        row = max(0, min(height - 1, row))
    return col, row
def render_ascii(x, y,
                            width: int = 80, 
                            height: int = 20,
                            left_margin: int = 9,
                            point_char: str = '*',
                            title: Optional[str] = None) -> str:
    """
    Renderiza un gráfico ASCII con puntos (x,y).
    Devuelve el contenido como string listo para imprimir en stdout.
    - x: lista de valores x
    - y: lista de valores y
    - width: ancho del área de dibujo (sin contar margen izquierdo para labels).
    - height: alto del área de dibujo.
    - left_margin: espacio para etiquetas Y (números).
    - point_char: carácter para representar los puntos de datos.
    - title: título opcional para el gráfico.
    """
    if width < 10 or height < 4:
        raise ValueError("width o height demasiado pequeño para renderizar")

    xmin = min(x)
    xmax = max(x)
    ymin = min(y)
    ymax = max(y)

    if xmax == xmin:
        xmin -= 0.5
        xmax += 0.5
    if ymax == ymin:
        ymin -= 0.5
        ymax += 0.5


    xpad = (xmax - xmin) * 0.04
    ypad = (ymax - ymin) * 0.08
    xmin -= xpad
    xmax += xpad
    ymin -= ypad
    ymax += ypad

    W = width
    H = height

    grid = [[' ' for _ in range(W)] for _ in range(H)]


    x0_in_range = ymin <= 0 <= ymax
    if x0_in_range:
        x_axis_row = _map_to_grid(0, 0, xmin, xmax, ymin, ymax, W, H)[1]
    else:
        x_axis_row = H - 1

    y0_in_range = xmin <= 0 <= xmax
    if y0_in_range:
        y_axis_col = _map_to_grid(0, 0, xmin, xmax, ymin, ymax, W, H)[0]
    else:
        y_axis_col = 0


    for c in range(W):

        if 0 <= x_axis_row < H:
            grid[x_axis_row][c] = '-' if grid[x_axis_row][c] == ' ' else grid[x_axis_row][c]
    for r in range(H):

        if 0 <= y_axis_col < W:
            grid[r][y_axis_col] = '|' if grid[r][y_axis_col] == ' ' else grid[r][y_axis_col]

    if 0 <= x_axis_row < H and 0 <= y_axis_col < W:
        grid[x_axis_row][y_axis_col] = '+'


    for xi, yi in zip(x, y):
        col, row = _map_to_grid(xi, yi, xmin, xmax, ymin, ymax, W, H)
        grid[row][col] = point_char


    max_ticks = min(5, H)
    ticks = []
    for i in range(max_ticks):
        t = i / (max_ticks - 1) if max_ticks > 1 else 0.5
        ytick_val = ymin + (1 - t) * (ymax - ymin)  
        _, row = _map_to_grid(xmin, ytick_val, xmin, xmax, ymin, ymax, W, H)
        ticks.append((row, ytick_val))

    lines: List[str] = []

    header_lines: List[str] = []
    if title:
        header_lines.append(title)

    for hl in header_lines:
        lines.append(' ' * left_margin + hl)

    tick_dict = {row: val for (row, val) in ticks}
    for row_idx in range(H):
        label = ""
        if row_idx in tick_dict:
            sval = f"{tick_dict[row_idx]:.3g}"
            label = sval.rjust(left_margin - 1) + ' '
        else:
            label = ' ' * left_margin

        row_str = ''.join(grid[row_idx])
        lines.append(label + row_str)

    x_ticks_count = min(5, W)
    x_tick_positions = []
    for i in range(x_ticks_count):
        t = i / (x_ticks_count - 1) if x_ticks_count > 1 else 0.5
        xv = xmin + t * (xmax - xmin)
        col, _ = _map_to_grid(xv, ymin, xmin, xmax, ymin, ymax, W, H)
        x_tick_positions.append((col, xv))

    footer = [' ' for _ in range(left_margin + W)]
    for col, xv in x_tick_positions:
        s = f"{xv:.3g}"
        start = left_margin + col - len(s) // 2

        for i, ch in enumerate(s):
            pos = start + i
            if 0 <= pos < len(footer):
                footer[pos] = ch
    lines.append(''.join(footer))

    return '\n'.join(lines)

def main():
    print("Prueba de render_ascii:")
    x = [-3, -2, -1, 0, 1, 2, 3]
    y = [4, -1, -4, -5, -4, -1, 4]

    art = render_ascii(x, y, width=60, height=15, title="Gráfico de función")
    print(art)
    
if __name__ == "__main__":
    main()