"""
mylib_aritmetica.py
Operaciones aritméticas y funciones matemáticas implementadas en Python puro,
sin dependencias externas.

Incluye:
- operaciones básicas (suma, resta...)
- factorial, potencia (x^y usando exp/ln)
- exp, ln (implementadas con series / Newton)
- seno, coseno, tan (series de Taylor con reducción de rango)
- sqrt (Newton)
- utilidades numéricas

Nota: estas implementaciones priorizan claridad y robustez sobre rendimiento.
"""

# -----------------------
# Utilidades básicas
# -----------------------
def _is_close(a, b, tol=1e-9):
    return abs(a - b) <= tol

def abs_val(x):
    return x if x >= 0 else -x

def factorial(n):
    """Factorial entero no negativo."""
    if n < 0:
        raise ValueError("factorial: n debe ser entero no negativo")
    n = int(n)
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def floor(x):
    """Versión simple de floor para floats (sin math)."""
    xi = int(x)
    if x < 0 and x != xi:
        return xi - 1
    return xi

def ceil(x):
    xi = int(x)
    if x > 0 and x != xi:
        return xi + 1
    return xi

# -----------------------
# Potencia, exp, ln, sqrt
# -----------------------
def _exp_series(x, terms=60):
    """Exponencial usando serie de Taylor (suma hasta convergencia)."""
    # reduce x para evitar overflow de la serie: exp(a+b) = exp(a)*exp(b)
    # pero aquí aplicamos directamente y controlamos término pequeño.
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
    """exp(x) implementado con series y reducción por partes para x grande/negativo."""
    # Manejo de negativos
    if x == 0:
        return 1.0
    # Reduce el valor de x usando la propiedad exp(k + r) = exp(k)*exp(r), con k entero
    # Elegimos k = floor(x) para evitar x grande en la serie
    k = floor(x)
    r = x - k
    # exp(x) = exp(k) * exp(r) where exp(k) = e^k = (e^1)^k, approximamos e ~ exp(1)
    # Calculamos exp(r) con serie
    exp_r = _exp_series(r, terms=200)
    # calcular exp(k) por multiplicación repetida (k puede ser negativo)
    if k >= 0:
        exp_k = 1.0
        e1 = _exp_series(1.0, terms=80)
        for _ in range(k):
            exp_k *= e1
    else:
        # para k negativo: exp(k) = 1/exp(-k)
        exp_k_pos = 1.0
        e1 = _exp_series(1.0, terms=80)
        for _ in range(-k):
            exp_k_pos *= e1
        exp_k = 1.0 / exp_k_pos
    return exp_k * exp_r

def sqrt(x, tol=1e-12, max_iter=200):
    """Raíz cuadrada por método de Newton (x >= 0)."""
    if x < 0:
        raise ValueError("sqrt: argumento negativo")
    if x == 0:
        return 0.0
    # initial guess
    guess = x if x < 1 else x / 2.0
    for _ in range(max_iter):
        newg = 0.5 * (guess + x / guess)
        if abs_val(newg - guess) < tol:
            return newg
        guess = newg
    return guess

def ln(x, tol=1e-12, max_iter=100):
    """Log natural usando Newton sobre f(t)=exp(t)-x -> t_{n+1} = t - (exp(t)-x)/exp(t) = t + ln(x) - t approx
    Newton's method: find t such that exp(t) = x.
    """
    if x <= 0:
        raise ValueError("ln: argumento debe ser > 0")
    # initial guess: use log base-approx by reducing x into [0.5, 2)
    # Count how many times divide/multiply by 2 to get near 1
    # Since we don't have log2, do simple scaling
    t = 0.0
    y = x
    while y > 2.0:
        y /= 2.0
        t += 0.6931471805599453  # ln(2) approximate constant
    while y < 0.5:
        y *= 2.0
        t -= 0.6931471805599453
    # refine with Newton: solve exp(z) = x -> z_{n+1} = z_n - (exp(z_n)-x)/exp(z_n) = z_n - 1 + x/exp(z_n)
    # start with z0 = ln(y) approx via series around 1: ln(1+u) ~ u - u^2/2 + u^3/3...
    u = y - 1.0
    z = u
    # series few terms for starting point
    term = u
    for n in range(2, 10):
        term *= -u
        z += term / n
    z += t
    for _ in range(max_iter):
        e_z = _exp_series(z, terms=200)
        diff = e_z - x
        if abs_val(diff) < tol:
            return z
        z = z - diff / e_z
    return z

def powf(x, y):
    """Potencia real x^y sin usar math; maneja casos:
       - x > 0: x^y = exp(y * ln(x))
       - x == 0: 0^y = 0 (y>0)
       - x < 0 and y entero: usual
    """
    # caso entero rápido para rendimiento
    try:
        yi = int(y)
        if _is_close(y, yi):
            # entero
            yi = int(yi)
            if yi >= 0:
                res = 1.0
                for _ in range(yi):
                    res *= x
                return res
            else:
                # negativo
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
        else:
            raise ValueError("0^y con y <= 0 indefinido")
    else:
        # x < 0 and y no entero -> complejo (no soportado)
        raise ValueError("potencia: base negativa con exponente no entero no soportado")

# -----------------------
# Trigonometría (Taylor + reducción de rango)
# -----------------------
PI = 3.141592653589793
TWOPI = 2.0 * PI
HALFPI = PI / 2.0

def _normalize_angle(x):
    # reduce a [-pi, pi]
    # hace módulo 2pi
    k = int(x / TWOPI)
    r = x - k * TWOPI
    if r > PI:
        r -= TWOPI
    if r < -PI:
        r += TWOPI
    return r

def sin(x):
    """Seno con serie de Taylor con reducción de rango."""
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
        if n > 50:
            break
    return s

def cos(x):
    x = _normalize_angle(x)
    term = 1.0
    s = 1.0
    n = 1
    while True:
        term *= -1 * x * x / ((2*n-1) * (2*n))
        s += term
        if abs_val(term) < 1e-15:
            break
        n += 1
        if n > 50:
            break
    return s

def tan(x):
    c = cos(x)
    if _is_close(c, 0.0):
        raise ValueError("tan: cos(x) cerca de 0 -> indefinido")
    return sin(x) / c

# -----------------------
# Operaciones aritméticas básicas
# -----------------------
def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplicacion(a, b): return a * b
def division(a, b):
    if b == 0:
        raise ZeroDivisionError("division: division por cero")
    return a / b
def modulo(a, b):
    if b == 0:
        raise ZeroDivisionError("modulo: division por cero")
    return a - int(a / b) * b

# -----------------------
# Pruebas rápidas
# -----------------------
if __name__ == "__main__":
    print("Pruebas mylib_aritmetica:")
    print("exp(1) ~", exp(1.0))
    print("ln(e) ~", ln(_exp_series(1.0)))
    print("sqrt(2) ~", sqrt(2.0))
    print("sin(pi/6) ~", sin(PI/6))
    print("cos(pi/3) ~", cos(PI/3))
    print("powf(2, 10) =", powf(2, 10))
    print("powf(9, 0.5) ~", powf(9, 0.5))