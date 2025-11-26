"""
LibreriaGraficas.py
Gráficas ASCII simples con guardado automático:
 - guardar_puntos(path, xs, ys)
 - print_hist(vals, bins)
 - graficar_puntos_ascii(xs, ys, width, height, title, archivo)
 - graficar_linea_ascii(vals, width, height, title, archivo)
 - guardar_grafica_ascii(contenido, archivo)
"""

from Librerias.LibreriaArchivoGestion import escribir_txt


def guardar_puntos(path, xs, ys):
    """Guarda puntos X,Y en formato CSV"""
    lines = []
    n = min(len(xs), len(ys))
    for i in range(n):
        lines.append(f"{xs[i]},{ys[i]}")
    escribir_txt(path, "\n".join(lines))
    return True


def guardar_grafica_ascii(contenido, archivo):
    """
    Guarda el contenido de una gráfica ASCII en un archivo
    
    Args:
        contenido: String con el contenido de la gráfica
        archivo: Ruta del archivo donde guardar
    """
    try:
        escribir_txt(archivo, contenido)
        print(f"✓ Gráfica guardada en: {archivo}")
        return True
    except Exception as e:
        print(f"✗ Error al guardar gráfica: {e}")
        return False


def graficar_puntos_ascii(xs, ys, width=60, height=20, title=None, archivo=None):
    """
    Crea un scatter plot ASCII de puntos X,Y
    
    Args:
        xs: Lista de valores X
        ys: Lista de valores Y
        width: Ancho de la gráfica
        height: Altura de la gráfica
        title: Título opcional
        archivo: Si se proporciona, guarda la gráfica en este archivo
        
    Returns:
        String con la gráfica ASCII
    """
    if not xs or not ys:
        return "(sin datos)"
    
    if len(xs) != len(ys):
        raise ValueError("xs e ys deben tener la misma longitud")
    
    # Encontrar rangos
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    
    # Evitar división por cero
    if max_x == min_x:
        max_x = min_x + 1
    if max_y == min_y:
        max_y = min_y + 1
    
    # Crear grid
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Mapear puntos al grid
    for x, y in zip(xs, ys):
        col = int((x - min_x) / (max_x - min_x) * (width - 1))
        row = height - 1 - int((y - min_y) / (max_y - min_y) * (height - 1))
        if 0 <= row < height and 0 <= col < width:
            grid[row][col] = '●'
    
    # Construir salida
    lines = []
    
    if title:
        lines.append(f"\n{title}")
        lines.append("=" * len(title))
    
    lines.append("+" + "-" * width + "+")
    for row in grid:
        lines.append("|" + "".join(row) + "|")
    lines.append("+" + "-" * width + "+")
    lines.append(f"X: [{min_x:.2f}, {max_x:.2f}]  Y: [{min_y:.2f}, {max_y:.2f}]")
    
    output = "\n".join(lines)
    
    # Mostrar en consola
    print(output)
    
    # Guardar en archivo si se especifica
    if archivo:
        guardar_grafica_ascii(output, archivo)
    
    return output


def graficar_linea_ascii(vals, width=60, height=15, title=None, archivo=None):
    """
    Crea un gráfico de línea ASCII
    
    Args:
        vals: Lista de valores Y (X será automático 0,1,2,...)
        width: Ancho de la gráfica
        height: Altura de la gráfica
        title: Título opcional
        archivo: Si se proporciona, guarda la gráfica en este archivo
        
    Returns:
        String con la gráfica ASCII
    """
    if not vals:
        return "(sin datos)"
    
    min_v, max_v = min(vals), max(vals)
    
    if max_v == min_v:
        max_v = min_v + 1
    
    # Crear grid
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Mapear valores
    n = len(vals)
    for i, v in enumerate(vals):
        col = int(i / max(1, n - 1) * (width - 1)) if n > 1 else 0
        row = height - 1 - int((v - min_v) / (max_v - min_v) * (height - 1))
        if 0 <= row < height and 0 <= col < width:
            grid[row][col] = '●'
    
    # Construir salida
    lines = []
    
    if title:
        lines.append(f"\n{title}")
        lines.append("=" * len(title))
    
    lines.append(f"Max: {max_v:.4f}")
    lines.append("+" + "-" * width + "+")
    for row in grid:
        lines.append("|" + "".join(row) + "|")
    lines.append("+" + "-" * width + "+")
    lines.append(f"Min: {min_v:.4f}")
    lines.append(f"Puntos: {len(vals)}")
    
    output = "\n".join(lines)
    
    # Mostrar en consola
    print(output)
    
    # Guardar en archivo si se especifica
    if archivo:
        guardar_grafica_ascii(output, archivo)
    
    return output


def print_hist(vals, bins=10, archivo=None):
    """
    Imprime un histograma ASCII
    
    Args:
        vals: Lista de valores
        bins: Número de bins
        archivo: Si se proporciona, guarda el histograma en este archivo
    """
    if not vals:
        output = "(sin datos)"
        print(output)
        return
    
    mn = min(vals)
    mx = max(vals)
    if mx == mn:
        mx = mn + 1
    
    width = 50
    counts = [0] * bins
    
    for v in vals:
        idx = int((v - mn) / (mx - mn) * bins)
        if idx == bins:
            idx = bins - 1
        counts[idx] += 1
    
    lines = []
    lines.append("\nHistograma:")
    lines.append("-" * 60)
    
    for i, c in enumerate(counts):
        bar = "#" * int(c / max(1, max(counts)) * width)
        lines.append(f"{i:02d}: {bar} ({c})")
    
    output = "\n".join(lines)
    print(output)
    
    # Guardar en archivo si se especifica
    if archivo:
        guardar_grafica_ascii(output, archivo)
    
    return counts


if __name__ == "__main__":
    print("\n=== Pruebas de LibreriaGraficas ===\n")
    
    # Test 1: Histograma
    print("1. Histograma ASCII:")
    print_hist([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5], bins=5)
    
    # Test 2: Scatter plot
    print("\n2. Gráfica de puntos:")
    xs = [1, 2, 3, 4, 5, 6, 7]
    ys = [2, 4, 3, 5, 4, 6, 5]
    graficar_puntos_ascii(xs, ys, width=40, height=15, title="Datos de ejemplo")
    
    # Test 3: Gráfica de línea
    print("\n3. Gráfica de línea:")
    vals = [1, 3, 2, 5, 4, 6, 5, 7, 6, 8]
    graficar_linea_ascii(vals, width=50, height=12, title="Serie temporal")
    
    # Test 4: Guardar puntos CSV
    guardar_puntos("puntos_test.csv", [1, 2, 3, 4], [2, 4, 6, 8])
    print("\n✓ Puntos guardados en puntos_test.csv")