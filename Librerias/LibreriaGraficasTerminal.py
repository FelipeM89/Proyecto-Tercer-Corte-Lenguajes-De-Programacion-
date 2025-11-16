"""
LibreriaGraficasTerminal.py
Funciones para graficar y visualizar contenido en una nueva ventana de terminal.

Incluye:
- Apertura de nuevas ventanas de terminal
- Escritura de texto en la nueva terminal
- Gráficos ASCII en terminal
- Barras de progreso
- Tablas y diagramas
"""

import subprocess
import platform
import os
import tempfile

# -----------------------
# Gestión de Terminal
# -----------------------

class TerminalGrafico:
    """Clase para manejar una nueva terminal para gráficos y visualización."""
    
    def __init__(self):
        self.sistema = platform.system()
        self.script_path = None
    
    def abrir_nueva_terminal(self, titulo="Terminal Gráfica"):
        """
        Abre una nueva ventana de terminal.
        
        Args:
            titulo: Título de la ventana de terminal
        
        Returns:
            True si se abrió correctamente, False en caso contrario
        """
        try:
            if self.sistema == 'Windows':
                self.script_path = self._crear_script_temporal()
                os.system("start cmd /k python " + self.script_path)
            elif self.sistema == 'Darwin':  # macOS
                self.script_path = self._crear_script_temporal()
                subprocess.Popen([
                    'osascript', '-e',
                    f'tell app "Terminal" to do script "python3 {self.script_path}"'
                ])
            else:  # Linux
                self.script_path = self._crear_script_temporal()
                # Intentar con varios emuladores de terminal comunes
                terminales = ['gnome-terminal', 'xterm', 'konsole', 'xfce4-terminal']
                for terminal in terminales:
                    try:
                        if terminal == 'gnome-terminal':
                            subprocess.Popen([terminal, '--', 'python3', self.script_path])
                        else:
                            subprocess.Popen([terminal, '-e', f'python3 {self.script_path}'])
                        break
                    except FileNotFoundError:
                        continue
            
            return True
        except Exception as e:
            print(f"Error al abrir terminal: {e}")
            return False
    
    def _crear_script_temporal(self):
        """Crea un script temporal de Python que mantiene la terminal abierta."""
        fd, path = tempfile.mkstemp(suffix='.py', text=True)
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write("""
import sys
import time

print("=" * 60)
print("TERMINAL GRÁFICA - Lista para recibir comandos".center(60))
print("=" * 60)
print()

# Mantener la terminal abierta
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\\nCerrando terminal...")
""")
        return path

# -----------------------
# Funciones de Escritura
# -----------------------

def escribir_en_nueva_terminal(texto, titulo="Salida"):
    """
    Escribe texto en una nueva ventana de terminal.
    
    Args:
        texto: Texto a escribir
        titulo: Título de la ventana
    """
    sistema = platform.system()
    
    # Crear script temporal con el texto
    fd, script_path = tempfile.mkstemp(suffix='.py', text=True)
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        f.write(f"""
import sys

print("=" * 60)
print("{titulo}".center(60))
print("=" * 60)
print()
print('''{texto}''')
print()
print("=" * 60)
print("Presiona Enter para cerrar...")
input()
""")
    
    try:
        if sistema == 'Windows':
            subprocess.Popen(
                ['cmd', '-NoExit', '-File', script_path],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        elif sistema == 'Darwin':  # macOS
            subprocess.Popen([
                'osascript', '-e',
                f'tell app "Terminal" to do script "python3 {script_path}"'
            ])
        else:  # Linux
            subprocess.Popen(['gnome-terminal', '--', 'python3', script_path])
    except Exception as e:
        print(f"Error: {e}")

# -----------------------
# Gráficos ASCII
# -----------------------

def crear_barra_horizontal(porcentaje, ancho=50, caracter='*'):
    """
    Crea una barra de progreso horizontal en ASCII.
    
    Args:
        porcentaje: Porcentaje de completado (0-100)
        ancho: Ancho de la barra en caracteres
        caracter: Caracter para rellenar la barra
    
    Returns:
        String con la barra de progreso
    """
    lleno = int(ancho * porcentaje / 100)
    vacio = ancho - lleno
    return f"|{caracter * lleno}{' ' * vacio}| {porcentaje:.1f}%"

def crear_grafico_barras(datos, etiquetas=None, ancho_max=40):
    """
    Crea un gráfico de barras horizontal en ASCII.
    
    Args:
        datos: Lista de valores numéricos
        etiquetas: Lista opcional de etiquetas para cada barra
        ancho_max: Ancho máximo de la barra más grande
    
    Returns:
        String con el gráfico de barras
    """
    if not datos:
        return ""
    
    max_valor = max(datos)
    if max_valor == 0:
        max_valor = 1
    
    resultado = []
    max_etiqueta = max(len(str(e)) for e in (etiquetas or range(len(datos))))
    
    for i, valor in enumerate(datos):
        etiqueta = etiquetas[i] if etiquetas else str(i)
        longitud_barra = int((valor / max_valor) * ancho_max)
        barra = '█' * longitud_barra
        resultado.append(f"{etiqueta.ljust(max_etiqueta)} | {barra} {valor}")
    
    return '\n'.join(resultado)

def crear_caja(texto, ancho=None, padding=2):
    """
    Crea una caja ASCII alrededor de un texto.
    
    Args:
        texto: Texto a encerrar
        ancho: Ancho de la caja (None para auto)
        padding: Espacios de relleno interno
    
    Returns:
        String con la caja
    """
    lineas = texto.split('\n')
    if ancho is None:
        ancho = max(len(linea) for linea in lineas) + padding * 2
    
    resultado = []
    resultado.append('┌' + '─' * ancho + '┐')
    
    for linea in lineas:
        espacios = ancho - len(linea) - padding
        resultado.append(f"│{' ' * padding}{linea}{' ' * espacios}│")
    
    resultado.append('└' + '─' * ancho + '┘')
    return '\n'.join(resultado)

def crear_tabla_ascii(datos, encabezados=None):
    """
    Crea una tabla ASCII formateada.
    
    Args:
        datos: Lista de listas con los datos
        encabezados: Lista opcional de encabezados
    
    Returns:
        String con la tabla formateada
    """
    if not datos:
        return "(sin datos)"
    
    # Preparar datos
    if encabezados:
        todas_filas = [encabezados] + datos
    else:
        todas_filas = datos
    
    # Calcular anchos
    num_cols = len(todas_filas[0])
    anchos = [0] * num_cols
    
    for fila in todas_filas:
        for i, celda in enumerate(fila):
            anchos[i] = max(anchos[i], len(str(celda)))
    
    # Construir tabla
    resultado = []
    
    # Línea superior
    resultado.append('┌' + '┬'.join('─' * (w + 2) for w in anchos) + '┐')
    
    # Encabezados
    if encabezados:
        fila_str = '│'
        for i, celda in enumerate(encabezados):
            fila_str += f" {str(celda).ljust(anchos[i])} │"
        resultado.append(fila_str)
        resultado.append('├' + '┼'.join('─' * (w + 2) for w in anchos) + '┤')
        inicio = 1
    else:
        inicio = 0
    
    # Datos
    for fila in todas_filas[inicio:]:
        fila_str = '│'
        for i, celda in enumerate(fila):
            fila_str += f" {str(celda).ljust(anchos[i])} │"
        resultado.append(fila_str)
    
    # Línea inferior
    resultado.append('└' + '┴'.join('─' * (w + 2) for w in anchos) + '┘')
    
    return '\n'.join(resultado)

# -----------------------
# Funciones Combinadas
# -----------------------

def graficar_barras_en_terminal(datos, etiquetas=None, titulo="Gráfico de Barras"):
    """
    Muestra un gráfico de barras en una nueva terminal.
    
    Args:
        datos: Lista de valores numéricos
        etiquetas: Lista opcional de etiquetas
        titulo: Título del gráfico
    """
    grafico = crear_grafico_barras(datos, etiquetas)
    contenido = f"{titulo}\n\n{grafico}"
    escribir_en_nueva_terminal(contenido, titulo)

def graficar_tabla_en_terminal(datos, encabezados=None, titulo="Tabla de Datos"):
    """
    Muestra una tabla en una nueva terminal.
    
    Args:
        datos: Lista de listas con los datos
        encabezados: Lista opcional de encabezados
        titulo: Título de la tabla
    """
    tabla = crear_tabla_ascii(datos, encabezados)
    contenido = f"{titulo}\n\n{tabla}"
    escribir_en_nueva_terminal(contenido, titulo)

def mostrar_progreso_en_terminal(porcentaje, mensaje="Progreso", titulo="Estado"):
    """
    Muestra una barra de progreso en una nueva terminal.
    
    Args:
        porcentaje: Porcentaje de completado (0-100)
        mensaje: Mensaje descriptivo
        titulo: Título de la ventana
    """
    barra = crear_barra_horizontal(porcentaje)
    contenido = f"{mensaje}\n\n{barra}"
    escribir_en_nueva_terminal(contenido, titulo)

# -----------------------
# Pruebas
# -----------------------

if __name__ == "__main__":
    print("Pruebas de LibreriaGraficasTerminal")
    print("=" * 60)
    
    # Prueba 1: Escribir texto simple
    print("\n1. Abriendo nueva terminal con texto...")
    escribir_en_nueva_terminal(
        "¡Hola desde una nueva terminal!\n\nEste es un ejemplo de texto.",
        "Prueba de Escritura"
    )
    
    # Prueba 2: Gráfico de barras
    print("\n2. Mostrando gráfico de barras...")
    datos = [85, 92, 78, 95, 88]
    etiquetas = ["Python", "Java", "C++", "JavaScript", "Go"]
    graficar_barras_en_terminal(datos, etiquetas, "Lenguajes de Programación")
    
    # Prueba 3: Tabla
    print("\n3. Mostrando tabla...")
    datos_tabla = [
        ["Alice", 25, "Ingeniera"],
        ["Bob", 30, "Doctor"],
        ["Carol", 28, "Diseñadora"]
    ]
    encabezados = ["Nombre", "Edad", "Profesión"]
    graficar_tabla_en_terminal(datos_tabla, encabezados, "Datos de Empleados")
    
    # Prueba 4: Barra de progreso
    print("\n4. Mostrando barra de progreso...")
    mostrar_progreso_en_terminal(75, "Instalando paquetes...", "Progreso de Instalación")
    
    # Ejemplos en consola actual
    print("\n" + "=" * 60)
    print("EJEMPLOS EN CONSOLA ACTUAL:")
    print("=" * 60)
    
    print("\nCaja con texto:")
    print(crear_caja("Este es un mensaje\ncon múltiples líneas\n¡dentro de una caja!"))
    
    print("\nBarra de progreso:")
    print(crear_barra_horizontal(65))
    
    print("\nTabla ASCII:")
    print(crear_tabla_ascii(datos_tabla, encabezados))
