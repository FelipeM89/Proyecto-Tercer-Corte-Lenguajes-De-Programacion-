from antlr4 import *
from Visitor.LenguajeDominioEspecificoVisitor import LenguajeDominioEspecificoVisitor
from Visitor.LenguajeDominioEspecificoParser import LenguajeDominioEspecificoParser

from Librerias.LibreriaAritmentica import *
from Librerias.LibreriasMatrices import *
from Librerias.LibreriaArchivoGestion import *
from Librerias.LibreriaFunciones import *
from Librerias.LibreriaGraficas import *
from Librerias.LibreriaGraficasTerminal import *
from Librerias.LibreriaRegresionLineal import *
from Librerias.LibreriaPerceptronMC import *
from Librerias.LibreriaTablas import *


class Visitor(LenguajeDominioEspecificoVisitor):

    def __init__(self):
        self.memoria = {}                 # Variables normales
        self.regresion = None             # Modelo de regresión lineal
        self.mlp = None                   # Perceptrón multicapa
        self.loss_history = []            # Historial de pérdida del MLP


    # ----------------------------
    #      ASIGNACIONES
    # ----------------------------
    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        self.memoria[nombre] = valor
        return valor


    # ----------------------------
    #         EXPRESIONES
    # ----------------------------
    def visitExpresionNumero(self, ctx):
        return float(ctx.NUMBER().getText())

    def visitExpresionVariable(self, ctx):
        nombre = ctx.ID().getText()
        return self.memoria.get(nombre, None)

    def visitExpresionString(self, ctx):
        return ctx.STRING().getText().strip('"').strip("'")

    def visitOperacionSumaResta(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        op = ctx.getChild(1).getText()
        return suma(izq, der) if op == "+" else resta(izq, der)

    def visitOperacionMultDiv(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        op = ctx.getChild(1).getText()

        if op == "*":
            return multiplicacion(izq, der)
        elif op == "/":
            return division(izq, der)
        elif op == "%":
            return modulo(izq, der)


    def visitExpresionParentesis(self, ctx):
        return self.visit(ctx.expresion())

    def visitExpresionLista(self, ctx):
        return [self.visit(e) for e in ctx.lista().expresion()]

    def visitExpresionMatriz(self, ctx):
        return self.visit(ctx.matriz())


    # ----------------------------
    #         MATRICES
    # ----------------------------
    def visitMatrizMultiFila(self, ctx):
        filas = []
        for f in ctx.fila():
            fila = [self.visit(e) for e in f.expresion()]
            filas.append(fila)
        return filas

    def visitMatrizUnidimensional(self, ctx):
        return [self.visit(e) for e in ctx.expresion()]
    def visitOperacionMatrizExpr(self, ctx):
        oper = ctx.operacion.text
        params = [self.visit(p) for p in ctx.parametrosMatriz().expresion()]

        if oper == "suma":
            return sumar_matrices(params[0], params[1])
        elif oper == "resta":
            return restar_matrices(params[0], params[1])
        elif oper == "multiplicar":
            return multiplicar_matrices(params[0], params[1])
        elif oper == "transpuesta":
            return transpuesta(params[0])
        elif oper == "determinante":
            return determinante(params[0])
        elif oper == "inversa":
            return inversa(params[0])




    # ----------------------------
    #       REGRESIÓN LINEAL
    # ----------------------------
    def visitCrearRegresion(self, ctx):
        self.regresion = regresion_lineal_model()
        return self.regresion

    def visitEntrenarRegresion(self, ctx):
        X = self.visit(ctx.x)
        y = self.visit(ctx.y)
        self.regresion.fit(X, y)
        return None

    def visitPredecirRegresion(self, ctx):
        nombre = ctx.ID().getText()
        x = self.visit(ctx.expresion())
        pred = self.regresion.predict(x)
        self.memoria[nombre] = pred
        return pred

    def visitObtenerMetricaRegresion(self, ctx):
        nombre = ctx.ID().getText()
        met = ctx.metrica.text

        if met == "mse":
            val = self.regresion.mse()
        elif met == "mae":
            val = self.regresion.mae()
        elif met == "r2":
            val = self.regresion.r2()
        elif met == "rmse":
            val = self.regresion.rmse()

        self.memoria[nombre] = val
        return val

    def visitGraficarRegresion(self, ctx):
        parametros = {}
        if ctx.parametrosPlot():
            for p in ctx.parametrosPlot().parametroPlot():
                key = p.getChild(0).getText()
                val = p.getChild(2).getText()
                parametros[key] = val

        graficar_regresion_terminal(
            self.regresion.X,
            self.regresion.y,
            self.regresion.m,
            self.regresion.b
        )
        return None


    # ----------------------------
    #      PERCEPTRÓN MULTICAPA
    # ----------------------------
    def visitCrearMLP(self, ctx):
        params = {}
        for p in ctx.parametrosMLP().parametroMLP():
            key = p.getChild(0).getText()
            value = self.visit(p.getChild(2))
            params[key] = value

        self.mlp = PerceptronMulticapa(**params)
        return self.mlp

    def visitEntrenarMLP(self, ctx):
        X = self.visit(ctx.x)
        y = self.visit(ctx.y)

        # parámetros opcionales
        epochs = 100
        batch = 1
        verbose = False

        if ctx.parametrosEntrenamiento():
            for p in ctx.parametrosEntrenamiento().parametroEntrenamiento():
                key = p.getChild(0).getText()
                value = float(p.getChild(2).getText())
                if key == "epochs": epochs = value
                elif key == "batch_size": batch = value
                elif key == "verbose": verbose = (p.getChild(2).getText() == "True")

        self.loss_history = self.mlp.fit(X, y, epochs, batch, verbose)
        return None

    def visitPredecirMLP(self, ctx):
        nombre = ctx.ID().getText()
        x = self.visit(ctx.expresion())
        pred = self.mlp.predict(x)
        self.memoria[nombre] = pred
        return pred

    def visitEvaluarMLP(self, ctx):
        nombre = ctx.ID().getText()
        X = self.visit(ctx.x)
        y = self.visit(ctx.y)
        score = self.mlp.score(X, y)
        self.memoria[nombre] = score
        return score

    def visitGraficarPerdidaMLP(self, ctx):
        graficar_entrenamiento(self.loss_history)
        return None


    # ----------------------------
    #          PRINT
    # ----------------------------
    def visitImpresion(self, ctx):
        if ctx.STRING():
            base = ctx.STRING().getText().strip('"').strip("'")
            if ctx.expresion():
                values = [self.visit(e) for e in ctx.expresion()]
                print(base, *values)
            else:
                print(base)
        else:
            print(self.visit(ctx.expresion()))
        return None
    # Simbolos de los tokens
    def mostrar_tabla_simbolos(self):
        
        print("\n tabla")
        
        if not self.memoria:
            print("  (vacía)")
        else:
            for i, (nombre, valor) in enumerate(self.memoria.items(), 1):
                tipo = type(valor).__name__
                
                # Si es una matriz (lista de listas), muestra dimensiones
                if isinstance(valor, list):
                    if valor and isinstance(valor[0], list):
                        filas = len(valor)
                        cols = len(valor[0]) if valor else 0
                        print(f"  [{i}] {nombre}: matriz {filas}x{cols}")
                    else:
                        print(f"  [{i}] {nombre}: lista de {len(valor)} elementos")
                else:
                    print(f"  [{i}] {nombre}: {tipo} = {valor}")
