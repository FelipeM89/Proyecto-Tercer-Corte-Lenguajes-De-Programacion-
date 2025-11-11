"""
mylib_archivos.py
Funciones para lectura/escritura de archivos de texto (UTF-8),
y utilidades de manejo de datos (guardar listas, cargar listas numéricas).
"""

def leer_archivo_texto(path):
    """Lee todo el archivo y devuelve una cadena."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def escribir_archivo_texto(path, contenido):
    """Escribe contenido (string) en archivo (sobrescribe)."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(contenido)
    return True

def append_archivo_texto(path, contenido):
    """Agrega una línea o texto al final del archivo."""
    with open(path, "a", encoding="utf-8") as f:
        f.write(contenido)
    return True

def guardar_lista_como_csv(path, lista, separador=","):
    """
    Guarda una lista de listas como CSV simple.
    lista = [[a,b,c], [d,e,f], ...]
    """
    lines = []
    for row in lista:
        lines.append(separador.join(str(x) for x in row))
    escribir_archivo_texto(path, "\n".join(lines))
    return True

def cargar_lista_de_csv(path, separador=",", tipo=float):
    """Carga archivo CSV simple y retorna lista de listas (tipo por elemento)."""
    text = leer_archivo_texto(path)
    lines = [ln for ln in text.splitlines() if ln.strip() != ""]
    result = []
    for ln in lines:
        parts = [p.strip() for p in ln.split(separador)]
        result.append([tipo(p) for p in parts])
    return result

if __name__ == "__main__":
    print("Pruebas mylib_archivos:")
    escribir_archivo_texto("test_archivo.txt", "hola\n1,2,3\n")
    print("Contenido:", leer_archivo_texto("test_archivo.txt"))
    guardar_lista_como_csv("test_matriz.csv", [[1,2,3],[4,5,6]])
    print("CSV cargado:", cargar_lista_de_csv("test_matriz.csv"))