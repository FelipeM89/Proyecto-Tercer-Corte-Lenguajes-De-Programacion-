"""
LibreriaTablas.py
Impresión de tablas ASCII simples.
Funciones:
 - table_print(headers, rows)
 - pretty_format(value, width)
"""

def _widths(headers, rows):
    widths = [len(str(h)) for h in headers]
    for r in rows:
        for i,cell in enumerate(r):
            w = len(str(cell))
            if i >= len(widths):
                widths.append(w)
            else:
                if w > widths[i]:
                    widths[i] = w
    return widths

def table_print(headers, rows):
    widths = _widths(headers, rows)
    sep = "+" + "+".join("-"*(w+2) for w in widths) + "+"
    # header
    print(sep)
    header_row = "| " + " | ".join(str(h).ljust(widths[i]) for i,h in enumerate(headers)) + " |"
    print(header_row)
    print(sep)
    # rows
    for r in rows:
        row_s = "| " + " | ".join(str(r[i]).ljust(widths[i]) if i < len(r) else "".ljust(widths[i]) for i in range(len(widths))) + " |"
        print(row_s)
    print(sep)
    return True

if __name__ == "__main__":
    headers = ["id","name","score"]
    rows = [[1,"Ana",9.5],[2,"Luis",8.2]]
    table_print(headers, rows)