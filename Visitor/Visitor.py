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
        """
        Maneja estructuras if/elif/else con llaves
        Sintaxis: if (condicion) { instrucciones } elif (condicion) { instrucciones } else { instrucciones }
        """
        num_expresiones = len(ctx.expresion())
        
        # Evaluar IF principal
        condicion_if = self.visit(ctx.expresion(0))
        if self._es_verdadero(condicion_if):
            # Ejecutar instrucciones del bloque IF
            for instr in ctx.instruccion()[:self._contar_instrucciones_bloque(ctx, 0)]:
                self.visit(instr)
            return None
        
        # Evaluar ELIFs si existen
        num_elifs = ctx.getChildCount() - len([c for c in ctx.children if hasattr(c, 'symbol') and c.symbol.text in ['if', 'else']])
        elif_count = sum(1 for i in range(ctx.getChildCount()) if ctx.getChild(i).getText() == 'elif')
        
        offset_instr = self._contar_instrucciones_bloque(ctx, 0)
        for i in range(1, elif_count + 1):
            if i < num_expresiones:
                condicion_elif = self.visit(ctx.expresion(i))
                if self._es_verdadero(condicion_elif):
                    # Ejecutar instrucciones de este ELIF
                    num_instr = self._contar_instrucciones_bloque(ctx, i)
                    for instr in ctx.instruccion()[offset_instr:offset_instr + num_instr]:
                        self.visit(instr)
                    return None
                offset_instr += num_instr
        
        # Ejecutar ELSE si existe y no se ejecutó ningún bloque anterior
        if ctx.ELSE():
            for instr in ctx.instruccion()[offset_instr:]:
                self.visit(instr)
        
        return None

    def _contar_instrucciones_bloque(self, ctx, indice_bloque):
        """Cuenta las instrucciones dentro de un bloque específico"""
        # Implementación simple: divide instrucciones por bloques
        # En una implementación real, deberías analizar la estructura del árbol
        total_instrucciones = len(ctx.instruccion())
        num_bloques = 1 + sum(1 for i in range(ctx.getChildCount()) if ctx.getChild(i).getText() in ['elif', 'else'])
        return total_instrucciones // num_bloques if num_bloques > 0 else total_instrucciones

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
        """
        Maneja bucles for con sintaxis: for (i in range(inicio, fin)) { instrucciones }
        """
        variable = ctx.ID().getText()
        inicio = int(float(self.visit(ctx.expresion(0))))
        fin = int(float(self.visit(ctx.expresion(1))))
        
        for i in range(inicio, fin):
            self.memoria[variable] = i
            for instr in ctx.instruccion():
                self.visit(instr)
        
        return None

    def visitBuclewhile(self, ctx):
        """
        Maneja bucles while con sintaxis: while (condicion) { instrucciones }
        """
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

    def visitLista(self, ctx):
        """Visita una lista y retorna sus elementos evaluados"""
        return [self.visit(e) for e in ctx.expresion()]

    def visitExpresionMatriz(self, ctx):
        return self.visit(ctx.matriz())

    def visitExpresionOperacion(self, ctx):
        return self.visit(ctx.operaciones())

    def visitAccesoCentroides(self, ctx):
        """Acceso a centroides: kmeans.centroids"""
        nombre_modelo = ctx.ID().getText()
        modelo = self.memoria.get(nombre_modelo)
        if not modelo:
            raise ValueError(f"Modelo '{nombre_modelo}' no encontrado.")
        
        if not hasattr(modelo, 'centroids'):
            raise ValueError(f"El objeto '{nombre_modelo}' no tiene centroides.")
        
        if modelo.centroids is None:
            raise ValueError("El modelo no ha sido entrenado. Llama a fit() primero.")
        
        return modelo.centroids


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
        return regresion_lineal_model()

    def visitEntrenarRegresion(self, ctx):
        nombre_modelo = ctx.ID().getText()
        modelo = self.memoria.get(nombre_modelo)
        if not modelo:
            raise ValueError(f"Modelo de regresión '{nombre_modelo}' no encontrado o no definido.")
        
        X = self.visit(ctx.x)
        y = self.visit(ctx.y)
        modelo.fit(X, y)
        return None

    def visitPredecirModelo(self, ctx):
        """
        Predicción genérica que funciona con cualquier modelo (Regresión, MLP, KMeans).
        Sintaxis: resultado = modelo.predict(datos);
        """
        target = ctx.target.text
        nombre_modelo = ctx.modelo.text
        modelo = self.memoria.get(nombre_modelo)
        if not modelo:
            raise ValueError(f"Modelo '{nombre_modelo}' no encontrado.")
        
        x = self.visit(ctx.expresion())
        pred = modelo.predict(x)
        self.memoria[target] = pred
        return pred

    def visitObtenerMetricaRegresion(self, ctx):
        target = ctx.target.text
        nombre_modelo = ctx.modelo.text
        modelo = self.memoria.get(nombre_modelo)
        if not modelo:
            raise ValueError(f"Modelo de regresión '{nombre_modelo}' no encontrado.")
            
        met = ctx.metrica.text

        if met == "mse":
            val = modelo.mse()
        elif met == "mae":
            val = modelo.mae()
        elif met == "r2":
            val = modelo.r2()
        elif met == "rmse":
            val = modelo.rmse()

        self.memoria[target] = val
        return val

    def visitGraficarRegresion(self, ctx):
        nombre_modelo = ctx.ID().getText()
        modelo = self.memoria.get(nombre_modelo)
        if not modelo:
            raise ValueError(f"Modelo de regresión '{nombre_modelo}' no encontrado.")

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

        # Usar el método render_ascii_regression del modelo
        output = modelo.render_ascii_regression(
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
        """
        Crea un perceptrón multicapa con sintaxis:
        mlp = PerceptronMulticapa(layers=[2,5,3,1], learning_rate=0.1, seed=42);
        """
        nombre = ctx.ID().getText()
        
        layers = None
        learning_rate = 0.1
        seed = 1234
        
        for p in ctx.parametrosMLP().parametroMLP():
            # Usar los métodos generados por ANTLR para determinar el tipo
            if p.lista() is not None:
                # Es el parámetro layers
                layers = self.visit(p.lista())
            elif p.NUMBER() is not None:
                # Es learning_rate o seed - determinar por el primer hijo
                key = p.getChild(0).getText()
                val = float(p.NUMBER().getText())
                if key == 'learning_rate':
                    learning_rate = val
                elif key == 'seed':
                    seed = int(val)
        
        if layers is None:
            raise ValueError("El parámetro 'layers' es obligatorio para PerceptronMulticapa")
        
        # Convertir layers a lista de enteros
        layers = [int(float(x)) for x in layers]
        
        mlp = PerceptronMulticapa(layers, learning_rate, seed)
        self.memoria[nombre] = mlp
        
        return mlp

    def visitEntrenarMLP(self, ctx):
        """
        Entrena el MLP con sintaxis:
        mlp.fit(X, y, epochs=100, batch_size=1, verbose=True);
        """
        nombre_modelo = ctx.ID().getText()
        modelo = self.memoria.get(nombre_modelo)
        if not modelo:
            raise ValueError(f"Modelo MLP '{nombre_modelo}' no encontrado.")
        
        X = self.visit(ctx.x)
        y = self.visit(ctx.y)

        # Parámetros opcionales
        epochs = 100
        batch = 1
        verbose = False

        if ctx.parametrosEntrenamiento():
            for p in ctx.parametrosEntrenamiento().parametroEntrenamiento():
                key = p.getChild(0).getText()
                value = p.getChild(2).getText()
                
                if key == "epochs":
                    epochs = int(float(value))
                elif key == "batch_size":
                    batch = int(float(value))
                elif key == "verbose":
                    verbose = (value == "True")

        modelo.fit(X, y, epochs, batch, verbose)
        return None

    def visitEvaluarMLP(self, ctx):
        """
        Evalúa el MLP: score = mlp.score(X, y);
        """
        target = ctx.target.text
        nombre_modelo = ctx.modelo.text
        modelo = self.memoria.get(nombre_modelo)
        if not modelo:
            raise ValueError(f"Modelo MLP '{nombre_modelo}' no encontrado.")
        
        X = self.visit(ctx.x)
        y = self.visit(ctx.y)
        score = modelo.score(X, y)
        self.memoria[target] = score
        return score

    def visitGraficarPerdidaMLP(self, ctx):
        """
        Grafica la pérdida del MLP: mlp.plot_loss("output.txt");
        """
        nombre_modelo = ctx.ID().getText()
        modelo = self.memoria.get(nombre_modelo)
        if not modelo:
            raise ValueError(f"Modelo MLP '{nombre_modelo}' no encontrado.")
        
        if not modelo or not modelo.loss_history:
            print("No hay historial de pérdida. Entrena el modelo primero.")
            return None
        
        output_file = None
        if ctx.STRING():
            output_file = ctx.STRING().getText().strip('"').strip("'")
        
        # Graficar usando graficar_linea_ascii
        graficar_linea_ascii(
            modelo.loss_history, 
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
        """
        Crea un modelo K-means: kmeans = KMeans(n_clusters=3, max_iter=100, seed=42);
        """
        nombre = ctx.ID().getText()
        
        n_clusters = 3
        max_iter = 100
        seed = 1234
        
        for p in ctx.parametrosKMeans().parametroKMeans():
            key = p.getChild(0).getText()
            value = float(p.getChild(2).getText())
            
            if key == 'n_clusters':
                n_clusters = int(value)
            elif key == 'max_iter':
                max_iter = int(value)
            elif key == 'seed':
                seed = int(value)
        
        kmeans = KMeans(n_clusters, max_iter, seed)
        self.memoria[nombre] = kmeans
        return kmeans

    def visitEntrenarKMeans(self, ctx):
        """
        Entrena K-means: kmeans.fit(datos);
        """
        nombre_modelo = ctx.ID().getText()
        modelo = self.memoria.get(nombre_modelo)
        if not modelo:
            raise ValueError(f"Modelo K-means '{nombre_modelo}' no encontrado.")
        
        X = self.visit(ctx.expresion())
        modelo.fit(X)
        print(f"✓ K-means entrenado con {modelo.n_clusters} clusters")
        return None

    def visitGraficarKMeans(self, ctx):
        """
        Grafica los clusters: kmeans.plot(width=80, height=20, output_file="clusters.txt");
        """
        nombre_modelo = ctx.ID().getText()
        modelo = self.memoria.get(nombre_modelo)
        if not modelo:
            raise ValueError(f"Modelo K-means '{nombre_modelo}' no encontrado.")
        
        width = 80
        height = 20
        output_file = None
        
        if ctx.parametrosGraficarKMeans():
            for p in ctx.parametrosGraficarKMeans().parametroGraficarKMeans():
                key = p.getChild(0).getText()
                txt = p.getChild(2).getText()
                
                if key == 'width':
                    width = int(float(txt))
                elif key == 'height':
                    height = int(float(txt))
                elif key == 'output_file':
                    output_file = txt.strip('"').strip("'")
        
        # Generar visualización
        plot_output = modelo.plot_clusters(width, height)
        
        if output_file:
            escribir_txt(output_file, plot_output)
            print(f"✓ Gráfica guardada en: {output_file}")
        else:
            print(plot_output)
        
        return None


    # ----------------------------
    #   GRÁFICAS GENERALES
    # ----------------------------
    def visitGraficar(self, ctx):
        """
        Grafica puntos: graficar(x, y, width=60, height=20, title="Mi Gráfica", output_file="plot.txt");
        """
        x = self.visit(ctx.x)
        y = self.visit(ctx.y)
        
        width = 60
        height = 20
        title = None
        output_file = None
        
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
                elif key == 'output_file':
                    output_file = txt.strip('"').strip("'")
        
        # Usar graficar_puntos_ascii con guardado automático
        graficar_puntos_ascii(x, y, width=width, height=height, title=title, archivo=output_file)
        
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
        """
        Imprime valores: print(x); o print("mensaje", x, y);
        """
        try:
            if ctx.expresion():
                # Evaluar todas las expresiones
                valores = [self.visit(e) for e in ctx.expresion()]
                # Imprimir separados por espacio
                print(*valores)
        except Exception as e:
            print(f"\n Error de evaluación: {str(e)}")
        return None


    def visitMostrarTablaASCII(self, ctx):
        """
        Muestra tabla: mostrar_tabla(data, max_rows=20, max_cols=10, show_index=True);
        """
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
        """Muestra todas las variables almacenadas en memoria"""
 
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
                elif isinstance(valor, regresion_lineal_model):
                    print(f"  [{i}] {nombre}: RegresionLineal(m={valor.m:.4f}, b={valor.b:.4f})")
                elif isinstance(valor, PerceptronMulticapa):
                    print(f"  [{i}] {nombre}: PerceptronMulticapa(layers={valor.layers})")
                elif isinstance(valor, KMeans):
                    print(f"  [{i}] {nombre}: KMeans(n_clusters={valor.n_clusters})")
                else:
                    valor_str = str(valor)
                    if len(valor_str) > 50:
                        valor_str = valor_str[:47] + "..."
                    print(f"  [{i}] {nombre}: {tipo} = {valor_str}")
        print()