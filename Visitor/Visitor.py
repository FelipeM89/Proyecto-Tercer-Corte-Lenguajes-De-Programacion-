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
from Librerias.LibreriaKMeans import *


class Visitor(LenguajeDominioEspecificoVisitor):

    def __init__(self):
        self.memoria = {}                 # Variables normales
        self.regresion = None             # Modelo de regresión lineal
        self.mlp = None                   # Perceptrón multicapa
        self.kmeans = None                # K-means clustering
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
    #  CONDICIONALES IF/ELIF/ELSE
    # ----------------------------
    def visitCondicional(self, ctx):
        # Contar cuántas expresiones y grupos de instrucciones hay
        num_expresiones = len(ctx.expresion())
        idx_expr = 0
        idx_instr_block = 0
        
        # Evaluar IF
        condicion = self.visit(ctx.expresion(idx_expr))
        if self._es_verdadero(condicion):
            # Ejecutar instrucciones del IF
            start_idx = 0
            for i, child in enumerate(ctx.children):
                if child.getText() == ':' and start_idx == 0:
                    # Encontramos el primer ':'
                    for j in range(i + 2, len(ctx.children)):  # +2 para saltar ':' y NEWLINE
                        if ctx.children[j].__class__.__name__ == 'InstruccionContext':
                            self.visit(ctx.children[j])
                        elif ctx.children[j].getText() in ['elif', 'else']:
                            break
                    return None
        idx_expr += 1
        
        # Evaluar ELIFs
        elif_count = len([c for c in ctx.children if hasattr(c, 'getText') and c.getText() == 'elif'])
        for _ in range(elif_count):
            if idx_expr < num_expresiones:
                condicion = self.visit(ctx.expresion(idx_expr))
                if self._es_verdadero(condicion):
                   # Ejecutar instrucciones de este ELIF
                    in_elif = False
                    for i, child in enumerate(ctx.children):
                        if hasattr(child, 'getText'):
                            if child.getText() == 'elif' and not in_elif:
                                in_elif = True
                                continue
                            if in_elif and child.getText() == ':':
                                for j in range(i + 2, len(ctx.children)):
                                    if ctx.children[j].__class__.__name__ == 'InstruccionContext':
                                        self.visit(ctx.children[j])
                                    elif hasattr(ctx.children[j], 'getText') and ctx.children[j].getText() in ['elif', 'else']:
                                        break
                                return None
                idx_expr += 1
        
        # Ejecutar ELSE si existe
        if ctx.ELSE():
            in_else = False
            for i, child in enumerate(ctx.children):
                if hasattr(child, 'getText'):
                    if child.getText() == 'else':
                        in_else = True
                        continue
                    if in_else and child.getText() == ':':
                        for j in range(i + 2, len(ctx.children)):
                            if ctx.children[j].__class__.__name__ == 'InstruccionContext':
                                self.visit(ctx.children[j])
                        return None
        
        return None

    def _es_verdadero(self, valor):
        """Evalúa si un valor es considerado verdadero"""
        if isinstance(valor, bool):
            return valor
        if isinstance(valor, (int, float)):
            return valor != 0
        if valor is None:
            return False
        return True


    # ----------------------------
    #    BUCLES FOR Y WHILE
    # ----------------------------
    def visitBuclefor(self, ctx):
        variable = ctx.ID().getText()
        inicio = int(float(ctx.NUMBER(0).getText()))
        fin = int(float(ctx.NUMBER(1).getText()))
        
        for i in range(inicio, fin):
            self.memoria[variable] = i
            for instr in ctx.instruccion():
                self.visit(instr)
        
        return None

    def visitBuclewhile(self, ctx):
        while True:
            condicion = self.visit(ctx.expresion())
            if not self._es_verdadero(condicion):
                break
            for instr in ctx.instruccion():
                self.visit(instr)
        return None


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

    def visitExpresionBooleano(self, ctx):
        return ctx.getText() == 'True'

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

    def visitExpresionLogica(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        op = ctx.getChild(1).getText()
        
        if op == "and":
            return self._es_verdadero(izq) and self._es_verdadero(der)
        elif op == "or":
            return self._es_verdadero(izq) or self._es_verdadero(der)

    def visitExpresionNot(self, ctx):
        valor = self.visit(ctx.expresion())
        return not self._es_verdadero(valor)

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

    def visitExpresionOperacion(self, ctx):
        return self.visit(ctx.operaciones())


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
        # Valores por defecto
        width = 80
        height = 20
        left_margin = 9
        point_char = '*'
        line_char = '-'
        title = None
        show_stats = True
        output_file = None
        
        # Procesar parámetros opcionales
        if ctx.parametrosPlot():
            for p in ctx.parametrosPlot().parametroPlot():
                key = p.getChild(0).getText()
                val_node = p.getChild(2)
                txt = val_node.getText()
                
                if key == 'width':
                    width = int(float(txt))
                elif key == 'height':
                    height = int(float(txt))
                elif key == 'left_margin':
                    left_margin = int(float(txt))
                elif key == 'point_char':
                    point_char = txt.strip('"').strip("'")
                elif key == 'line_char':
                    line_char = txt.strip('"').strip("'")
                elif key == 'title':
                    title = txt.strip('"').strip("'")
                elif key == 'show_stats':
                    show_stats = (txt == 'True')
                elif key == 'output_file':
                    output_file = txt.strip('"').strip("'")

        # Generar gráfica
        output = self.regresion.render_ascii_regression(
            width=width,
            height=height,
            left_margin=left_margin,
            point_char=point_char,
            line_char=line_char,
            title=title,
            show_stats=show_stats
        )
        
        # Guardar en archivo si se especifica
        if output_file:
            guardar_grafica_ascii(output, output_file)
        else:
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
                if key == "epochs": epochs = int(value)
                elif key == "batch_size": batch = int(value)
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
        if not self.mlp or not self.mlp.loss_history:
            print("No hay historial de pérdida. Entrena el modelo primero.")
            return None
        
        output_file = None
        if ctx.STRING():
            output_file = ctx.STRING().getText().strip('"').strip("'")
        
        # Graficar usando graficar_linea_ascii
        graficar_linea_ascii(
            self.mlp.loss_history, 
            width=60, 
            height=15, 
            title="Pérdida del MLP",
            archivo=output_file
        )
        
        return None


    # ----------------------------
    #    K-MEANS CLUSTERING
    # ----------------------------
    def visitCrearKMeans(self, ctx):
        n_clusters = 3
        max_iter = 100
        random_state = None
        
        for p in ctx.parametrosKMeans().parametroKMeans():
            key = p.getChild(0).getText()
            value = float(p.getChild(2).getText())
            
            if key == 'n_clusters':
                n_clusters = int(value)
            elif key == 'max_iter':
                max_iter = int(value)
            elif key == 'random_state':
                random_state = int(value)
        
        self.kmeans = KMeans(n_clusters, max_iter, random_state)
        nombre = ctx.ID().getText()
        self.memoria[nombre] = self.kmeans
        return self.kmeans

    def visitEntrenarKMeans(self, ctx):
        X = self.visit(ctx.expresion())
        self.kmeans.fit(X)
        print(f"K-means entrenado con {self.kmeans.n_clusters} clusters")
        return None

    def visitPredecirKMeans(self, ctx):
        nombre = ctx.ID().getText()
        X = self.visit(ctx.expresion())
        labels = self.kmeans.predict(X)
        self.memoria[nombre] = labels
        print(f"Predicción: {labels}")
        return labels

    def visitObtenerCentroides(self, ctx):
        nombre = ctx.ID().getText()
        centroids = self.kmeans.get_centroids()
        self.memoria[nombre] = centroids
        print(f"Centroides:\n{centroids}")
        return centroids

    def visitGraficarKMeans(self, ctx):
        
        
        output_file = None
        if ctx.STRING():
            output_file = ctx.STRING().getText().strip('"').strip("'")
        
        # Mostrar visualización en consola y opcionalmente guardar
        if hasattr(self.kmeans, 'labels') and self.kmeans.labels:
            # Necesitamos los datos originales - los guardamos durante fit
            # Por ahora solo mostramos los centroides
            print(f"\nCentroides del K-means:")
            for i, centroid in enumerate(self.kmeans.centroids):
                print(f"  Cluster {i}: {centroid}")
        else:
            print("Entrena el modelo primero con kmeans.fit()")
        
        return None


    # ----------------------------
    #   GRÁFICAS GENERALES
    # ----------------------------
    def visitGraficar(self, ctx):
        x = self.visit(ctx.x)
        y = self.visit(ctx.y)
        archivo = ctx.archivo.text.strip('"').strip("'")
        
        width = 60
        height = 20
        title = None
        
        if ctx.parametrosGraficar():
            for p in ctx.parametrosGraficar().parametroGraficar():
                key = p.getChild(0).getText()
                txt = p.getChild(2).getText()
                
                if key == 'width':
                    width = int(float(txt))
                elif key == 'height':
                    height = int(float(txt))
                elif key == 'title':
                    title = txt.strip('"').strip("'")
        
        # Usar graficar_puntos_ascii con guardado automático
        graficar_puntos_ascii(x, y, width=width, height=height, title=title, archivo=archivo)
        
        return None


    # ----------------------------
    #     OPERACIONES ARITMÉTICAS
    # ----------------------------
    def visitOperaciones(self, ctx):
        oper = ctx.getChild(0).getText()

        def eval_expr_node(node):
            val = self.visit(node)
            if val is None:
                raise ValueError("Expresión no evaluable (valor None)")
            try:
                return float(val)
            except Exception:
                raise ValueError(f"Valor no numérico en expresión: {val}")

        if oper == "abs":
            val = eval_expr_node(ctx.expresion())
            return abs(val)

        if oper == "sqrt":
            val = eval_expr_node(ctx.expresion())
            if val < 0:
                raise ValueError(f"sqrt: dominio inválido, se recibió {val}")
            return sqrt(val)

        if oper == "exp":
            val = eval_expr_node(ctx.expresion())
            return exp(val)

        if oper == "ln":
            val = eval_expr_node(ctx.expresion())
            if val <= 0:
                raise ValueError(f"ln: dominio inválido, se recibió {val}")
            return ln(val)

        if oper == "sin":
            val = eval_expr_node(ctx.expresion())
            return sin(val)

        if oper == "cos":
            val = eval_expr_node(ctx.expresion())
            return cos(val)

        if oper == "tan":
            val = eval_expr_node(ctx.expresion())
            return tan(val)

        if oper == "factorial":
            val = self.visit(ctx.expresion())
            if val is None:
                raise ValueError("factorial: expresión no evaluable")
            try:
                f = float(val)
            except Exception:
                raise ValueError(f"factorial: valor no numérico {val}")
            if not f.is_integer():
                raise ValueError(f"factorial: se requiere entero no negativo, se recibió {f}")
            n = int(f)
            return factorial(n)

        if oper in ("powf", "div", "mod"):
            params = ctx.parametrosOp()
            if params is None or len(params.expresion()) < 2:
                raise ValueError(f"{oper} requiere dos argumentos")
            a = eval_expr_node(params.expresion(0))
            b = eval_expr_node(params.expresion(1))

            if oper == "powf":
                return powf(a, b)
            if oper == "div":
                return division(a, b)
            if oper == "mod":
                return modulo(a, b)

        raise ValueError(f"Operación desconocida: {oper}")


    # ----------------------------
    #          PRINT
    # ----------------------------
    def visitImpresion(self, ctx):
        try:
            if ctx.STRING():
                base = ctx.STRING().getText().strip('"').strip("'")
                if ctx.expresion():
                    values = [self.visit(e) for e in ctx.expresion()]
                    print(base, *values)
                else:
                    print(base)
            elif ctx.operaciones():
                resultado = self.visit(ctx.operaciones())
                print(resultado)
            elif ctx.expresion():
                print(self.visit(ctx.expresion(0)))
        except Exception as e:
            print("\nError de evaluación:", str(e))
        return None


    # ----------------------------
    #      TABLAS ASCII
    # ----------------------------
    def visitMostrarTablaASCII(self, ctx):
        data = self.visit(ctx.expresion())
        
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
                txt = val_node.getText() if hasattr(val_node, 'getText') else None

                if key in ['max_rows', 'max_cols', 'max_col_width']:
                    try:
                        params[key] = int(float(txt))
                    except Exception:
                        val = self.visit(val_node)
                        if val is not None:
                            params[key] = int(val)
                elif key == 'show_index':
                    params[key] = (txt == 'True')
                elif key == 'floatfmt':
                    params[key] = txt.strip('"').strip("'") if txt is not None else self.visit(val_node)
                elif key == 'headers':
                    params[key] = self.visit(val_node)
        
        tabla = ascii_table(data, **params)
        print(tabla)
        return None


    # ----------------------------
    #    TABLA DE SÍMBOLOS
    # ----------------------------
    def mostrar_tabla_simbolos(self):
        print("\n=== TABLA DE SÍMBOLOS ===")
        
        if not self.memoria:
            print("  (vacía)")
        else:
            for i, (nombre, valor) in enumerate(self.memoria.items(), 1):
                tipo = type(valor).__name__
                
                if isinstance(valor, list):
                    if valor and isinstance(valor[0], list):
                        filas = len(valor)
                        cols = len(valor[0]) if valor else 0
                        print(f"  [{i}] {nombre}: matriz {filas}x{cols}")
                    else:
                        print(f"  [{i}] {nombre}: lista de {len(valor)} elementos")
                else:
                    print(f"  [{i}] {nombre}: {tipo} = {valor}")