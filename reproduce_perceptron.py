
from Librerias.LibreriaPerceptronMC import PerceptronMulticapa
import traceback

try:
    p = PerceptronMulticapa(layers=[2,3,1], learning_rate=0.1, seed=42)
    p.fit([[0,0],[0,1],[1,0],[1,1]],[0,1,1,0], epochs=100, batch_size=4)
    res = p.predict([1,0])
    print(res)
except Exception:
    traceback.print_exc()
