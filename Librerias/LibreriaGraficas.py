"""
LibreriaGraficas.py
Gráficas ASCII simples:
 - graficar_barras_ascii(vals, max_width, simbolo)
 - graficar_linea_ascii(vals, width, height)
 - guardar_puntos(path, xs, ys)
"""

from Librerias.LibreriaArchivoGestion import escribir_txt

def _normalizar_lista(vals, max_width):
    if not vals:
        return []
    mn = min(vals); mx = max(vals)
    if mx == mn:
        return [max_width//2 for _ in vals]
    return [int((v - mn)/(mx-mn) * max_width) for v in vals]

def graficar_barras_ascii(vals, max_width=50, simbolo="█"):
    bars = _normalizar_lista(vals, max_width)
    out = []
    for i,b in enumerate(bars):
        line = f"{i:>3}: {simbolo * b} ({vals[i]})"
        print(line)
        out.append(line)
    return out

def graficar_linea_ascii(vals, width=60, height=20):
    if not vals:
        print("(sin datos)")
        return []
    n = len(vals)
    if n <= width:
        sampled = vals[:]
    else:
        block = n / width
        sampled = []
        for i in range(width):
            start = int(i*block)
            end = int((i+1)*block)
            if end <= start:
                end = start + 1
                if end > n: end = n
            block_vals = vals[start:end]
            sampled.append(sum(block_vals) / len(block_vals))
    mn = min(sampled); mx = max(sampled)
    if mx == mn:
        rows = [height//2 for _ in sampled]
    else:
        rows = [int((v - mn)/(mx - mn) * (height-1)) for v in sampled]
    canvas = [[" " for _ in range(len(sampled))] for _ in range(height)]
    for col, r in enumerate(rows):
        row_idx = height - 1 - r
        canvas[row_idx][col] = "*"
    for row in canvas:
        print("".join(row))
    return canvas

def guardar_puntos(path, xs, ys):
    lines = []
    n = min(len(xs), len(ys))
    for i in range(n):
        lines.append(f"{xs[i]},{ys[i]}")
    escribir_txt(path, "\n".join(lines))
    return True