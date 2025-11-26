# Generated from ./visitor/LenguajeDominioEspecifico.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LenguajeDominioEspecificoParser import LenguajeDominioEspecificoParser
else:
    from LenguajeDominioEspecificoParser import LenguajeDominioEspecificoParser

# This class defines a complete listener for a parse tree produced by LenguajeDominioEspecificoParser.
class LenguajeDominioEspecificoListener(ParseTreeListener):

    # Enter a parse tree produced by LenguajeDominioEspecificoParser#programa.
    def enterPrograma(self, ctx:LenguajeDominioEspecificoParser.ProgramaContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#programa.
    def exitPrograma(self, ctx:LenguajeDominioEspecificoParser.ProgramaContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#instruccion.
    def enterInstruccion(self, ctx:LenguajeDominioEspecificoParser.InstruccionContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#instruccion.
    def exitInstruccion(self, ctx:LenguajeDominioEspecificoParser.InstruccionContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#buclefor.
    def enterBuclefor(self, ctx:LenguajeDominioEspecificoParser.BucleforContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#buclefor.
    def exitBuclefor(self, ctx:LenguajeDominioEspecificoParser.BucleforContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#buclewhile.
    def enterBuclewhile(self, ctx:LenguajeDominioEspecificoParser.BuclewhileContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#buclewhile.
    def exitBuclewhile(self, ctx:LenguajeDominioEspecificoParser.BuclewhileContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#comentario.
    def enterComentario(self, ctx:LenguajeDominioEspecificoParser.ComentarioContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#comentario.
    def exitComentario(self, ctx:LenguajeDominioEspecificoParser.ComentarioContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#asignacion.
    def enterAsignacion(self, ctx:LenguajeDominioEspecificoParser.AsignacionContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#asignacion.
    def exitAsignacion(self, ctx:LenguajeDominioEspecificoParser.AsignacionContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#ExpresionLista.
    def enterExpresionLista(self, ctx:LenguajeDominioEspecificoParser.ExpresionListaContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#ExpresionLista.
    def exitExpresionLista(self, ctx:LenguajeDominioEspecificoParser.ExpresionListaContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#ExpresionNumero.
    def enterExpresionNumero(self, ctx:LenguajeDominioEspecificoParser.ExpresionNumeroContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#ExpresionNumero.
    def exitExpresionNumero(self, ctx:LenguajeDominioEspecificoParser.ExpresionNumeroContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#ExpresionParentesis.
    def enterExpresionParentesis(self, ctx:LenguajeDominioEspecificoParser.ExpresionParentesisContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#ExpresionParentesis.
    def exitExpresionParentesis(self, ctx:LenguajeDominioEspecificoParser.ExpresionParentesisContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#ExpresionComparacion.
    def enterExpresionComparacion(self, ctx:LenguajeDominioEspecificoParser.ExpresionComparacionContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#ExpresionComparacion.
    def exitExpresionComparacion(self, ctx:LenguajeDominioEspecificoParser.ExpresionComparacionContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#OperacionSumaResta.
    def enterOperacionSumaResta(self, ctx:LenguajeDominioEspecificoParser.OperacionSumaRestaContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#OperacionSumaResta.
    def exitOperacionSumaResta(self, ctx:LenguajeDominioEspecificoParser.OperacionSumaRestaContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#ExpresionVariable.
    def enterExpresionVariable(self, ctx:LenguajeDominioEspecificoParser.ExpresionVariableContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#ExpresionVariable.
    def exitExpresionVariable(self, ctx:LenguajeDominioEspecificoParser.ExpresionVariableContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#OperacionMatrizExpr.
    def enterOperacionMatrizExpr(self, ctx:LenguajeDominioEspecificoParser.OperacionMatrizExprContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#OperacionMatrizExpr.
    def exitOperacionMatrizExpr(self, ctx:LenguajeDominioEspecificoParser.OperacionMatrizExprContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#ExpresionString.
    def enterExpresionString(self, ctx:LenguajeDominioEspecificoParser.ExpresionStringContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#ExpresionString.
    def exitExpresionString(self, ctx:LenguajeDominioEspecificoParser.ExpresionStringContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#ExpresionMatriz.
    def enterExpresionMatriz(self, ctx:LenguajeDominioEspecificoParser.ExpresionMatrizContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#ExpresionMatriz.
    def exitExpresionMatriz(self, ctx:LenguajeDominioEspecificoParser.ExpresionMatrizContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#OperacionMultDiv.
    def enterOperacionMultDiv(self, ctx:LenguajeDominioEspecificoParser.OperacionMultDivContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#OperacionMultDiv.
    def exitOperacionMultDiv(self, ctx:LenguajeDominioEspecificoParser.OperacionMultDivContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#MatrizMultiFila.
    def enterMatrizMultiFila(self, ctx:LenguajeDominioEspecificoParser.MatrizMultiFilaContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#MatrizMultiFila.
    def exitMatrizMultiFila(self, ctx:LenguajeDominioEspecificoParser.MatrizMultiFilaContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#MatrizUnidimensional.
    def enterMatrizUnidimensional(self, ctx:LenguajeDominioEspecificoParser.MatrizUnidimensionalContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#MatrizUnidimensional.
    def exitMatrizUnidimensional(self, ctx:LenguajeDominioEspecificoParser.MatrizUnidimensionalContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#fila.
    def enterFila(self, ctx:LenguajeDominioEspecificoParser.FilaContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#fila.
    def exitFila(self, ctx:LenguajeDominioEspecificoParser.FilaContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#lista.
    def enterLista(self, ctx:LenguajeDominioEspecificoParser.ListaContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#lista.
    def exitLista(self, ctx:LenguajeDominioEspecificoParser.ListaContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#parametrosMatriz.
    def enterParametrosMatriz(self, ctx:LenguajeDominioEspecificoParser.ParametrosMatrizContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#parametrosMatriz.
    def exitParametrosMatriz(self, ctx:LenguajeDominioEspecificoParser.ParametrosMatrizContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#CrearRegresion.
    def enterCrearRegresion(self, ctx:LenguajeDominioEspecificoParser.CrearRegresionContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#CrearRegresion.
    def exitCrearRegresion(self, ctx:LenguajeDominioEspecificoParser.CrearRegresionContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#EntrenarRegresion.
    def enterEntrenarRegresion(self, ctx:LenguajeDominioEspecificoParser.EntrenarRegresionContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#EntrenarRegresion.
    def exitEntrenarRegresion(self, ctx:LenguajeDominioEspecificoParser.EntrenarRegresionContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#PredecirRegresion.
    def enterPredecirRegresion(self, ctx:LenguajeDominioEspecificoParser.PredecirRegresionContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#PredecirRegresion.
    def exitPredecirRegresion(self, ctx:LenguajeDominioEspecificoParser.PredecirRegresionContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#ObtenerMetricaRegresion.
    def enterObtenerMetricaRegresion(self, ctx:LenguajeDominioEspecificoParser.ObtenerMetricaRegresionContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#ObtenerMetricaRegresion.
    def exitObtenerMetricaRegresion(self, ctx:LenguajeDominioEspecificoParser.ObtenerMetricaRegresionContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#GraficarRegresion.
    def enterGraficarRegresion(self, ctx:LenguajeDominioEspecificoParser.GraficarRegresionContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#GraficarRegresion.
    def exitGraficarRegresion(self, ctx:LenguajeDominioEspecificoParser.GraficarRegresionContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#parametrosPlot.
    def enterParametrosPlot(self, ctx:LenguajeDominioEspecificoParser.ParametrosPlotContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#parametrosPlot.
    def exitParametrosPlot(self, ctx:LenguajeDominioEspecificoParser.ParametrosPlotContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#parametroPlot.
    def enterParametroPlot(self, ctx:LenguajeDominioEspecificoParser.ParametroPlotContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#parametroPlot.
    def exitParametroPlot(self, ctx:LenguajeDominioEspecificoParser.ParametroPlotContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#CrearMLP.
    def enterCrearMLP(self, ctx:LenguajeDominioEspecificoParser.CrearMLPContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#CrearMLP.
    def exitCrearMLP(self, ctx:LenguajeDominioEspecificoParser.CrearMLPContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#EntrenarMLP.
    def enterEntrenarMLP(self, ctx:LenguajeDominioEspecificoParser.EntrenarMLPContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#EntrenarMLP.
    def exitEntrenarMLP(self, ctx:LenguajeDominioEspecificoParser.EntrenarMLPContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#PredecirMLP.
    def enterPredecirMLP(self, ctx:LenguajeDominioEspecificoParser.PredecirMLPContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#PredecirMLP.
    def exitPredecirMLP(self, ctx:LenguajeDominioEspecificoParser.PredecirMLPContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#EvaluarMLP.
    def enterEvaluarMLP(self, ctx:LenguajeDominioEspecificoParser.EvaluarMLPContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#EvaluarMLP.
    def exitEvaluarMLP(self, ctx:LenguajeDominioEspecificoParser.EvaluarMLPContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#GraficarPerdidaMLP.
    def enterGraficarPerdidaMLP(self, ctx:LenguajeDominioEspecificoParser.GraficarPerdidaMLPContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#GraficarPerdidaMLP.
    def exitGraficarPerdidaMLP(self, ctx:LenguajeDominioEspecificoParser.GraficarPerdidaMLPContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#parametrosMLP.
    def enterParametrosMLP(self, ctx:LenguajeDominioEspecificoParser.ParametrosMLPContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#parametrosMLP.
    def exitParametrosMLP(self, ctx:LenguajeDominioEspecificoParser.ParametrosMLPContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#parametroMLP.
    def enterParametroMLP(self, ctx:LenguajeDominioEspecificoParser.ParametroMLPContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#parametroMLP.
    def exitParametroMLP(self, ctx:LenguajeDominioEspecificoParser.ParametroMLPContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#parametrosEntrenamiento.
    def enterParametrosEntrenamiento(self, ctx:LenguajeDominioEspecificoParser.ParametrosEntrenamientoContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#parametrosEntrenamiento.
    def exitParametrosEntrenamiento(self, ctx:LenguajeDominioEspecificoParser.ParametrosEntrenamientoContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#parametroEntrenamiento.
    def enterParametroEntrenamiento(self, ctx:LenguajeDominioEspecificoParser.ParametroEntrenamientoContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#parametroEntrenamiento.
    def exitParametroEntrenamiento(self, ctx:LenguajeDominioEspecificoParser.ParametroEntrenamientoContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#impresion.
    def enterImpresion(self, ctx:LenguajeDominioEspecificoParser.ImpresionContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#impresion.
    def exitImpresion(self, ctx:LenguajeDominioEspecificoParser.ImpresionContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#MostrarTablaASCII.
    def enterMostrarTablaASCII(self, ctx:LenguajeDominioEspecificoParser.MostrarTablaASCIIContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#MostrarTablaASCII.
    def exitMostrarTablaASCII(self, ctx:LenguajeDominioEspecificoParser.MostrarTablaASCIIContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#parametrosTabla.
    def enterParametrosTabla(self, ctx:LenguajeDominioEspecificoParser.ParametrosTablaContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#parametrosTabla.
    def exitParametrosTabla(self, ctx:LenguajeDominioEspecificoParser.ParametrosTablaContext):
        pass


    # Enter a parse tree produced by LenguajeDominioEspecificoParser#parametroTabla.
    def enterParametroTabla(self, ctx:LenguajeDominioEspecificoParser.ParametroTablaContext):
        pass

    # Exit a parse tree produced by LenguajeDominioEspecificoParser#parametroTabla.
    def exitParametroTabla(self, ctx:LenguajeDominioEspecificoParser.ParametroTablaContext):
        pass



del LenguajeDominioEspecificoParser