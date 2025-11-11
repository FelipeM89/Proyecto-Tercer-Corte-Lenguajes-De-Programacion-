"""
mylib_matrices.py
Operaciones con matrices 2D en Python puro:
- creación, suma, resta, multiplicación
- transpuesta, identidad
- inversa por Gauss-Jordan
- determinante (recursivo, para uso en matrices pequeñas)
"""

# -----------------------
# Utilidades internas
# -----------------------
def _check_matrix(A):
    if not A or not isinstance(A, list):
        raise ValueError("Matriz inválida")
    cols = len(A[0])
    for row in A:
        if not isinstance(row, list) or len(row) != cols:
            raise ValueError("Matriz no rectangular")

def shape(A):
    _check_matrix(A)
    return (len(A), len(A[0]))

def zeros(rows, cols):
    return [[0.0 for _ in range(cols)] for _ in range(rows)]

def identity(n):
    I = zeros(n, n)
    for i in range(n):
        I[i][i] = 1.0
    return I

# -----------------------
# Operaciones básicas
# -----------------------
def sumar_matrices(A, B):
    _check_matrix(A); _check_matrix(B)
    rA, cA = shape(A); rB, cB = shape(B)
    if rA != rB or cA != cB:
        raise ValueError("Dimensiones incompatibles para suma")
    return [[A[i][j] + B[i][j] for j in range(cA)] for i in range(rA)]

def restar_matrices(A, B):
    _check_matrix(A); _check_matrix(B)
    rA, cA = shape(A); rB, cB = shape(B)
    if rA != rB or cA != cB:
        raise ValueError("Dimensiones incompatibles para resta")
    return [[A[i][j] - B[i][j] for j in range(cA)] for i in range(rA)]

def multiplicar_matrices(A, B):
    _check_matrix(A); _check_matrix(B)
    rA, cA = shape(A); rB, cB = shape(B)
    if cA != rB:
        raise ValueError("Dimensiones incompatibles para multiplicación")
    C = zeros(rA, cB)
    for i in range(rA):
        for j in range(cB):
            s = 0.0
            for k in range(cA):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    return C

def transpuesta(A):
    _check_matrix(A)
    r, c = shape(A)
    return [[A[i][j] for i in range(r)] for j in range(c)]

# -----------------------
# Determinante (recursivo, para matrices pequeñas)
# -----------------------
def _minor(A, i, j):
    # devuelve la matriz que resulta de eliminar fila i y columna j
    return [row[:j] + row[j+1:] for k,row in enumerate(A) if k != i]

def determinante(A):
    _check_matrix(A)
    r, c = shape(A)
    if r != c:
        raise ValueError("Determinante sólo definida para matrices cuadradas")
    n = r
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    det = 0.0
    for j in range(n):
        det += ((-1)**j) * A[0][j] * determinante(_minor(A, 0, j))
    return det

# -----------------------
# Inversa por Gauss-Jordan
# -----------------------
def inversa(A, tol=1e-12):
    _check_matrix(A)
    n, m = shape(A)
    if n != m:
        raise ValueError("Inversa sólo definida para matrices cuadradas")
    # crear matriz aumentada [A | I]
    AM = [row[:] + identity(n)[i] for i, row in enumerate([r[:] for r in A])]
    # Convertir a forma reducida
    for col in range(n):
        # Buscar pivote (fila con valor no cero)
        pivot_row = None
        for r in range(col, n):
            if abs(AM[r][col]) > tol:
                pivot_row = r
                break
        if pivot_row is None:
            raise ValueError("Matriz singular, no tiene inversa")
        # intercambiar si es necesario
        if pivot_row != col:
            AM[col], AM[pivot_row] = AM[pivot_row], AM[col]
        # Normalizar fila del pivote
        pivot = AM[col][col]
        AM[col] = [val / pivot for val in AM[col]]
        # Eliminar otras filas
        for r in range(n):
            if r != col:
                factor = AM[r][col]
                if factor != 0:
                    AM[r] = [AM[r][c] - factor * AM[col][c] for c in range(2*n)]
    # extraer la mitad derecha como la inversa
    inv = [row[n:] for row in AM]
    return inv

# -----------------------
# Multiplicar matriz por escalar y vector
# -----------------------
def escalar_matriz(A, k):
    _check_matrix(A)
    r, c = shape(A)
    return [[A[i][j] * k for j in range(c)] for i in range(r)]

def multiplicar_matriz_vector(A, v):
    _check_matrix(A)
    r, c = shape(A)
    if len(v) != c:
        raise ValueError("Dimensiones incompatibles para multiplicar matriz por vector")
    res = [0.0 for _ in range(r)]
    for i in range(r):
        s = 0.0
        for j in range(c):
            s += A[i][j] * v[j]
        res[i] = s
    return res

# -----------------------
# Pruebas rápidas
# -----------------------
if __name__ == "__main__":
    print("Pruebas mylib_matrices:")
    A = [[1.0, 2.0], [3.0, 4.0]]
    B = [[5.0, 6.0], [7.0, 8.0]]
    print("A+B =", sumar_matrices(A, B))
    print("A*B =", multiplicar_matrices(A, B))
    print("trans(A) =", transpuesta(A))
    print("det(A) =", determinante(A))
    print("inv(A) =", inversa(A))