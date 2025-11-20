"""
LibreriaAritmentica.py
Funciones numéricas básicas implementadas sin usar librerías externas.
Incluye: abs_val, factorial, exp, ln, powf, sqrt, sin, cos, tan,
operaciones aritméticas básicas y un LCG sencillo para números pseudoaleatorios.
"""

# ---------- utilidades ----------
def abs_val(x):
    return x if x >= 0 else -x

def _is_close(a,b,tol=1e-12):
    return abs_val(a-b) <= tol

def factorial(n):
    n = int(n)
    if n < 0:
        raise ValueError("factorial: n debe ser >= 0")
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

# ---------- series y exp/ln ----------
def _exp_series(x, terms=80):
    term = 1.0
    s = 1.0
    n = 1
    while n < terms:
        term *= x / n
        s += term
        if abs_val(term) < 1e-15:
            break
        n += 1
    return s

def exp(x):
    # manejo simple de enteros y fraccion
    if x == 0:
        return 1.0
    # reduce usando k = int(x)
    k = int(x)
    r = x - k
    e1 = _exp_series(1.0, terms=80)
    # exp(k) ~ e1^k
    exp_k = 1.0
    if k > 0:
        for _ in range(k):
            exp_k *= e1
    elif k < 0:
        for _ in range(-k):
            exp_k /= e1
    return exp_k * _exp_series(r, terms=80)

def ln(x, tol=1e-12, max_iter=200):
    if x <= 0:
        raise ValueError("ln: argumento debe ser > 0")
    # reduce x into (0.5, 2]
    t = 0.0
    y = x
    while y > 2.0:
        y /= 2.0
        t += 0.6931471805599453
    while y < 0.5:
        y *= 2.0
        t -= 0.6931471805599453
    # initial approx by series ln(1+u)
    u = y - 1.0
    z = u
    term = u
    for n in range(2, 12):
        term *= -u
        z += term / n
    z += t
    for _ in range(max_iter):
        e_z = _exp_series(z, terms=100)
        diff = e_z - x
        if abs_val(diff) < tol:
            return z
        z = z - diff / e_z
    return z

def sqrt(x, tol=1e-12, max_iter=200):
    if x < 0:
        raise ValueError("sqrt: argumento negativo")
    if x == 0:
        return 0.0
    guess = x if x < 1 else x/2.0
    for _ in range(max_iter):
        newg = 0.5 * (guess + x/guess)
        if abs_val(newg - guess) < tol:
            return newg
        guess = newg
    return guess

def powf(x, y):
    # maneja enteros rápidamente
    try:
        yi = int(y)
        if _is_close(y, yi):
            yi = int(yi)
            if yi >= 0:
                res = 1.0
                for _ in range(yi):
                    res *= x
                return res
            else:
                pos = -yi
                res = 1.0
                for _ in range(pos):
                    res *= x
                if res == 0:
                    raise ZeroDivisionError("0 ** negative")
                return 1.0 / res
    except Exception:
        pass
    if x > 0:
        return exp(y * ln(x))
    elif x == 0.0:
        if y > 0:
            return 0.0
        raise ValueError("0^y con y <=0 indefinido")
    else:
        raise ValueError("base negativa con exponente no entero no soportado")

# ---------- trigonometría (reducción + Taylor) ----------
PI = 3.141592653589793
TWOPI = 2.0 * PI

def _normalize_angle(x):
    k = int(x / TWOPI)
    r = x - k * TWOPI
    if r > PI:
        r -= TWOPI
    if r < -PI:
        r += TWOPI
    return r

def sin(x):
    x = _normalize_angle(x)
    term = x
    s = x
    n = 1
    while True:
        term *= -1 * x * x / ((2*n) * (2*n+1))
        s += term
        if abs_val(term) < 1e-15:
            break
        n += 1
        if n > 60:
            break
    return s

def cos(x):
    x = _normalize_angle(x)
    term = 1.0
    s = 1.0
    n = 1
    while True:
        term *= -1 * x * x / ((2*n-1)*(2*n))
        s += term
        if abs_val(term) < 1e-15:
            break
        n += 1
        if n > 60:
            break
    return s

def tan(x):
    c = cos(x)
    if _is_close(c, 0.0):
        raise ValueError("tan: cos(x) cerca de 0")
    return sin(x) / c

# ---------- operaciones basicas ----------
def suma(a,b): return a + b
def resta(a,b): return a - b
def multiplicacion(a,b): return a * b
def division(a,b):
    if b == 0:
        raise ZeroDivisionError("division por cero")
    return a / b
def modulo(a,b):
    if b == 0:
        raise ZeroDivisionError("modulo por cero")
    return a - int(a / b) * b

# ---------- LCG simple (semilla manejable) ----------
class LCG:
    def __init__(self, seed=123456):
        self.state = int(seed) & 0x7fffffff
    def rand(self):
        self.state = (1103515245 * self.state + 12345) & 0x7fffffff
        return self.state / 2147483648.0
    def randint(self, a, b):
        return a + int(self.rand() * (b - a + 1))

# ---------- pruebas ----------
if __name__ == "__main__":
    print("exp(1)~", exp(1))
    print("ln(e)~", ln(_exp_series(1)))
    print("sqrt(2)~", sqrt(2))
    print("sin(pi/6)~", sin(PI/6))