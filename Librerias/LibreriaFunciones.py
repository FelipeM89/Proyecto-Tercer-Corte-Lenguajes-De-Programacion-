"""
mylib_funciones.py
Funciones estadísticas y de aprendizaje básicas:
- regresion_lineal (OLS) con salida (m, b)
- metrics: MSE, MAE
- normalizacion: min-max y z-score
- utilidades: mean, variance, dot
"""

# Utilidades
def mean(xs):
    if not xs:
        return 0.0
    return sum(xs) / len(xs)

def variance(xs, ddof=0):
    if not xs:
        return 0.0
    m = mean(xs)
    n = len(xs)
    s = sum((x - m) ** 2 for x in xs)
    return s / (n - ddof) if n - ddof > 0 else 0.0

def dot(a, b):
    if len(a) != len(b):
        raise ValueError("dot: vectores distintas longitudes")
    s = 0.0
    for x, y in zip(a, b):
        s += x * y
    return s

# -----------------------
# Regresion Lineal Simple (y = m * x + b)
# -----------------------
def regresion_lineal(x, y):
    """
    Retorna (m, b) donde m = slope, b = intercept usando mínimos cuadrados ordinarios.
    x, y: listas del mismo tamaño.
    """
    if not x or not y or len(x) != len(y):
        raise ValueError("regresion_lineal: listas vacías o distintas longitudes")
    n = len(x)
    mx = mean(x)
    my = mean(y)
    numer = sum((x[i] - mx) * (y[i] - my) for i in range(n))
    denom = sum((x[i] - mx) ** 2 for i in range(n))
    if denom == 0:
        raise ValueError("regresion_lineal: varianza de x es cero")
    m = numer / denom
    b = my - m * mx
    return (m, b)

def predict_linear(x, m, b):
    return [m * xi + b for xi in x]

# -----------------------
# Métricas
# -----------------------
def mse(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("mse: listas distintas longitudes")
    n = len(y_true)
    return sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / n

def mae(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("mae: listas distintas longitudes")
    n = len(y_true)
    return sum(abs(yt - yp) for yt, yp in zip(y_true, y_pred)) / n

# -----------------------
# Normalizaciones
# -----------------------
def min_max_normalize(xs):
    if not xs:
        return []
    mn = min(xs)
    mx = max(xs)
    if mx == mn:
        return [0.5 for _ in xs]
    return [(x - mn) / (mx - mn) for x in xs]

def z_score(xs):
    if not xs:
        return []
    m = mean(xs)
    var = variance(xs)
    sd = var ** 0.5
    if sd == 0:
        return [0.0 for _ in xs]
    return [(x - m) / sd for x in xs]

if __name__ == "__main__":
    print("Pruebas mylib_funciones:")
    x = [1,2,3,4,5]
    y = [2,4,5,4,5]
    m,b = regresion_lineal(x,y)
    print("m,b =", m, b)
    preds = predict_linear(x,m,b)
    print("preds =", preds)
    print("MSE =", mse(y, preds))
    print("MAE =", mae(y, preds))
    print("minmax =", min_max_normalize([10,20,30]))
    print("zscore =", z_score([10,20,30]))