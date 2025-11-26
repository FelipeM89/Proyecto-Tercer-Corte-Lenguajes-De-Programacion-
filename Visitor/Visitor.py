from antlr4 import *
from Visitor.LenguajeDominioEspecificoVisitor import LenguajeDominioEspecificoVisitor
from Visitor.LenguajeDominioEspecificoParser import LenguajeDominioEspecificoParser

from Librerias.LibreriaAritmetica import *
from Librerias.LibreriasMatrices import *
from Librerias.LibreriaArchivoGestion import *
from Librerias.LibreriaFunciones import *
from Librerias.LibreriaGraficas import *
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

    def visitExpresionComparacion(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        op = ctx.getChild(1).getText()
        
        if op == "==":
            return izq == der
        elif op == "!=":
            return izq != der
        elif op == "<":
            return izq < der
        elif op == ">":
            return izq > der
        elif op == "<=":
            return izq <= der
        elif op == ">=":
            return izq >= der

    def visitOperacionSumaResta(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        op = ctx.getChild(1).getText()
        return izq+der if op == "+" else izq-der

    def visitOperacionMultDiv(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        op = ctx.getChild(1).getText()

        if op == "*":
            return izq*der
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

        # Usar el método render_ascii_regression del modelo
        output = self.regresion.render_ascii_regression(
            width=parametros.get('width', 80),
            height=parametros.get('height', 20),
            left_margin=parametros.get('left_margin', 9),
            point_char=parametros.get('point_char', '*'),
            line_char=parametros.get('line_char', '-'),
            title=parametros.get('title'),
            show_stats=parametros.get('show_stats', True)
        )
        print(output)
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
    def visitMostrarTablaASCII(self, ctx):
        data = self.visit(ctx.expresion())
        
        # Parámetros opcionales con valores por defecto
        params = {
            'max_rows': 20,
            'max_cols': 20,
            'max_col_width': 30,
            'floatfmt': '.6g',
            'show_index': True,
            'headers': None
        }
        
        if ctx.parametrosTabla():
            for p in ctx.parametrosTabla().parametroTabla():
                key = p.getChild(0).getText()
                val_node = p.getChild(2)

                # Obtener texto del nodo (funciona tanto para terminales como para sub-árboles simples)
                txt = val_node.getText() if hasattr(val_node, 'getText') else None

                # Manejar diferentes tipos de valores
                if key in ['max_rows', 'max_cols', 'max_col_width']:
                    # txt debería ser un número (ej. '10'), convertir a int
                    try:
                        params[key] = int(float(txt))
                    except Exception:
                        # fallback: intentar evaluar la expresión si es una sub-expresión
                        val = self.visit(val_node)
                        if val is not None:
                            params[key] = int(val)
                elif key == 'show_index':
                    params[key] = (txt == 'True')
                elif key == 'floatfmt':
                    params[key] = txt.strip('"').strip("'") if txt is not None else self.visit(val_node)
                elif key == 'headers':
                    # headers es una lista, usar visit para construirla
                    params[key] = self.visit(val_node)
        
        # Renderizar tabla
        tabla = ascii_table(data, **params)
        print(tabla)
        return None
    def visitGraficarPerdidaMLP(self, ctx):
        # Graficar el historial de pérdida usando graficar_linea_ascii
        if self.mlp and self.mlp.loss_history:
            print("\nHistorial de pérdida del entrenamiento:")
            graficar_linea_ascii(self.mlp.loss_history, width=60, height=15)
        else:
            print("No hay historial de pérdida disponible. Entrena el modelo primero.")
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
