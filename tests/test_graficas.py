import os
import sys
import importlib.util
import types
import tempfile


def load_module(fname, modname):
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Librerias'))
    path = os.path.join(base, fname)
    # ensure dummy module for 'libs.mylib_archivos' exists so import in file works
    dummy = types.ModuleType('mylib_archivos')
    dummy.escribir_archivo_texto = lambda path, contenido: open(path, 'w', encoding='utf-8').write(contenido) or True
    # insert package-like module
    pkg = types.ModuleType('libs')
    sys.modules['libs'] = pkg
    sys.modules['libs.mylib_archivos'] = dummy
    spec = importlib.util.spec_from_file_location(modname, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_graficas_guardar_puntos():
    m = load_module('LibreriaGraficas.py', 'gr')
    xs = [0,1,2]
    ys = [10,20,30]
    with tempfile.NamedTemporaryFile('w+', delete=False) as tf:
        path = tf.name
    try:
        res = m.guardar_puntos(path, xs, ys)
        assert res is True
        with open(path, 'r', encoding='utf-8') as f:
            txt = f.read()
        assert '0,10' in txt and '2,30' in txt
    finally:
        os.unlink(path)
