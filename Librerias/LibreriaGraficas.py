"""
LibreriaGraficas.py
Gráficas ASCII simples:
 - guardar_puntos(path, xs, ys)
 - print_hist(vals, bins)
"""

from Librerias.LibreriaArchivoGestion import escribir_txt


def guardar_puntos(path, xs, ys):
    lines = []
    n = min(len(xs), len(ys))
    for i in range(n):
        lines.append(f"{xs[i]},{ys[i]}")
    escribir_txt(path, "\n".join(lines))
    return True

def print_hist(vals, bins=10):
    if not vals:
        print("(sin datos)")
        return
    mn = min(vals); mx = max(vals)
    if mx == mn: mx = mn + 1
    width = 50
    counts = [0]*bins
    step = (mx - mn) / bins
    for v in vals:
        idx = int((v - mn) / (mx - mn) * bins)
        if idx == bins: idx = bins - 1
        counts[idx] += 1
    for i,c in enumerate(counts):
        bar = "#" * int(c / max(1, max(counts)) * width)
        print(f"{i:02d}: {bar} ({c})")
    return counts

if __name__ == "__main__":

    print("\nHistograma ASCII:")
    print_hist([1,2,2,3,3,3,4,4,4,4,5,5,5,5,5], bins=5)
    guardar_puntos("puntos.csv", [1,2,3,4], [2,4,6,8])