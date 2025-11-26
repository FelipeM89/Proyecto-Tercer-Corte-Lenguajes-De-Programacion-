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
    """Valida que A sea una matriz rectangular válida."""
    if not isinstance(A, list) or len(A) == 0:
        raise ValueError("Matriz invalida: debe ser una lista no vacia")
    if not isinstance(A[0], list) or len(A[0]) == 0:
        raise ValueError("Matriz invalida: cada fila debe ser una lista no vacia")
    cols = len(A[0])
    for i, row in enumerate(A):
        if not isinstance(row, list) or len(row) != cols:
            raise ValueError(f"Matriz no rectangular en fila {i}")

def shape(A):
    _check_matrix(A)
    return (len(A), len(A[0]))

def zeros(r, c):
    """Crea una matriz de ceros de tamaño r x c."""
    if r <= 0 or c <= 0:
        raise ValueError("Las dimensiones deben ser positivas")
    return [[0.0 for _ in range(c)] for _ in range(r)]


def identity(n):
    """Devuelve la matriz identidad de tamaño n x n."""
    if n <= 0:
        raise ValueError("El tamaño debe ser positivo")
    I = zeros(n, n)
    for i in range(n):
        I[i][i] = 1.0
    return I


def sumar_matrices(A, B):
    """Suma dos matrices A y B elemento a elemento."""
    _check_matrix(A)
    _check_matrix(B)
    rA, cA = shape(A)
    rB, cB = shape(B)
    if rA != rB or cA != cB:
        raise ValueError(f"Dimensiones incompatibles: ({rA}x{cA}) + ({rB}x{cB})")
    return [[A[i][j] + B[i][j] for j in range(cA)] for i in range(rA)]

def restar_matrices(A, B):
    """Resta la matriz B de A elemento a elemento."""
    _check_matrix(A)
    _check_matrix(B)
    rA, cA = shape(A)
    rB, cB = shape(B)
    if rA != rB or cA != cB:
        raise ValueError(f"Dimensiones incompatibles: ({rA}x{cA}) - ({rB}x{cB})")
    return [[A[i][j] - B[i][j] for j in range(cA)] for i in range(rA)]

def multiplicar_matrices(A, B):
    """Multiplica dos matrices A y B (producto matricial)."""
    _check_matrix(A)
    _check_matrix(B)
    rA, cA = shape(A)
    rB, cB = shape(B)
    if cA != rB:
        raise ValueError(f"Dimensiones incompatibles: ({rA}x{cA}) * ({rB}x{cB})")
    C = zeros(rA, cB)
    for i in range(rA):
        for j in range(cB):
            s = 0.0
            for k in range(cA):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    return C


def transpuesta(A):
    """Devuelve la transpuesta de la matriz A."""
    _check_matrix(A)
    r, c = shape(A)
    return [[A[i][j] for i in range(r)] for j in range(c)]

def inversa(A, tol=1e-12):
    """
    Calcula la inversa de la matriz A usando el método de Gauss-Jordan.
    Lanza ValueError si la matriz es singular o no cuadrada.
    """
    _check_matrix(A)
    n, m = shape(A)
    if n != m:
        raise ValueError("La inversa solo está definida para matrices cuadradas")
    
    # Crear matriz aumentada [A | I]
    AM = [A[i][:] + identity(n)[i] for i in range(n)]
    
    for col in range(n):
        # Buscar pivote con pivoteo parcial
        pivot = None
        max_val = tol
        for r in range(col, n):
            if abs(AM[r][col]) > max_val:
                max_val = abs(AM[r][col])
                pivot = r
        
        if pivot is None:
            raise ValueError("Matriz singular: no tiene inversa")
        
        # Intercambiar filas si es necesario
        if pivot != col:
            AM[col], AM[pivot] = AM[pivot], AM[col]
        
        # Normalizar fila pivote
        piv = AM[col][col]
        AM[col] = [v / piv for v in AM[col]]
        
        # Eliminar en otras filas
        for r in range(n):
            if r != col:
                factor = AM[r][col]
                if factor != 0:
                    AM[r] = [AM[r][c] - factor * AM[col][c] for c in range(2 * n)]
    
    # Extraer la inversa (parte derecha de la matriz aumentada)
    return [row[n:] for row in AM]



def _minor(A,i,j):
    return [row[:j] + row[j+1:] for k,row in enumerate(A) if k != i]

def determinante(A):
    """ Calcula el determinante de la matriz A de forma recursiva. Lanza ValueError si la matriz no es cuadrada."""
    _check_matrix(A)
    r,c = shape(A)
    if r != c:
        raise ValueError("Determinante solo para cuadradas")
    n = r
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    det = 0.0
    for j in range(n):
        det += ((-1)**j) * A[0][j] * determinante(_minor(A,0,j))
    return det


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
    
    
    print("=== Demostración de Operaciones con Matrices ===\n")
    
    A = [[1, 2], 
         [3, 4]]
    
    B = [[5, 6], 
         [7, 8]]
    
    print("Matriz A:")
    for fila in A:
        print(f"  {fila}")
    
    print("\nMatriz B:")
    for fila in B:
        print(f"  {fila}")
    
    print("\nA + B:")
    for fila in sumar_matrices(A, B):
        print(f"  {fila}")
    
    print("\nA - B:")
    for fila in restar_matrices(A, B):
        print(f"  {fila}")
    
    print("\nA * B:")
    for fila in multiplicar_matrices(A, B):
        print(f"  {fila}")
    
    print("\nTranspuesta de A:")
    for fila in transpuesta(A):
        print(f"  {fila}")
    
    print("\nInversa de A:")
    for fila in inversa(A):
        print(f"  {[round(x, 4) for x in fila]}")
    
    print("\nVerificación A * A⁻¹ = I:")
    resultado = multiplicar_matrices(A, inversa(A))
    for fila in resultado:
        print(f"  {[round(x, 4) for x in fila]}")