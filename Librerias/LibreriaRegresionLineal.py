"""
LibreriaRegresionLineal.py
Clase que envuelve regresion_lineal de LibreriaFunciones.
"""

from Librerias.LibreriaFunciones import regresion_lineal, predict_linear, mse, mae, r2

class RegresionLineal:
    def __init__(self):
        self.trained = False
        self.m = None
        self.b = None
        self.x = None
        self.y = None

    def fit(self, x, y):
        m,b = regresion_lineal(x,y)
        self.m = m; self.b = b
        self.trained = True
        self.x = x; self.y = y
        return (m,b)

    def predict(self, X):
        if not self.trained:
            raise RuntimeError("Modelo no entrenado")
        return predict_linear(X, self.m, self.b)

    def mse(self, X=None, Y=None):
        if X is None:
            X = self.x; Y = self.y
            preds = predict_linear(X, self.m, self.b)
            return mse(Y, preds)
        else:
            preds = predict_linear(X, self.m, self.b)
            return mse(Y, preds)

    def mae(self, X=None, Y=None):
        if X is None:
            X = self.x; Y = self.y
            preds = predict_linear(X, self.m, self.b)
            return mae(Y, preds)
        else:
            preds = predict_linear(X, self.m, self.b)
            return mae(Y, preds)

    def r2(self, X=None, Y=None):
        if X is None:
            X = self.x; Y = self.y
            preds = predict_linear(X, self.m, self.b)
            return r2(Y, preds)
        else:
            preds = predict_linear(X, self.m, self.b)
            return r2(Y, preds)