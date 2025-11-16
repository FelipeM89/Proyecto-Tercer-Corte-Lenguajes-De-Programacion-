"""
mylib_terminal.py
Funciones para ejecutar comandos del sistema operativo y escribir en la terminal.

Incluye:
- ejecución de comandos del sistema con captura de salida
- ejecución de comandos con salida directa a terminal
- escritura y formateo de texto en terminal
- información del sistema operativo
"""

import subprocess
import sys
import platform

# -----------------------
# Ejecución de comandos
# -----------------------

def ejecutar_comando(comando, capturar_salida=True, shell=True):
    """
    Ejecuta un comando del sistema operativo.
    
    Args:
        comando: String con el comando a ejecutar
        capturar_salida: Si es True, retorna la salida. Si es False, imprime directamente
        shell: Si es True, ejecuta el comando a través del shell
    
    Returns:
        Si capturar_salida=True: diccionario con 'salida', 'error' y 'codigo'
        Si capturar_salida=False: código de retorno
    """
    try:
        if capturar_salida:
            resultado = subprocess.run(
                comando,
                shell=shell,
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='replace'
            )
            return {
                'salida': resultado.stdout,
                'error': resultado.stderr,
                'codigo': resultado.returncode
            }
        else:
            resultado = subprocess.run(comando, shell=shell)
            return resultado.returncode
    except Exception as e:
        if capturar_salida:
            return {
                'salida': '',
                'error': str(e),
                'codigo': -1
            }
        else:
            print(f"Error ejecutando comando: {e}")
            return -1

def ejecutar_y_mostrar(comando, shell=True):
    """
    Ejecuta un comando y muestra su salida directamente en la terminal.
    
    Args:
        comando: String con el comando a ejecutar
        shell: Si es True, ejecuta el comando a través del shell
    
    Returns:
        Código de retorno del comando
    """
    return ejecutar_comando(comando, capturar_salida=False, shell=shell)

def ejecutar_y_capturar(comando, shell=True):
    """
    Ejecuta un comando y captura su salida.
    
    Args:
        comando: String con el comando a ejecutar
        shell: Si es True, ejecuta el comando a través del shell
    
    Returns:
        Diccionario con 'salida', 'error' y 'codigo'
    """
    return ejecutar_comando(comando, capturar_salida=True, shell=shell)

# -----------------------
# Información del sistema
# -----------------------

def obtener_sistema_operativo():
    """Retorna el nombre del sistema operativo."""
    return platform.system()

def obtener_informacion_sistema():
    """
    Retorna información detallada del sistema.
    
    Returns:
        Diccionario con información del sistema
    """
    return {
        'sistema': platform.system(),
        'version': platform.version(),
        'arquitectura': platform.machine(),
        'procesador': platform.processor(),
        'plataforma': platform.platform(),
        'python_version': platform.python_version()
    }

# -----------------------
# Escritura en terminal
# -----------------------

def escribir_terminal(texto, fin='\n'):
    """
    Escribe texto en la terminal.
    
    Args:
        texto: Texto a escribir
        fin: Caracter final (por defecto salto de línea)
    """
    print(texto, end=fin)

def escribir_linea(texto=''):
    """Escribe una línea de texto en la terminal."""
    print(texto)

def escribir_separador(caracter='-', longitud=50):
    """Escribe una línea separadora en la terminal."""
    print(caracter * longitud)

def escribir_titulo(titulo, caracter='=', longitud=50):
    """
    Escribe un título centrado con separadores.
    
    Args:
        titulo: Texto del título
        caracter: Caracter para el separador
        longitud: Longitud de la línea separadora
    """
    escribir_separador(caracter, longitud)
    print(titulo.center(longitud))
    escribir_separador(caracter, longitud)

def escribir_tabla(datos, encabezados=None):
    """
    Escribe una tabla simple en la terminal.
    
    Args:
        datos: Lista de listas con los datos
        encabezados: Lista opcional con los nombres de las columnas
    """
    if not datos:
        print("(sin datos)")
        return
    
    # Calcular anchos de columna
    if encabezados:
        datos_con_encabezado = [encabezados] + datos
    else:
        datos_con_encabezado = datos
    
    num_cols = len(datos_con_encabezado[0])
    anchos = [0] * num_cols
    
    for fila in datos_con_encabezado:
        for i, celda in enumerate(fila):
            anchos[i] = max(anchos[i], len(str(celda)))
    
    # Imprimir encabezados si existen
    if encabezados:
        for i, enc in enumerate(encabezados):
            print(str(enc).ljust(anchos[i] + 2), end='')
        print()
        print('-' * (sum(anchos) + 2 * num_cols))
    
    # Imprimir datos
    inicio = 1 if encabezados else 0
    for fila in datos_con_encabezado[inicio:]:
        for i, celda in enumerate(fila):
            print(str(celda).ljust(anchos[i] + 2), end='')
        print()

def limpiar_terminal():
    """Limpia la terminal según el sistema operativo."""
    sistema = obtener_sistema_operativo()
    if sistema == 'Windows':
        ejecutar_y_mostrar('cls')
    else:
        ejecutar_y_mostrar('clear')

# -----------------------
# Funciones combinadas
# -----------------------

def ejecutar_y_graficar_salida(comando, shell=True):
    """
    Ejecuta un comando y muestra su salida formateada.
    
    Args:
        comando: String con el comando a ejecutar
        shell: Si es True, ejecuta el comando a través del shell
    """
    escribir_titulo(f"Ejecutando: {comando}")
    resultado = ejecutar_y_capturar(comando, shell)
    
    if resultado['salida']:
        escribir_linea("\n--- SALIDA ---")
        escribir_linea(resultado['salida'])
    
    if resultado['error']:
        escribir_linea("\n--- ERROR ---")
        escribir_linea(resultado['error'])
    
    escribir_linea(f"\n--- Código de retorno: {resultado['codigo']} ---")
    return resultado

# -----------------------
# Pruebas rápidas
# -----------------------

if __name__ == "__main__":
    print("Pruebas mylib_terminal:")
    
    # Información del sistema
    escribir_titulo("Información del Sistema")
    info = obtener_informacion_sistema()
    for clave, valor in info.items():
        print(f"{clave}: {valor}")
    
    # Tabla de ejemplo
    print("\n")
    escribir_titulo("Ejemplo de Tabla")
    datos = [
        ["Python", "3.x", "Lenguaje"],
        ["Bash", "5.x", "Shell"],
        ["PowerShell", "7.x", "Shell"]
    ]
    escribir_tabla(datos, ["Herramienta", "Versión", "Tipo"])
    
    # Ejecución de comando simple
    print("\n")
    escribir_titulo("Comando Simple")
    if obtener_sistema_operativo() == 'Windows':
        resultado = ejecutar_y_capturar('echo Hola desde Windows')
    else:
        resultado = ejecutar_y_capturar('echo "Hola desde Unix/Linux"')
    print(f"Salida: {resultado['salida'].strip()}")
    print(f"Código: {resultado['codigo']}")
