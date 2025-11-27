
from Librerias.LibreriaRegresionLineal import regresion_lineal_model

try:
    modelo = regresion_lineal_model()
    modelo.fit([[1],[2],[3],[4]],[2,4,6,8])
    pred = modelo.predict([5])
    print(f"Prediction for [5]: {pred}")
except Exception as e:
    print(f"Caught expected error: {e}")

