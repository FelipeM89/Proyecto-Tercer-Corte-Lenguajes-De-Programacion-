"""
LibreriaGraficasTerminal.py
Funciones más sencillas para mostrar datos en terminal.
 - plot_points(xs, ys)
 - print_hist(vals, bins)
"""

def plot_points(xs, ys, width=60, height=20):
    if not xs or not ys:
        print("(sin datos)")
        return
    # normalize to grid
    mnx = min(xs); mxx = max(xs)
    mny = min(ys); mxy = max(ys)
    if mxx == mnx: mxx = mnx + 1
    if mxy == mny: mxy = mny + 1
    grid = [[" " for _ in range(width)] for _ in range(height)]
    for x,y in zip(xs,ys):
        cx = int((x - mnx) / (mxx - mnx) * (width - 1))
        cy = int((y - mny) / (mxy - mny) * (height - 1))
        grid[height - 1 - cy][cx] = "o"
    for row in grid:
        print("".join(row))
    return grid

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