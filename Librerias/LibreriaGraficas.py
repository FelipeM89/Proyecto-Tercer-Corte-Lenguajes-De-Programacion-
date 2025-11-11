"""
mylib_graficas.py
Funcionalidades simples de graficado sin usar librerías externas:
- graficado ASCII (histograma / line plot muy simple)
- guardar puntos en archivo (para graficar fuera si se desea)
- transformación de datos para visualización
"""

from libs.mylib_archivos import escribir_archivo_texto  # interno al paquete libs

def _normalizar_lista(vals, max_width):
    if not vals:
        return []
    mn = min(vals)
    mx = max(vals)
    if mx == mn:
        return [max_width // 2 for _ in vals]
    return [int((v - mn) / (mx - mn) * max_width) for v in vals]

def graficar_barras_ascii(vals, max_width=50, simbolo="█"):
    """Imprime una gráfica de barras en ASCII, una barra por valor."""
    bars = _normalizar_lista(vals, max_width)
    for i, b in enumerate(bars):
        print(f"{i:>3}: {simbolo * b} ({vals[i]})")

def graficar_linea_ascii(vals, width=60, height=20):
    """Dibuja una gráfica de línea simple en una rejilla ASCII.
    - width: columnas de la trama
    - height: filas de la trama
    """
    if not vals:
        print("(sin datos)")
        return
    n = len(vals)
    # muestrear / interpolar valores a 'width' columnas
    if n <= width:
        sampled = vals[:]
    else:
        # tomar promedios por bloque
        block = n / width
        sampled = []
        for i in range(width):
            start = int(i * block)
            end = int((i+1) * block)
            if end <= start:
                end = start + 1
                if end > n: end = n
            block_vals = vals[start:end]
            sampled.append(sum(block_vals) / len(block_vals))
    # normalizar a `height`
    mn = min(sampled); mx = max(sampled)
    if mx == mn:
        rows = [height // 2 for _ in sampled]
    else:
        rows = [int((v - mn) / (mx - mn) * (height-1)) for v in sampled]
    # crear matriz de espacios
    canvas = [[" " for _ in range(len(sampled))] for _ in range(height)]
    for col, r in enumerate(rows):
        row_idx = height - 1 - r
        canvas[row_idx][col] = "*"
    # imprimir
    for row in canvas:
        print("".join(row))

def guardar_puntos(path, xs, ys):
    """Guarda dos listas de puntos en CSV 'x,y' para graficar externamente."""
    lines = []
    n = min(len(xs), len(ys))
    for i in range(n):
        lines.append(f"{xs[i]},{ys[i]}")
    escribir_archivo_texto(path, "\n".join(lines))
    return True

if __name__ == "__main__":
    print("Pruebas mylib_graficas:")
    data = [1, 5, 3, 8, 7, 2, 10, 6]
    print("Barras ASCII:")
    graficar_barras_ascii(data)
    print("\nLínea ASCII:")
    graficar_linea_ascii(data, width=40, height=10)