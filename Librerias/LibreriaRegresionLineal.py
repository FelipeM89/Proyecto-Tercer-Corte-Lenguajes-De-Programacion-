from typing import List, Optional
from Librerias.LibreriaAritmentica import sqrt
from Librerias.LibreriaFunciones import mean, mse, mae, regresion_lineal, predict_linear



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



class regresion_lineal_model:
    def __init__(self):
        self.m=None
        self.b=None
        self.x_train=None
        self.y_train=None
        self.y_pred=None
    def fit(self,x,y):
        """ Ajusta el modelo de regresión lineal a los datos (x, y). """
        self.x_train = list(x)
        self.y_train = list(y)
        self.m, self.b = regresion_lineal(x, y)
        self.y_pred = self.predict(x)
        return self
    def predict(self, x):
        """ Predice los valores dados una lista de x usando el modelo ajustado. """
        if self.m is None:
            raise ValueError("Modelo no ajustado. Llama fit() primero.")
        return predict_linear(x, self.m, self.b)
    def mse(self):
        """ Calcula el Error Cuadrático Medio (MSE) del modelo ajustado. """
        return mse(self.y_train, self.y_pred)  
    def mae(self):
        """ Calcula el Error Absoluto Medio (MAE) del modelo ajustado. """
        return mae(self.y_train, self.y_pred)
    def r2(self):
        """ Calcula el coeficiente de determinación R² del modelo ajustado. """
        my = mean(self.y_train)
        ss_res = sum((yt - yp) ** 2 for yt, yp in zip(self.y_train, self.y_pred))
        ss_tot = sum((yt - my) ** 2 for yt in self.y_train)
        return 1.0 - ss_res / ss_tot if ss_tot != 0 else 0.0
    def rmse(self):
        """ Calcula la raíz del error cuadrático medio (RMSE) del modelo ajustado. """
        return sqrt(self.mse())
    
    def render_ascii_regression(self,
                                width: int = 80, 
                                height: int = 20,
                                left_margin: int = 9,
                                point_char: str = '*', 
                                line_char: str = '-',
                                title: Optional[str] = None,
                                show_stats: bool = True) -> str:
        """
        Renderiza un gráfico ASCII con puntos (x,y) y la recta de regresiOn y = m x + b.
        Devuelve el contenido como string
        - width: ancho del Area de dibujo (sin contar margen izquierdo para labels).
        - height: alto del Area de dibujo.
        - left_margin: espacio para etiquetas.
        - point_char: caracter para representar los puntos de datos.
        - line_char: caracter para representar la línea de regresión.
        - title: titulo opcional para el gráfico.
        - show_stats: mostrar estadísticas de la regresión.
        """
        if self.m is None or self.b is None:
            raise ValueError("Modelo no ajustado. Llama fit() primero.")
        
        x = self.x_train
        y = self.y_train
        m = self.m
        b = self.b
        
        if width < 10 or height < 4:
            raise ValueError("width o height demasiado pequeño para renderizar")

        # Determinar rangos con un pequeño padding
        xmin = min(x)
        xmax = max(x)
        ymin = min(y)
        ymax = max(y)

        # Añadir margen si rango es cero
        if xmax == xmin:
            xmin -= 0.5
            xmax += 0.5
        if ymax == ymin:
            ymin -= 0.5
            ymax += 0.5

        # Expande rangos un poco para que puntos no queden pegados a los bordes
        xpad = (xmax - xmin) * 0.04
        ypad = (ymax - ymin) * 0.08
        xmin -= xpad
        xmax += xpad
        ymin -= ypad
        ymax += ypad

        W = width
        H = height

        # Grid de caracteres (H filas, W columnas)
        grid = [[' ' for _ in range(W)] for _ in range(H)]

        # Dibujar eje X (en la fila correspondiente a y=0 si está en rango, si no en borde inferior)
        x0_in_range = ymin <= 0 <= ymax
        if x0_in_range:
            x_axis_row = _map_to_grid(0, 0, xmin, xmax, ymin, ymax, W, H)[1]
        else:
            x_axis_row = H - 1

        # Dibujar eje Y (columna correspondiente a x=0 si está en rango, si no en borde izquierdo)
        y0_in_range = xmin <= 0 <= xmax
        if y0_in_range:
            y_axis_col = _map_to_grid(0, 0, xmin, xmax, ymin, ymax, W, H)[0]
        else:
            y_axis_col = 0

        # Dibujar ejes en grid
        for c in range(W):
            # si hay eje X, marcar '-'
            if 0 <= x_axis_row < H:
                grid[x_axis_row][c] = '-' if grid[x_axis_row][c] == ' ' else grid[x_axis_row][c]
        for r in range(H):
            # si hay eje Y, marcar '|'
            if 0 <= y_axis_col < W:
                grid[r][y_axis_col] = '|' if grid[r][y_axis_col] == ' ' else grid[r][y_axis_col]

        # Cruce ejes
        if 0 <= x_axis_row < H and 0 <= y_axis_col < W:
            grid[x_axis_row][y_axis_col] = '+'

        # Dibujar puntos
        for xi, yi in zip(x, y):
            col, row = _map_to_grid(xi, yi, xmin, xmax, ymin, ymax, W, H)
            grid[row][col] = point_char

        # Dibujar línea de regresión muestreando X a lo largo del ancho
        # Tomamos más muestras que columnas para continuidad y conectamos
        sample_count = max(W * 2, 200)
        prev_col = prev_row = None
        for i in range(sample_count):
            t = i / (sample_count - 1)
            xv = xmin + t * (xmax - xmin)
            yv = m * xv + b
            col, row = _map_to_grid(xv, yv, xmin, xmax, ymin, ymax, W, H)
            # Si hay punto ya, priorizamos punto_char; si no, colocamos line_char
            if grid[row][col] == ' ':
                grid[row][col] = line_char
            if prev_col is not None and prev_row is not None:
                # Interpolar columnas entre prev_col y col en la misma fila(s) si necesario
                if prev_row == row:

                    c1 = min(prev_col, col)
                    c2 = max(prev_col, col)
                    for c in range(c1, c2 + 1):
                        if grid[row][c] == ' ':
                            grid[row][c] = line_char
                else:
                    if grid[row][col] == ' ':
                        grid[row][col] = line_char
                    if grid[prev_row][prev_col] == ' ':
                        grid[prev_row][prev_col] = line_char
            prev_col, prev_row = col, row

        max_ticks = min(5, H)
        ticks = []
        for i in range(max_ticks):
            t = i / (max_ticks - 1) if max_ticks > 1 else 0.5
            ytick_val = ymin + (1 - t) * (ymax - ymin)  # descendente (row 0 arriba)

            _, row = _map_to_grid(xmin, ytick_val, xmin, xmax, ymin, ymax, W, H)
            ticks.append((row, ytick_val))

        lines: List[str] = []

        header_lines: List[str] = []
        if title:
            header_lines.append(title)
        if show_stats:

            header_lines.append(f"y = {m:.6g} x + {b:.6g}")

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
    # Parámetros por default
    width = 100
    height = 20
    left_margin = 10
    
    x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    y = [15, 28, 42, 55, 68, 82, 95, 108, 122, 135]

    # Crear instancia y ajustar el modelo
    modelo = regresion_lineal_model()
    modelo.fit(x, y)
    
    # Calcular métricas
    r2 = modelo.r2()
    rmse_val = modelo.rmse()

    # Render ASCII usando el método de la clase
    title = f"Regresión lineal el python (m={modelo.m:.6g}, b={modelo.b:.6g}, R²={r2:.6g}, RMSE={rmse_val:.6g})"
    art = modelo.render_ascii_regression(
        width=width - left_margin, 
        height=height,
        left_margin=left_margin, 
        point_char='*', 
        line_char='-',
        title=title, 
        show_stats=False
    )
    print(art)

    print()
    print(f"Ecuación: y = {modelo.m:.6g} x + {modelo.b:.6g}")
    print(f"R² = {r2:.6g}    RMSE = {rmse_val:.6g}")

if __name__ == "__main__":
    main()