import os
import importlib.util
import math


def load_module_from_libraries(fname, modname):
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Librerias'))
    path = os.path.join(base, fname)
    spec = importlib.util.spec_from_file_location(modname, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_factorial_and_sqrt():
    m = load_module_from_libraries('LibreriaAritmentica.py', 'arith')
    assert m.factorial(5) == 120
    assert abs(m.sqrt(2.0) - math.sqrt(2.0)) < 1e-8


def test_exp_ln_and_powf():
    m = load_module_from_libraries('LibreriaAritmentica.py', 'arith')
    # exp(1) approx e
    assert abs(m.exp(1.0) - math.e) < 1e-6
    # powf integer exponent
    assert m.powf(2, 10) == 1024


def test_trig():
    m = load_module_from_libraries('LibreriaAritmentica.py', 'arith')
    assert abs(m.sin(m.PI/6) - 0.5) < 1e-6
    assert abs(m.cos(m.PI/3) - 0.5) < 1e-6


def test_division_by_zero():
    m = load_module_from_libraries('LibreriaAritmentica.py', 'arith')
    try:
        m.division(1, 0)
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        pass
