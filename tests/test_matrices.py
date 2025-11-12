import os
import importlib.util


def load_module(fname, modname):
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Librerias'))
    path = os.path.join(base, fname)
    spec = importlib.util.spec_from_file_location(modname, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_sum_and_multiply_and_transpose():
    m = load_module('LibreriasMatrices.py', 'mat')
    A = [[1.0, 2.0], [3.0, 4.0]]
    B = [[5.0, 6.0], [7.0, 8.0]]
    C = m.sumar_matrices(A, B)
    assert C == [[6.0, 8.0], [10.0, 12.0]]
    D = m.multiplicar_matrices(A, B)
    assert D == [[19.0, 22.0], [43.0, 50.0]]
    assert m.transpuesta(A) == [[1.0, 3.0], [2.0, 4.0]]


def test_determinant_and_inverse():
    m = load_module('LibreriasMatrices.py', 'mat')
    A = [[1.0, 2.0], [3.0, 4.0]]
    assert abs(m.determinante(A) - (-2.0)) < 1e-12
    invA = m.inversa(A)
    # invA should be approximately [[-2,1],[1.5,-0.5]]
    assert abs(invA[0][0] + 2.0) < 1e-9
    assert abs(invA[0][1] - 1.0) < 1e-9
