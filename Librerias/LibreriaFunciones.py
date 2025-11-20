"""
LibreriaFunciones.py
Funciones estadísticas y utilidades:
 - mean, variance, std, dot
 - min_max_normalize, z_score
 - mse, mae, rmse, r2
 - regresion_lineal (simple OLS), predict_linear
"""

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

def std(xs):
    return variance(xs) ** 0.5

def dot(a,b):
    if len(a) != len(b):
        raise ValueError("dot: vectores distintas longitudes")
    s = 0.0
    for x,y in zip(a,b):
        s += x*y
    return s

def min_max_normalize(xs):
    if not xs:
        return []
    mn = min(xs); mx = max(xs)
    if mx == mn:
        return [0.5 for _ in xs]
    return [(x - mn) / (mx - mn) for x in xs]

def z_score(xs):
    if not xs:
        return []
    m = mean(xs)
    sd = std(xs)
    if sd == 0:
        return [0.0 for _ in xs]
    return [(x - m) / sd for x in xs]

# --------- metrics ----------
def mse(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("mse: longitudes difieren")
    n = len(y_true)
    return sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / n

def mae(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("mae: longitudes difieren")
    n = len(y_true)
    return sum(abs(yt - yp) for yt, yp in zip(y_true, y_pred)) / n

def rmse(y_true, y_pred):
    return mse(y_true, y_pred) ** 0.5

def r2(y_true, y_pred):
    m = mean(y_true)
    ss_res = sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred))
    ss_tot = sum((yt - m) ** 2 for yt in y_true)
    return 1.0 - ss_res / ss_tot if ss_tot != 0 else 0.0

# --------- regresion lineal simple ----------
def regresion_lineal(x, y):
    if not x or not y or len(x) != len(y):
        raise ValueError("regresion_lineal: listas vacías o distintas longitudes")
    n = len(x)
    mx = mean(x)
    my = mean(y)
    numer = sum((x[i] - mx) * (y[i] - my) for i in range(n))
    denom = sum((x[i] - mx) ** 2 for i in range(n))
    if denom == 0:
        raise ValueError("regresion_lineal: varianza x = 0")
    m = numer / denom
    b = my - m * mx
    return (m, b)

def predict_linear(X, m, b):
    if isinstance(X, list) and (not X or not isinstance(X[0], list)):
        # 1D list
        return [m * xi + b for xi in X]
    elif isinstance(X, list):
        # list of lists -> apply on first feature only
        return [m * xi[0] + b for xi in X]
    else:
        return m * X + b

if __name__ == "__main__":
    x=[1,2,3,4]; y=[2,4,5,4]
    m,b = regresion_lineal(x,y)
    print("m,b",m,b)
    print("mse", mse(y, predict_linear(x,m,b)))