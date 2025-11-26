# Generated from ./visitor/LenguajeDominioEspecifico.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LenguajeDominioEspecificoParser import LenguajeDominioEspecificoParser
else:
    from LenguajeDominioEspecificoParser import LenguajeDominioEspecificoParser

# This class defines a complete generic visitor for a parse tree produced by LenguajeDominioEspecificoParser.

class LenguajeDominioEspecificoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LenguajeDominioEspecificoParser#programa.
    def visitPrograma(self, ctx:LenguajeDominioEspecificoParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#instruccion.
    def visitInstruccion(self, ctx:LenguajeDominioEspecificoParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#buclefor.
    def visitBuclefor(self, ctx:LenguajeDominioEspecificoParser.BucleforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#buclewhile.
    def visitBuclewhile(self, ctx:LenguajeDominioEspecificoParser.BuclewhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#comentario.
    def visitComentario(self, ctx:LenguajeDominioEspecificoParser.ComentarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#asignacion.
    def visitAsignacion(self, ctx:LenguajeDominioEspecificoParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#ExpresionLista.
    def visitExpresionLista(self, ctx:LenguajeDominioEspecificoParser.ExpresionListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#ExpresionNumero.
    def visitExpresionNumero(self, ctx:LenguajeDominioEspecificoParser.ExpresionNumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#ExpresionParentesis.
    def visitExpresionParentesis(self, ctx:LenguajeDominioEspecificoParser.ExpresionParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#ExpresionComparacion.
    def visitExpresionComparacion(self, ctx:LenguajeDominioEspecificoParser.ExpresionComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#OperacionSumaResta.
    def visitOperacionSumaResta(self, ctx:LenguajeDominioEspecificoParser.OperacionSumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#ExpresionVariable.
    def visitExpresionVariable(self, ctx:LenguajeDominioEspecificoParser.ExpresionVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#OperacionMatrizExpr.
    def visitOperacionMatrizExpr(self, ctx:LenguajeDominioEspecificoParser.OperacionMatrizExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#ExpresionString.
    def visitExpresionString(self, ctx:LenguajeDominioEspecificoParser.ExpresionStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#ExpresionMatriz.
    def visitExpresionMatriz(self, ctx:LenguajeDominioEspecificoParser.ExpresionMatrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#OperacionMultDiv.
    def visitOperacionMultDiv(self, ctx:LenguajeDominioEspecificoParser.OperacionMultDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#MatrizMultiFila.
    def visitMatrizMultiFila(self, ctx:LenguajeDominioEspecificoParser.MatrizMultiFilaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#MatrizUnidimensional.
    def visitMatrizUnidimensional(self, ctx:LenguajeDominioEspecificoParser.MatrizUnidimensionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#fila.
    def visitFila(self, ctx:LenguajeDominioEspecificoParser.FilaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#lista.
    def visitLista(self, ctx:LenguajeDominioEspecificoParser.ListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#parametrosMatriz.
    def visitParametrosMatriz(self, ctx:LenguajeDominioEspecificoParser.ParametrosMatrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#CrearRegresion.
    def visitCrearRegresion(self, ctx:LenguajeDominioEspecificoParser.CrearRegresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#EntrenarRegresion.
    def visitEntrenarRegresion(self, ctx:LenguajeDominioEspecificoParser.EntrenarRegresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#PredecirRegresion.
    def visitPredecirRegresion(self, ctx:LenguajeDominioEspecificoParser.PredecirRegresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#ObtenerMetricaRegresion.
    def visitObtenerMetricaRegresion(self, ctx:LenguajeDominioEspecificoParser.ObtenerMetricaRegresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#GraficarRegresion.
    def visitGraficarRegresion(self, ctx:LenguajeDominioEspecificoParser.GraficarRegresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#parametrosPlot.
    def visitParametrosPlot(self, ctx:LenguajeDominioEspecificoParser.ParametrosPlotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#parametroPlot.
    def visitParametroPlot(self, ctx:LenguajeDominioEspecificoParser.ParametroPlotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#CrearMLP.
    def visitCrearMLP(self, ctx:LenguajeDominioEspecificoParser.CrearMLPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#EntrenarMLP.
    def visitEntrenarMLP(self, ctx:LenguajeDominioEspecificoParser.EntrenarMLPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#PredecirMLP.
    def visitPredecirMLP(self, ctx:LenguajeDominioEspecificoParser.PredecirMLPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#EvaluarMLP.
    def visitEvaluarMLP(self, ctx:LenguajeDominioEspecificoParser.EvaluarMLPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#GraficarPerdidaMLP.
    def visitGraficarPerdidaMLP(self, ctx:LenguajeDominioEspecificoParser.GraficarPerdidaMLPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#parametrosMLP.
    def visitParametrosMLP(self, ctx:LenguajeDominioEspecificoParser.ParametrosMLPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#parametroMLP.
    def visitParametroMLP(self, ctx:LenguajeDominioEspecificoParser.ParametroMLPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#parametrosEntrenamiento.
    def visitParametrosEntrenamiento(self, ctx:LenguajeDominioEspecificoParser.ParametrosEntrenamientoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#parametroEntrenamiento.
    def visitParametroEntrenamiento(self, ctx:LenguajeDominioEspecificoParser.ParametroEntrenamientoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDominioEspecificoParser#impresion.
    def visitImpresion(self, ctx:LenguajeDominioEspecificoParser.ImpresionContext):
        return self.visitChildren(ctx)



del LenguajeDominioEspecificoParser