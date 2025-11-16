import os
import sys
import importlib.util
import types
import tempfile
import io
from contextlib import redirect_stdout


def load_module(fname, modname):
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Librerias'))
    path = os.path.join(base, fname)
    spec = importlib.util.spec_from_file_location(modname, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_ejecutar_comando_capturar():
    """Test ejecutar comando con captura de salida"""
    m = load_module('LibreriaTerminal.py', 'terminal')
    
    # Test comando simple
    resultado = m.ejecutar_y_capturar('echo "test"')
    assert resultado['codigo'] == 0
    assert 'test' in resultado['salida']
    assert resultado['error'] == ''


def test_obtener_sistema_operativo():
    """Test obtener información del sistema operativo"""
    m = load_module('LibreriaTerminal.py', 'terminal')
    
    sistema = m.obtener_sistema_operativo()
    assert sistema in ['Linux', 'Windows', 'Darwin', 'Java']
    assert isinstance(sistema, str)
    assert len(sistema) > 0


def test_obtener_informacion_sistema():
    """Test obtener información detallada del sistema"""
    m = load_module('LibreriaTerminal.py', 'terminal')
    
    info = m.obtener_informacion_sistema()
    assert isinstance(info, dict)
    assert 'sistema' in info
    assert 'version' in info
    assert 'arquitectura' in info
    assert 'plataforma' in info
    assert 'python_version' in info


def test_escribir_terminal():
    """Test escribir en terminal"""
    m = load_module('LibreriaTerminal.py', 'terminal')
    
    # Capturar salida
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        m.escribir_terminal("Hola mundo")
    
    salida = buffer.getvalue()
    assert "Hola mundo" in salida


def test_escribir_linea():
    """Test escribir línea en terminal"""
    m = load_module('LibreriaTerminal.py', 'terminal')
    
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        m.escribir_linea("Test line")
    
    salida = buffer.getvalue()
    assert "Test line" in salida


def test_escribir_separador():
    """Test escribir separador en terminal"""
    m = load_module('LibreriaTerminal.py', 'terminal')
    
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        m.escribir_separador('-', 20)
    
    salida = buffer.getvalue()
    assert '-' * 20 in salida


def test_escribir_titulo():
    """Test escribir título en terminal"""
    m = load_module('LibreriaTerminal.py', 'terminal')
    
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        m.escribir_titulo("Mi Titulo", '=', 30)
    
    salida = buffer.getvalue()
    assert "Mi Titulo" in salida
    assert '=' in salida


def test_escribir_tabla():
    """Test escribir tabla en terminal"""
    m = load_module('LibreriaTerminal.py', 'terminal')
    
    datos = [
        ["A", "B", "C"],
        ["1", "2", "3"]
    ]
    encabezados = ["Col1", "Col2", "Col3"]
    
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        m.escribir_tabla(datos, encabezados)
    
    salida = buffer.getvalue()
    assert "Col1" in salida
    assert "A" in salida
    assert "1" in salida


def test_escribir_tabla_sin_encabezados():
    """Test escribir tabla sin encabezados"""
    m = load_module('LibreriaTerminal.py', 'terminal')
    
    datos = [
        ["X", "Y"],
        ["10", "20"]
    ]
    
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        m.escribir_tabla(datos)
    
    salida = buffer.getvalue()
    assert "X" in salida
    assert "10" in salida


def test_escribir_tabla_vacia():
    """Test escribir tabla vacía"""
    m = load_module('LibreriaTerminal.py', 'terminal')
    
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        m.escribir_tabla([])
    
    salida = buffer.getvalue()
    assert "sin datos" in salida


def test_ejecutar_comando_con_error():
    """Test ejecutar comando que genera error"""
    m = load_module('LibreriaTerminal.py', 'terminal')
    
    # Comando que no existe
    resultado = m.ejecutar_y_capturar('comando_que_no_existe_12345')
    assert resultado['codigo'] != 0


def test_ejecutar_y_graficar_salida():
    """Test ejecutar comando y graficar salida"""
    m = load_module('LibreriaTerminal.py', 'terminal')
    
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        resultado = m.ejecutar_y_graficar_salida('echo "test output"')
    
    salida = buffer.getvalue()
    assert "Ejecutando:" in salida
    assert "SALIDA" in salida or "test output" in salida


# Ejecutar todas las pruebas
if __name__ == "__main__":
    test_ejecutar_comando_capturar()
    print("✓ test_ejecutar_comando_capturar")
    
    test_obtener_sistema_operativo()
    print("✓ test_obtener_sistema_operativo")
    
    test_obtener_informacion_sistema()
    print("✓ test_obtener_informacion_sistema")
    
    test_escribir_terminal()
    print("✓ test_escribir_terminal")
    
    test_escribir_linea()
    print("✓ test_escribir_linea")
    
    test_escribir_separador()
    print("✓ test_escribir_separador")
    
    test_escribir_titulo()
    print("✓ test_escribir_titulo")
    
    test_escribir_tabla()
    print("✓ test_escribir_tabla")
    
    test_escribir_tabla_sin_encabezados()
    print("✓ test_escribir_tabla_sin_encabezados")
    
    test_escribir_tabla_vacia()
    print("✓ test_escribir_tabla_vacia")
    
    test_ejecutar_comando_con_error()
    print("✓ test_ejecutar_comando_con_error")
    
    test_ejecutar_y_graficar_salida()
    print("✓ test_ejecutar_y_graficar_salida")
    
    print("\n¡Todas las pruebas pasaron!")
