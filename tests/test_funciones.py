import os
import importlib.util


def load_module(fname, modname):
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Librerias'))
    path = os.path.join(base, fname)
    spec = importlib.util.spec_from_file_location(modname, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_mean_variance_and_dot():
    m = load_module('LibreriaFunciones.py', 'funcs')
    xs = [1.0, 2.0, 3.0]
    assert m.mean(xs) == 2.0
    assert abs(m.variance(xs) - (2.0/3.0)) < 1e-9


def test_regression_and_metrics():
    m = load_module('LibreriaFunciones.py', 'funcs')
    x = [1, 2, 3]
    y = [2, 4, 6]
    slope, intercept = m.regresion_lineal(x, y)
    assert abs(slope - 2.0) < 1e-9
    assert abs(intercept - 0.0) < 1e-9
    preds = m.predict_linear(x, slope, intercept)
    assert m.mse(y, preds) == 0.0
    assert m.mae(y, preds) == 0.0


def test_normalizations():
    m = load_module('LibreriaFunciones.py', 'funcs')
    assert m.min_max_normalize([10, 20, 30]) == [0.0, 0.5, 1.0]
    zs = m.z_score([10, 20, 30])
    # zero mean for z-score
    assert abs(sum(zs)) < 1e-12
