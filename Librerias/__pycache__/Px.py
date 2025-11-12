import sys
import os

def _enable_vt_mode_windows():
    """
    Habilita procesamiento de secuencias ANSI en Windows (si es posible).
    No falla si no está disponible.
    """
    if os.name != "nt":
        return
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        h = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE = -11
        mode = ctypes.c_uint()
        if kernel32.GetConsoleMode(h, ctypes.byref(mode)) == 0:
            return
        ENABLE_VT_PROCESSING = 0x0004
        new_mode = mode.value | ENABLE_VT_PROCESSING
        kernel32.SetConsoleMode(h, new_mode)
    except Exception:
        # si no podemos activar no hacemos nada (seguir con best-effort)
        pass

_enable_vt_mode_windows()

def goto(row: int, col: int):
    """
    Mueve el cursor a la posición (row, col). Ambas 1-based.
    Ejemplo: goto(5,10) -> fila 5, columna 10.
    """
    # Validar enteros
    if not (isinstance(row, int) and isinstance(col, int)):
        raise TypeError("row y col deben ser enteros")
    if row < 1 or col < 1:
        raise ValueError("row y col deben ser >= 1")
    # Secuencia ANSI CSI r ; c H  (también puede usarse 'f'): ESC[{r};{c}H
    sys.stdout.write(f"\x1b[{row};{col}H")
    sys.stdout.flush()

def put_at(row: int, col: int, text: str, end: str = ""):
    """
    Mueve el cursor a (row,col) y escribe `text`.
    `end` se pasa a la impresión final (por defecto nada).
    """
    goto(row, col)
    sys.stdout.write(str(text) + end)
    sys.stdout.flush()

# utilidades opcionales
def save_cursor():
    """Guardar posición actual del cursor (ESC7 o ESC[s)."""
    sys.stdout.write("\x1b7")
    sys.stdout.flush()

def restore_cursor():
    """Restaurar posición guardada del cursor (ESC8 o ESC[u)."""
    sys.stdout.write("\x1b8")
    sys.stdout.flush()

def clear_line():
    """Borra la línea actual (de cursor a fin de línea)."""
    sys.stdout.write("\x1b[2K")
    sys.stdout.flush()

if __name__ == "__main__":
    # Ejemplo de uso:
    import time
    print("Esto imprime, luego moveremos el cursor y escribiremos en fila 10 columna 20.")
    time.sleep(1)
    put_at(40,140, "W")
    time.sleep(0)
    # restaurar cursor al final para no sobreescribir prompt
    ##put_at(20, 1, "\n")