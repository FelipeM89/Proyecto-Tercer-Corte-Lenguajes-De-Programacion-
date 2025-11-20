"""
LibreriasMatrices.py
Operaciones con matrices 2D sin dependencias.
Funciones:
 - _check_matrix, shape, zeros, identity
 - sumar_matrices, restar_matrices, multiplicar_matrices
 - transpuesta, determinante (recursivo), inversa (Gauss-Jordan)
 - escalar_matriz, multiplicar_matriz_vector
"""

def _check_matrix(A):
    if not isinstance(A, list) or len(A) == 0:
        raise ValueError("Matriz inválida")
    cols = len(A[0])
    for row in A:
        if not isinstance(row, list) or len(row) != cols:
            raise ValueError("Matriz no rectangular")

def shape(A):
    _check_matrix(A)
    return (len(A), len(A[0]))

def zeros(r,c):
    return [[0.0 for _ in range(c)] for _ in range(r)]

def identity(n):
    I = zeros(n,n)
    for i in range(n):
        I[i][i] = 1.0
    return I

def sumar_matrices(A,B):
    _check_matrix(A); _check_matrix(B)
    rA,cA = shape(A); rB,cB = shape(B)
    if rA != rB or cA != cB:
        raise ValueError("Dimensiones incompatibles")
    return [[A[i][j] + B[i][j] for j in range(cA)] for i in range(rA)]

def restar_matrices(A,B):
    _check_matrix(A); _check_matrix(B)
    rA,cA = shape(A); rB,cB = shape(B)
    if rA != rB or cA != cB:
        raise ValueError("Dimensiones incompatibles")
    return [[A[i][j] - B[i][j] for j in range(cA)] for i in range(rA)]

def multiplicar_matrices(A,B):
    _check_matrix(A); _check_matrix(B)
    rA,cA = shape(A); rB,cB = shape(B)
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
    r,c = shape(A)
    return [[A[i][j] for i in range(r)] for j in range(c)]

# determinante recursivo (no optimizado)
def _minor(A,i,j):
    return [row[:j] + row[j+1:] for k,row in enumerate(A) if k != i]

def determinante(A):
    _check_matrix(A)
    r,c = shape(A)
    if r != c:
        raise ValueError("Determinante sólo para cuadradas")
    n = r
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    det = 0.0
    for j in range(n):
        det += ((-1)**j) * A[0][j] * determinante(_minor(A,0,j))
    return det

# inversa por Gauss-Jordan
def inversa(A, tol=1e-12):
    _check_matrix(A)
    n,m = shape(A)
    if n != m:
        raise ValueError("Inversa sólo para cuadradas")
    AM = [row[:] + identity(n)[i] for i,row in enumerate([r[:] for r in A])]
    for col in range(n):
        pivot = None
        for r in range(col, n):
            if abs(AM[r][col]) > tol:
                pivot = r
                break
        if pivot is None:
            raise ValueError("Matriz singular")
        if pivot != col:
            AM[col], AM[pivot] = AM[pivot], AM[col]
        piv = AM[col][col]
        AM[col] = [v / piv for v in AM[col]]
        for r in range(n):
            if r != col:
                factor = AM[r][col]
                if factor != 0:
                    AM[r] = [AM[r][c] - factor * AM[col][c] for c in range(2*n)]
    inv = [row[n:] for row in AM]
    return inv

def escalar_matriz(A,k):
    _check_matrix(A)
    r,c = shape(A)
    return [[A[i][j]*k for j in range(c)] for i in range(r)]

def multiplicar_matriz_vector(A,v):
    _check_matrix(A)
    r,c = shape(A)
    if len(v) != c:
        raise ValueError("Dimensiones incompatibles")
    res = [0.0 for _ in range(r)]
    for i in range(r):
        s = 0.0
        for j in range(c):
            s += A[i][j] * v[j]
        res[i] = s
    return res

if __name__ == "__main__":
    A = [[1,2],[3,4]]
    B = [[5,6],[7,8]]
    print("A+B", sumar_matrices(A,B))
    print("A*B", multiplicar_matrices(A,B))
    print("inv(A)", inversa(A))