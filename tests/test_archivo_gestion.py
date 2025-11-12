import os
import tempfile
import importlib.util


def load_module(fname, modname):
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Librerias'))
    path = os.path.join(base, fname)
    spec = importlib.util.spec_from_file_location(modname, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_write_and_read_text():
    m = load_module('LibreriaArchivoGestion.py', 'arch')
    with tempfile.NamedTemporaryFile('w+', delete=False) as tf:
        path = tf.name
    try:
        assert m.escribir_archivo_texto(path, 'hola\n1,2,3\n') is True
        content = m.leer_archivo_texto(path)
        assert 'hola' in content
    finally:
        os.unlink(path)


def test_guardar_y_cargar_csv():
    m = load_module('LibreriaArchivoGestion.py', 'arch')
    lst = [[1,2,3],[4,5,6]]
    with tempfile.NamedTemporaryFile('w+', delete=False) as tf:
        path = tf.name
    try:
        assert m.guardar_lista_como_csv(path, lst) is True
        loaded = m.cargar_lista_de_csv(path, tipo=int)
        assert loaded == [[1,2,3],[4,5,6]]
    finally:
        os.unlink(path)
