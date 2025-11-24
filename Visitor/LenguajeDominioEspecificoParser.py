# Generated from ./visitor/LenguajeDominioEspecifico.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,63,373,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,1,0,4,0,49,8,0,11,0,12,0,50,1,0,
        5,0,54,8,0,10,0,12,0,57,9,0,1,0,5,0,60,8,0,10,0,12,0,63,9,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,74,8,1,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,88,8,2,11,2,12,2,89,1,3,1,3,1,3,1,
        3,1,3,4,3,97,8,3,11,3,12,3,98,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,124,
        8,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,132,8,6,10,6,12,6,135,9,6,1,7,1,
        7,1,7,1,7,5,7,141,8,7,10,7,12,7,144,9,7,1,7,1,7,1,7,1,7,1,7,1,7,
        5,7,152,8,7,10,7,12,7,155,9,7,1,7,1,7,3,7,159,8,7,1,8,1,8,1,8,1,
        8,5,8,165,8,8,10,8,12,8,168,9,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,176,
        8,9,10,9,12,9,179,9,9,3,9,181,8,9,1,9,1,9,1,10,1,10,1,10,5,10,188,
        8,10,10,10,12,10,191,9,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,3,11,228,8,11,1,11,3,11,231,8,11,1,12,1,12,1,12,5,12,236,8,
        12,10,12,12,12,239,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        3,13,262,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,3,14,280,8,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,309,8,14,
        1,15,1,15,1,15,5,15,314,8,15,10,15,12,15,317,9,15,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,
        334,8,16,1,17,1,17,1,17,5,17,339,8,17,10,17,12,17,342,9,17,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,353,8,18,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,5,19,365,8,19,10,19,12,19,
        368,9,19,1,19,3,19,371,8,19,1,19,0,1,12,20,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,0,5,1,0,12,17,1,0,6,8,1,0,9,10,
        1,0,23,26,1,0,54,55,406,0,43,1,0,0,0,2,73,1,0,0,0,4,75,1,0,0,0,6,
        91,1,0,0,0,8,100,1,0,0,0,10,102,1,0,0,0,12,123,1,0,0,0,14,158,1,
        0,0,0,16,160,1,0,0,0,18,171,1,0,0,0,20,184,1,0,0,0,22,230,1,0,0,
        0,24,232,1,0,0,0,26,261,1,0,0,0,28,308,1,0,0,0,30,310,1,0,0,0,32,
        333,1,0,0,0,34,335,1,0,0,0,36,352,1,0,0,0,38,370,1,0,0,0,40,42,5,
        63,0,0,41,40,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,
        46,1,0,0,0,45,43,1,0,0,0,46,55,3,2,1,0,47,49,5,63,0,0,48,47,1,0,
        0,0,49,50,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,52,1,0,0,0,52,54,
        3,2,1,0,53,48,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,
        56,61,1,0,0,0,57,55,1,0,0,0,58,60,5,63,0,0,59,58,1,0,0,0,60,63,1,
        0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,61,1,0,0,0,64,
        65,5,0,0,1,65,1,1,0,0,0,66,74,3,10,5,0,67,74,3,22,11,0,68,74,3,28,
        14,0,69,74,3,38,19,0,70,74,3,8,4,0,71,74,3,4,2,0,72,74,3,6,3,0,73,
        66,1,0,0,0,73,67,1,0,0,0,73,68,1,0,0,0,73,69,1,0,0,0,73,70,1,0,0,
        0,73,71,1,0,0,0,73,72,1,0,0,0,74,3,1,0,0,0,75,76,5,47,0,0,76,77,
        5,56,0,0,77,78,5,49,0,0,78,79,5,50,0,0,79,80,5,1,0,0,80,81,5,57,
        0,0,81,82,5,2,0,0,82,83,5,57,0,0,83,84,5,3,0,0,84,85,5,4,0,0,85,
        87,5,63,0,0,86,88,3,2,1,0,87,86,1,0,0,0,88,89,1,0,0,0,89,87,1,0,
        0,0,89,90,1,0,0,0,90,5,1,0,0,0,91,92,5,48,0,0,92,93,3,12,6,0,93,
        94,5,4,0,0,94,96,5,63,0,0,95,97,3,2,1,0,96,95,1,0,0,0,97,98,1,0,
        0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,7,1,0,0,0,100,101,5,61,0,0,101,
        9,1,0,0,0,102,103,5,56,0,0,103,104,5,5,0,0,104,105,3,12,6,0,105,
        11,1,0,0,0,106,107,6,6,-1,0,107,108,5,1,0,0,108,109,3,12,6,0,109,
        110,5,3,0,0,110,124,1,0,0,0,111,112,5,46,0,0,112,113,5,11,0,0,113,
        114,7,0,0,0,114,115,5,1,0,0,115,116,3,20,10,0,116,117,5,3,0,0,117,
        124,1,0,0,0,118,124,3,14,7,0,119,124,3,18,9,0,120,124,5,57,0,0,121,
        124,5,56,0,0,122,124,5,60,0,0,123,106,1,0,0,0,123,111,1,0,0,0,123,
        118,1,0,0,0,123,119,1,0,0,0,123,120,1,0,0,0,123,121,1,0,0,0,123,
        122,1,0,0,0,124,133,1,0,0,0,125,126,10,9,0,0,126,127,7,1,0,0,127,
        132,3,12,6,10,128,129,10,8,0,0,129,130,7,2,0,0,130,132,3,12,6,9,
        131,125,1,0,0,0,131,128,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,
        133,134,1,0,0,0,134,13,1,0,0,0,135,133,1,0,0,0,136,137,5,18,0,0,
        137,142,3,16,8,0,138,139,5,2,0,0,139,141,3,16,8,0,140,138,1,0,0,
        0,141,144,1,0,0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,145,1,0,0,
        0,144,142,1,0,0,0,145,146,5,19,0,0,146,159,1,0,0,0,147,148,5,18,
        0,0,148,153,3,12,6,0,149,150,5,2,0,0,150,152,3,12,6,0,151,149,1,
        0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,153,154,1,0,0,0,154,156,1,
        0,0,0,155,153,1,0,0,0,156,157,5,19,0,0,157,159,1,0,0,0,158,136,1,
        0,0,0,158,147,1,0,0,0,159,15,1,0,0,0,160,161,5,18,0,0,161,166,3,
        12,6,0,162,163,5,2,0,0,163,165,3,12,6,0,164,162,1,0,0,0,165,168,
        1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,169,1,0,0,0,168,166,
        1,0,0,0,169,170,5,19,0,0,170,17,1,0,0,0,171,180,5,18,0,0,172,177,
        3,12,6,0,173,174,5,2,0,0,174,176,3,12,6,0,175,173,1,0,0,0,176,179,
        1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,181,1,0,0,0,179,177,
        1,0,0,0,180,172,1,0,0,0,180,181,1,0,0,0,181,182,1,0,0,0,182,183,
        5,19,0,0,183,19,1,0,0,0,184,189,3,12,6,0,185,186,5,2,0,0,186,188,
        3,12,6,0,187,185,1,0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,189,190,
        1,0,0,0,190,21,1,0,0,0,191,189,1,0,0,0,192,193,5,51,0,0,193,194,
        5,5,0,0,194,195,5,20,0,0,195,196,5,1,0,0,196,231,5,3,0,0,197,198,
        5,51,0,0,198,199,5,11,0,0,199,200,5,21,0,0,200,201,5,1,0,0,201,202,
        3,12,6,0,202,203,5,2,0,0,203,204,3,12,6,0,204,205,5,3,0,0,205,231,
        1,0,0,0,206,207,5,56,0,0,207,208,5,5,0,0,208,209,5,51,0,0,209,210,
        5,11,0,0,210,211,5,22,0,0,211,212,5,1,0,0,212,213,3,12,6,0,213,214,
        5,3,0,0,214,231,1,0,0,0,215,216,5,56,0,0,216,217,5,5,0,0,217,218,
        5,51,0,0,218,219,5,11,0,0,219,220,7,3,0,0,220,221,5,1,0,0,221,231,
        5,3,0,0,222,223,5,51,0,0,223,224,5,11,0,0,224,225,5,27,0,0,225,227,
        5,1,0,0,226,228,3,24,12,0,227,226,1,0,0,0,227,228,1,0,0,0,228,229,
        1,0,0,0,229,231,5,3,0,0,230,192,1,0,0,0,230,197,1,0,0,0,230,206,
        1,0,0,0,230,215,1,0,0,0,230,222,1,0,0,0,231,23,1,0,0,0,232,237,3,
        26,13,0,233,234,5,2,0,0,234,236,3,26,13,0,235,233,1,0,0,0,236,239,
        1,0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,25,1,0,0,0,239,237,1,
        0,0,0,240,241,5,28,0,0,241,242,5,5,0,0,242,262,5,57,0,0,243,244,
        5,29,0,0,244,245,5,5,0,0,245,262,5,57,0,0,246,247,5,30,0,0,247,248,
        5,5,0,0,248,262,5,57,0,0,249,250,5,31,0,0,250,251,5,5,0,0,251,262,
        5,60,0,0,252,253,5,32,0,0,253,254,5,5,0,0,254,262,5,60,0,0,255,256,
        5,33,0,0,256,257,5,5,0,0,257,262,5,60,0,0,258,259,5,34,0,0,259,260,
        5,5,0,0,260,262,7,4,0,0,261,240,1,0,0,0,261,243,1,0,0,0,261,246,
        1,0,0,0,261,249,1,0,0,0,261,252,1,0,0,0,261,255,1,0,0,0,261,258,
        1,0,0,0,262,27,1,0,0,0,263,264,5,52,0,0,264,265,5,5,0,0,265,266,
        5,35,0,0,266,267,5,1,0,0,267,268,3,30,15,0,268,269,5,3,0,0,269,309,
        1,0,0,0,270,271,5,52,0,0,271,272,5,11,0,0,272,273,5,21,0,0,273,274,
        5,1,0,0,274,275,3,12,6,0,275,276,5,2,0,0,276,279,3,12,6,0,277,278,
        5,2,0,0,278,280,3,34,17,0,279,277,1,0,0,0,279,280,1,0,0,0,280,281,
        1,0,0,0,281,282,5,3,0,0,282,309,1,0,0,0,283,284,5,56,0,0,284,285,
        5,5,0,0,285,286,5,52,0,0,286,287,5,11,0,0,287,288,5,22,0,0,288,289,
        5,1,0,0,289,290,3,12,6,0,290,291,5,3,0,0,291,309,1,0,0,0,292,293,
        5,56,0,0,293,294,5,5,0,0,294,295,5,52,0,0,295,296,5,11,0,0,296,297,
        5,36,0,0,297,298,5,1,0,0,298,299,3,12,6,0,299,300,5,2,0,0,300,301,
        3,12,6,0,301,302,5,3,0,0,302,309,1,0,0,0,303,304,5,52,0,0,304,305,
        5,11,0,0,305,306,5,37,0,0,306,307,5,1,0,0,307,309,5,3,0,0,308,263,
        1,0,0,0,308,270,1,0,0,0,308,283,1,0,0,0,308,292,1,0,0,0,308,303,
        1,0,0,0,309,29,1,0,0,0,310,315,3,32,16,0,311,312,5,2,0,0,312,314,
        3,32,16,0,313,311,1,0,0,0,314,317,1,0,0,0,315,313,1,0,0,0,315,316,
        1,0,0,0,316,31,1,0,0,0,317,315,1,0,0,0,318,319,5,38,0,0,319,320,
        5,5,0,0,320,334,3,18,9,0,321,322,5,39,0,0,322,323,5,5,0,0,323,334,
        5,60,0,0,324,325,5,40,0,0,325,326,5,5,0,0,326,334,5,57,0,0,327,328,
        5,41,0,0,328,329,5,5,0,0,329,334,5,57,0,0,330,331,5,42,0,0,331,332,
        5,5,0,0,332,334,5,57,0,0,333,318,1,0,0,0,333,321,1,0,0,0,333,324,
        1,0,0,0,333,327,1,0,0,0,333,330,1,0,0,0,334,33,1,0,0,0,335,340,3,
        36,18,0,336,337,5,2,0,0,337,339,3,36,18,0,338,336,1,0,0,0,339,342,
        1,0,0,0,340,338,1,0,0,0,340,341,1,0,0,0,341,35,1,0,0,0,342,340,1,
        0,0,0,343,344,5,43,0,0,344,345,5,5,0,0,345,353,5,57,0,0,346,347,
        5,44,0,0,347,348,5,5,0,0,348,353,5,57,0,0,349,350,5,45,0,0,350,351,
        5,5,0,0,351,353,7,4,0,0,352,343,1,0,0,0,352,346,1,0,0,0,352,349,
        1,0,0,0,353,37,1,0,0,0,354,355,5,53,0,0,355,356,5,1,0,0,356,357,
        3,12,6,0,357,358,5,3,0,0,358,371,1,0,0,0,359,360,5,53,0,0,360,361,
        5,1,0,0,361,366,5,60,0,0,362,363,5,2,0,0,363,365,3,12,6,0,364,362,
        1,0,0,0,365,368,1,0,0,0,366,364,1,0,0,0,366,367,1,0,0,0,367,369,
        1,0,0,0,368,366,1,0,0,0,369,371,5,3,0,0,370,354,1,0,0,0,370,359,
        1,0,0,0,371,39,1,0,0,0,29,43,50,55,61,73,89,98,123,131,133,142,153,
        158,166,177,180,189,227,230,237,261,279,308,315,333,340,352,366,
        370
    ]

class LenguajeDominioEspecificoParser ( Parser ):

    grammarFileName = "LenguajeDominioEspecifico.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "':'", "'='", "'*'", 
                     "'/'", "'%'", "'+'", "'-'", "'.'", "'suma'", "'resta'", 
                     "'multiplicar'", "'transpuesta'", "'determinante'", 
                     "'inversa'", "'['", "']'", "'RegresionLineal'", "'fit'", 
                     "'predict'", "'mse'", "'mae'", "'r2'", "'rmse'", "'plot'", 
                     "'width'", "'height'", "'left_margin'", "'point_char'", 
                     "'line_char'", "'title'", "'show_stats'", "'PerceptronMulticapa'", 
                     "'score'", "'plot_loss'", "'hidden_layers'", "'activation'", 
                     "'learning_rate'", "'max_iter'", "'random_state'", 
                     "'epochs'", "'batch_size'", "'verbose'", "'matriz'", 
                     "'for'", "'while'", "'in'", "'range'", "'regresion'", 
                     "'mlp'", "'print'", "'True'", "'False'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "MATRIZ", "FOR", "WHILE", 
                      "IN", "RANGE", "REGRESION", "MLP", "PRINT", "TRUE", 
                      "FALSE", "ID", "NUMBER", "ENTERO", "DECIMAL", "STRING", 
                      "COMENTARIO", "WS", "NEWLINE" ]

    RULE_programa = 0
    RULE_instruccion = 1
    RULE_buclefor = 2
    RULE_buclewhile = 3
    RULE_comentario = 4
    RULE_asignacion = 5
    RULE_expresion = 6
    RULE_matriz = 7
    RULE_fila = 8
    RULE_lista = 9
    RULE_parametrosMatriz = 10
    RULE_regresionLineal = 11
    RULE_parametrosPlot = 12
    RULE_parametroPlot = 13
    RULE_perceptronMulticapa = 14
    RULE_parametrosMLP = 15
    RULE_parametroMLP = 16
    RULE_parametrosEntrenamiento = 17
    RULE_parametroEntrenamiento = 18
    RULE_impresion = 19

    ruleNames =  [ "programa", "instruccion", "buclefor", "buclewhile", 
                   "comentario", "asignacion", "expresion", "matriz", "fila", 
                   "lista", "parametrosMatriz", "regresionLineal", "parametrosPlot", 
                   "parametroPlot", "perceptronMulticapa", "parametrosMLP", 
                   "parametroMLP", "parametrosEntrenamiento", "parametroEntrenamiento", 
                   "impresion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    MATRIZ=46
    FOR=47
    WHILE=48
    IN=49
    RANGE=50
    REGRESION=51
    MLP=52
    PRINT=53
    TRUE=54
    FALSE=55
    ID=56
    NUMBER=57
    ENTERO=58
    DECIMAL=59
    STRING=60
    COMENTARIO=61
    WS=62
    NEWLINE=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDominioEspecificoParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(LenguajeDominioEspecificoParser.InstruccionContext,i)


        def EOF(self):
            return self.getToken(LenguajeDominioEspecificoParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeDominioEspecificoParser.NEWLINE)
            else:
                return self.getToken(LenguajeDominioEspecificoParser.NEWLINE, i)

        def getRuleIndex(self):
            return LenguajeDominioEspecificoParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = LenguajeDominioEspecificoParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==63:
                self.state = 40
                self.match(LenguajeDominioEspecificoParser.NEWLINE)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.instruccion()
            self.state = 55
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 48 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 47
                        self.match(LenguajeDominioEspecificoParser.NEWLINE)
                        self.state = 50 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==63):
                            break

                    self.state = 52
                    self.instruccion() 
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==63:
                self.state = 58
                self.match(LenguajeDominioEspecificoParser.NEWLINE)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(LenguajeDominioEspecificoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(LenguajeDominioEspecificoParser.AsignacionContext,0)


        def regresionLineal(self):
            return self.getTypedRuleContext(LenguajeDominioEspecificoParser.RegresionLinealContext,0)


        def perceptronMulticapa(self):
            return self.getTypedRuleContext(LenguajeDominioEspecificoParser.PerceptronMulticapaContext,0)


        def impresion(self):
            return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ImpresionContext,0)


        def comentario(self):
            return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ComentarioContext,0)


        def buclefor(self):
            return self.getTypedRuleContext(LenguajeDominioEspecificoParser.BucleforContext,0)


        def buclewhile(self):
            return self.getTypedRuleContext(LenguajeDominioEspecificoParser.BuclewhileContext,0)


        def getRuleIndex(self):
            return LenguajeDominioEspecificoParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = LenguajeDominioEspecificoParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccion)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.regresionLineal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.perceptronMulticapa()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.impresion()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 70
                self.comentario()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 71
                self.buclefor()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 72
                self.buclewhile()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BucleforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(LenguajeDominioEspecificoParser.FOR, 0)

        def ID(self):
            return self.getToken(LenguajeDominioEspecificoParser.ID, 0)

        def IN(self):
            return self.getToken(LenguajeDominioEspecificoParser.IN, 0)

        def RANGE(self):
            return self.getToken(LenguajeDominioEspecificoParser.RANGE, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeDominioEspecificoParser.NUMBER)
            else:
                return self.getToken(LenguajeDominioEspecificoParser.NUMBER, i)

        def NEWLINE(self):
            return self.getToken(LenguajeDominioEspecificoParser.NEWLINE, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDominioEspecificoParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(LenguajeDominioEspecificoParser.InstruccionContext,i)


        def getRuleIndex(self):
            return LenguajeDominioEspecificoParser.RULE_buclefor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuclefor" ):
                listener.enterBuclefor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuclefor" ):
                listener.exitBuclefor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuclefor" ):
                return visitor.visitBuclefor(self)
            else:
                return visitor.visitChildren(self)




    def buclefor(self):

        localctx = LenguajeDominioEspecificoParser.BucleforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_buclefor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(LenguajeDominioEspecificoParser.FOR)
            self.state = 76
            self.match(LenguajeDominioEspecificoParser.ID)
            self.state = 77
            self.match(LenguajeDominioEspecificoParser.IN)
            self.state = 78
            self.match(LenguajeDominioEspecificoParser.RANGE)
            self.state = 79
            self.match(LenguajeDominioEspecificoParser.T__0)
            self.state = 80
            self.match(LenguajeDominioEspecificoParser.NUMBER)
            self.state = 81
            self.match(LenguajeDominioEspecificoParser.T__1)
            self.state = 82
            self.match(LenguajeDominioEspecificoParser.NUMBER)
            self.state = 83
            self.match(LenguajeDominioEspecificoParser.T__2)
            self.state = 84
            self.match(LenguajeDominioEspecificoParser.T__3)
            self.state = 85
            self.match(LenguajeDominioEspecificoParser.NEWLINE)
            self.state = 87 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 86
                    self.instruccion()

                else:
                    raise NoViableAltException(self)
                self.state = 89 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BuclewhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(LenguajeDominioEspecificoParser.WHILE, 0)

        def expresion(self):
            return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ExpresionContext,0)


        def NEWLINE(self):
            return self.getToken(LenguajeDominioEspecificoParser.NEWLINE, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDominioEspecificoParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(LenguajeDominioEspecificoParser.InstruccionContext,i)


        def getRuleIndex(self):
            return LenguajeDominioEspecificoParser.RULE_buclewhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuclewhile" ):
                listener.enterBuclewhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuclewhile" ):
                listener.exitBuclewhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuclewhile" ):
                return visitor.visitBuclewhile(self)
            else:
                return visitor.visitChildren(self)




    def buclewhile(self):

        localctx = LenguajeDominioEspecificoParser.BuclewhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_buclewhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(LenguajeDominioEspecificoParser.WHILE)
            self.state = 92
            self.expresion(0)
            self.state = 93
            self.match(LenguajeDominioEspecificoParser.T__3)
            self.state = 94
            self.match(LenguajeDominioEspecificoParser.NEWLINE)
            self.state = 96 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 95
                    self.instruccion()

                else:
                    raise NoViableAltException(self)
                self.state = 98 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComentarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMENTARIO(self):
            return self.getToken(LenguajeDominioEspecificoParser.COMENTARIO, 0)

        def getRuleIndex(self):
            return LenguajeDominioEspecificoParser.RULE_comentario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComentario" ):
                listener.enterComentario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComentario" ):
                listener.exitComentario(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComentario" ):
                return visitor.visitComentario(self)
            else:
                return visitor.visitChildren(self)




    def comentario(self):

        localctx = LenguajeDominioEspecificoParser.ComentarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comentario)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(LenguajeDominioEspecificoParser.COMENTARIO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LenguajeDominioEspecificoParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ExpresionContext,0)


        def getRuleIndex(self):
            return LenguajeDominioEspecificoParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = LenguajeDominioEspecificoParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(LenguajeDominioEspecificoParser.ID)
            self.state = 103
            self.match(LenguajeDominioEspecificoParser.T__4)
            self.state = 104
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LenguajeDominioEspecificoParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExpresionListaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lista(self):
            return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ListaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionLista" ):
                listener.enterExpresionLista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionLista" ):
                listener.exitExpresionLista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionLista" ):
                return visitor.visitExpresionLista(self)
            else:
                return visitor.visitChildren(self)


    class ExpresionNumeroContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(LenguajeDominioEspecificoParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionNumero" ):
                listener.enterExpresionNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionNumero" ):
                listener.exitExpresionNumero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionNumero" ):
                return visitor.visitExpresionNumero(self)
            else:
                return visitor.visitChildren(self)


    class ExpresionParentesisContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionParentesis" ):
                listener.enterExpresionParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionParentesis" ):
                listener.exitExpresionParentesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionParentesis" ):
                return visitor.visitExpresionParentesis(self)
            else:
                return visitor.visitChildren(self)


    class OperacionSumaRestaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDominioEspecificoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionSumaResta" ):
                listener.enterOperacionSumaResta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionSumaResta" ):
                listener.exitOperacionSumaResta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionSumaResta" ):
                return visitor.visitOperacionSumaResta(self)
            else:
                return visitor.visitChildren(self)


    class ExpresionVariableContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LenguajeDominioEspecificoParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionVariable" ):
                listener.enterExpresionVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionVariable" ):
                listener.exitExpresionVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionVariable" ):
                return visitor.visitExpresionVariable(self)
            else:
                return visitor.visitChildren(self)


    class OperacionMatrizExprContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.ExpresionContext
            super().__init__(parser)
            self.operacion = None # Token
            self.copyFrom(ctx)

        def MATRIZ(self):
            return self.getToken(LenguajeDominioEspecificoParser.MATRIZ, 0)
        def parametrosMatriz(self):
            return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ParametrosMatrizContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionMatrizExpr" ):
                listener.enterOperacionMatrizExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionMatrizExpr" ):
                listener.exitOperacionMatrizExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionMatrizExpr" ):
                return visitor.visitOperacionMatrizExpr(self)
            else:
                return visitor.visitChildren(self)


    class ExpresionStringContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(LenguajeDominioEspecificoParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionString" ):
                listener.enterExpresionString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionString" ):
                listener.exitExpresionString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionString" ):
                return visitor.visitExpresionString(self)
            else:
                return visitor.visitChildren(self)


    class ExpresionMatrizContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def matriz(self):
            return self.getTypedRuleContext(LenguajeDominioEspecificoParser.MatrizContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionMatriz" ):
                listener.enterExpresionMatriz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionMatriz" ):
                listener.exitExpresionMatriz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionMatriz" ):
                return visitor.visitExpresionMatriz(self)
            else:
                return visitor.visitChildren(self)


    class OperacionMultDivContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDominioEspecificoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionMultDiv" ):
                listener.enterOperacionMultDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionMultDiv" ):
                listener.exitOperacionMultDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionMultDiv" ):
                return visitor.visitOperacionMultDiv(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LenguajeDominioEspecificoParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = LenguajeDominioEspecificoParser.ExpresionParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 107
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 108
                self.expresion(0)
                self.state = 109
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass

            elif la_ == 2:
                localctx = LenguajeDominioEspecificoParser.OperacionMatrizExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 111
                self.match(LenguajeDominioEspecificoParser.MATRIZ)
                self.state = 112
                self.match(LenguajeDominioEspecificoParser.T__10)
                self.state = 113
                localctx.operacion = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                    localctx.operacion = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 114
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 115
                self.parametrosMatriz()
                self.state = 116
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass

            elif la_ == 3:
                localctx = LenguajeDominioEspecificoParser.ExpresionMatrizContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 118
                self.matriz()
                pass

            elif la_ == 4:
                localctx = LenguajeDominioEspecificoParser.ExpresionListaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 119
                self.lista()
                pass

            elif la_ == 5:
                localctx = LenguajeDominioEspecificoParser.ExpresionNumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 120
                self.match(LenguajeDominioEspecificoParser.NUMBER)
                pass

            elif la_ == 6:
                localctx = LenguajeDominioEspecificoParser.ExpresionVariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 121
                self.match(LenguajeDominioEspecificoParser.ID)
                pass

            elif la_ == 7:
                localctx = LenguajeDominioEspecificoParser.ExpresionStringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 122
                self.match(LenguajeDominioEspecificoParser.STRING)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 133
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 131
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = LenguajeDominioEspecificoParser.OperacionMultDivContext(self, LenguajeDominioEspecificoParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 125
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 126
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 127
                        self.expresion(10)
                        pass

                    elif la_ == 2:
                        localctx = LenguajeDominioEspecificoParser.OperacionSumaRestaContext(self, LenguajeDominioEspecificoParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 128
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 129
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 130
                        self.expresion(9)
                        pass

             
                self.state = 135
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MatrizContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LenguajeDominioEspecificoParser.RULE_matriz

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MatrizMultiFilaContext(MatrizContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.MatrizContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fila(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDominioEspecificoParser.FilaContext)
            else:
                return self.getTypedRuleContext(LenguajeDominioEspecificoParser.FilaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrizMultiFila" ):
                listener.enterMatrizMultiFila(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrizMultiFila" ):
                listener.exitMatrizMultiFila(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrizMultiFila" ):
                return visitor.visitMatrizMultiFila(self)
            else:
                return visitor.visitChildren(self)


    class MatrizUnidimensionalContext(MatrizContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.MatrizContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDominioEspecificoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrizUnidimensional" ):
                listener.enterMatrizUnidimensional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrizUnidimensional" ):
                listener.exitMatrizUnidimensional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrizUnidimensional" ):
                return visitor.visitMatrizUnidimensional(self)
            else:
                return visitor.visitChildren(self)



    def matriz(self):

        localctx = LenguajeDominioEspecificoParser.MatrizContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_matriz)
        self._la = 0 # Token type
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = LenguajeDominioEspecificoParser.MatrizMultiFilaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(LenguajeDominioEspecificoParser.T__17)
                self.state = 137
                self.fila()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 138
                    self.match(LenguajeDominioEspecificoParser.T__1)
                    self.state = 139
                    self.fila()
                    self.state = 144
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 145
                self.match(LenguajeDominioEspecificoParser.T__18)
                pass

            elif la_ == 2:
                localctx = LenguajeDominioEspecificoParser.MatrizUnidimensionalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(LenguajeDominioEspecificoParser.T__17)
                self.state = 148
                self.expresion(0)
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 149
                    self.match(LenguajeDominioEspecificoParser.T__1)
                    self.state = 150
                    self.expresion(0)
                    self.state = 155
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 156
                self.match(LenguajeDominioEspecificoParser.T__18)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDominioEspecificoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ExpresionContext,i)


        def getRuleIndex(self):
            return LenguajeDominioEspecificoParser.RULE_fila

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFila" ):
                listener.enterFila(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFila" ):
                listener.exitFila(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFila" ):
                return visitor.visitFila(self)
            else:
                return visitor.visitChildren(self)




    def fila(self):

        localctx = LenguajeDominioEspecificoParser.FilaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_fila)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(LenguajeDominioEspecificoParser.T__17)
            self.state = 161
            self.expresion(0)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 162
                self.match(LenguajeDominioEspecificoParser.T__1)
                self.state = 163
                self.expresion(0)
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 169
            self.match(LenguajeDominioEspecificoParser.T__18)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDominioEspecificoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ExpresionContext,i)


        def getRuleIndex(self):
            return LenguajeDominioEspecificoParser.RULE_lista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista" ):
                listener.enterLista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista" ):
                listener.exitLista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista" ):
                return visitor.visitLista(self)
            else:
                return visitor.visitChildren(self)




    def lista(self):

        localctx = LenguajeDominioEspecificoParser.ListaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(LenguajeDominioEspecificoParser.T__17)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1369164655465070594) != 0):
                self.state = 172
                self.expresion(0)
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 173
                    self.match(LenguajeDominioEspecificoParser.T__1)
                    self.state = 174
                    self.expresion(0)
                    self.state = 179
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 182
            self.match(LenguajeDominioEspecificoParser.T__18)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosMatrizContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDominioEspecificoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ExpresionContext,i)


        def getRuleIndex(self):
            return LenguajeDominioEspecificoParser.RULE_parametrosMatriz

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametrosMatriz" ):
                listener.enterParametrosMatriz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametrosMatriz" ):
                listener.exitParametrosMatriz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametrosMatriz" ):
                return visitor.visitParametrosMatriz(self)
            else:
                return visitor.visitChildren(self)




    def parametrosMatriz(self):

        localctx = LenguajeDominioEspecificoParser.ParametrosMatrizContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parametrosMatriz)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.expresion(0)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 185
                self.match(LenguajeDominioEspecificoParser.T__1)
                self.state = 186
                self.expresion(0)
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegresionLinealContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LenguajeDominioEspecificoParser.RULE_regresionLineal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class GraficarRegresionContext(RegresionLinealContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.RegresionLinealContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REGRESION(self):
            return self.getToken(LenguajeDominioEspecificoParser.REGRESION, 0)
        def parametrosPlot(self):
            return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ParametrosPlotContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraficarRegresion" ):
                listener.enterGraficarRegresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraficarRegresion" ):
                listener.exitGraficarRegresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGraficarRegresion" ):
                return visitor.visitGraficarRegresion(self)
            else:
                return visitor.visitChildren(self)


    class EntrenarRegresionContext(RegresionLinealContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.RegresionLinealContext
            super().__init__(parser)
            self.x = None # ExpresionContext
            self.y = None # ExpresionContext
            self.copyFrom(ctx)

        def REGRESION(self):
            return self.getToken(LenguajeDominioEspecificoParser.REGRESION, 0)
        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDominioEspecificoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntrenarRegresion" ):
                listener.enterEntrenarRegresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntrenarRegresion" ):
                listener.exitEntrenarRegresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntrenarRegresion" ):
                return visitor.visitEntrenarRegresion(self)
            else:
                return visitor.visitChildren(self)


    class PredecirRegresionContext(RegresionLinealContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.RegresionLinealContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LenguajeDominioEspecificoParser.ID, 0)
        def REGRESION(self):
            return self.getToken(LenguajeDominioEspecificoParser.REGRESION, 0)
        def expresion(self):
            return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredecirRegresion" ):
                listener.enterPredecirRegresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredecirRegresion" ):
                listener.exitPredecirRegresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredecirRegresion" ):
                return visitor.visitPredecirRegresion(self)
            else:
                return visitor.visitChildren(self)


    class ObtenerMetricaRegresionContext(RegresionLinealContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.RegresionLinealContext
            super().__init__(parser)
            self.metrica = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LenguajeDominioEspecificoParser.ID, 0)
        def REGRESION(self):
            return self.getToken(LenguajeDominioEspecificoParser.REGRESION, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObtenerMetricaRegresion" ):
                listener.enterObtenerMetricaRegresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObtenerMetricaRegresion" ):
                listener.exitObtenerMetricaRegresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObtenerMetricaRegresion" ):
                return visitor.visitObtenerMetricaRegresion(self)
            else:
                return visitor.visitChildren(self)


    class CrearRegresionContext(RegresionLinealContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.RegresionLinealContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REGRESION(self):
            return self.getToken(LenguajeDominioEspecificoParser.REGRESION, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCrearRegresion" ):
                listener.enterCrearRegresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCrearRegresion" ):
                listener.exitCrearRegresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCrearRegresion" ):
                return visitor.visitCrearRegresion(self)
            else:
                return visitor.visitChildren(self)



    def regresionLineal(self):

        localctx = LenguajeDominioEspecificoParser.RegresionLinealContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_regresionLineal)
        self._la = 0 # Token type
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = LenguajeDominioEspecificoParser.CrearRegresionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.match(LenguajeDominioEspecificoParser.REGRESION)
                self.state = 193
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 194
                self.match(LenguajeDominioEspecificoParser.T__19)
                self.state = 195
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 196
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass

            elif la_ == 2:
                localctx = LenguajeDominioEspecificoParser.EntrenarRegresionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.match(LenguajeDominioEspecificoParser.REGRESION)
                self.state = 198
                self.match(LenguajeDominioEspecificoParser.T__10)
                self.state = 199
                self.match(LenguajeDominioEspecificoParser.T__20)
                self.state = 200
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 201
                localctx.x = self.expresion(0)
                self.state = 202
                self.match(LenguajeDominioEspecificoParser.T__1)
                self.state = 203
                localctx.y = self.expresion(0)
                self.state = 204
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass

            elif la_ == 3:
                localctx = LenguajeDominioEspecificoParser.PredecirRegresionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 206
                self.match(LenguajeDominioEspecificoParser.ID)
                self.state = 207
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 208
                self.match(LenguajeDominioEspecificoParser.REGRESION)
                self.state = 209
                self.match(LenguajeDominioEspecificoParser.T__10)
                self.state = 210
                self.match(LenguajeDominioEspecificoParser.T__21)
                self.state = 211
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 212
                self.expresion(0)
                self.state = 213
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass

            elif la_ == 4:
                localctx = LenguajeDominioEspecificoParser.ObtenerMetricaRegresionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 215
                self.match(LenguajeDominioEspecificoParser.ID)
                self.state = 216
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 217
                self.match(LenguajeDominioEspecificoParser.REGRESION)
                self.state = 218
                self.match(LenguajeDominioEspecificoParser.T__10)
                self.state = 219
                localctx.metrica = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0)):
                    localctx.metrica = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 220
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 221
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass

            elif la_ == 5:
                localctx = LenguajeDominioEspecificoParser.GraficarRegresionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 222
                self.match(LenguajeDominioEspecificoParser.REGRESION)
                self.state = 223
                self.match(LenguajeDominioEspecificoParser.T__10)
                self.state = 224
                self.match(LenguajeDominioEspecificoParser.T__26)
                self.state = 225
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34091302912) != 0):
                    self.state = 226
                    self.parametrosPlot()


                self.state = 229
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosPlotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametroPlot(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDominioEspecificoParser.ParametroPlotContext)
            else:
                return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ParametroPlotContext,i)


        def getRuleIndex(self):
            return LenguajeDominioEspecificoParser.RULE_parametrosPlot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametrosPlot" ):
                listener.enterParametrosPlot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametrosPlot" ):
                listener.exitParametrosPlot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametrosPlot" ):
                return visitor.visitParametrosPlot(self)
            else:
                return visitor.visitChildren(self)




    def parametrosPlot(self):

        localctx = LenguajeDominioEspecificoParser.ParametrosPlotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parametrosPlot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.parametroPlot()
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 233
                self.match(LenguajeDominioEspecificoParser.T__1)
                self.state = 234
                self.parametroPlot()
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroPlotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(LenguajeDominioEspecificoParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(LenguajeDominioEspecificoParser.STRING, 0)

        def TRUE(self):
            return self.getToken(LenguajeDominioEspecificoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(LenguajeDominioEspecificoParser.FALSE, 0)

        def getRuleIndex(self):
            return LenguajeDominioEspecificoParser.RULE_parametroPlot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametroPlot" ):
                listener.enterParametroPlot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametroPlot" ):
                listener.exitParametroPlot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametroPlot" ):
                return visitor.visitParametroPlot(self)
            else:
                return visitor.visitChildren(self)




    def parametroPlot(self):

        localctx = LenguajeDominioEspecificoParser.ParametroPlotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parametroPlot)
        self._la = 0 # Token type
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(LenguajeDominioEspecificoParser.T__27)
                self.state = 241
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 242
                self.match(LenguajeDominioEspecificoParser.NUMBER)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.match(LenguajeDominioEspecificoParser.T__28)
                self.state = 244
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 245
                self.match(LenguajeDominioEspecificoParser.NUMBER)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 246
                self.match(LenguajeDominioEspecificoParser.T__29)
                self.state = 247
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 248
                self.match(LenguajeDominioEspecificoParser.NUMBER)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 4)
                self.state = 249
                self.match(LenguajeDominioEspecificoParser.T__30)
                self.state = 250
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 251
                self.match(LenguajeDominioEspecificoParser.STRING)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 5)
                self.state = 252
                self.match(LenguajeDominioEspecificoParser.T__31)
                self.state = 253
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 254
                self.match(LenguajeDominioEspecificoParser.STRING)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 6)
                self.state = 255
                self.match(LenguajeDominioEspecificoParser.T__32)
                self.state = 256
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 257
                self.match(LenguajeDominioEspecificoParser.STRING)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 7)
                self.state = 258
                self.match(LenguajeDominioEspecificoParser.T__33)
                self.state = 259
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 260
                _la = self._input.LA(1)
                if not(_la==54 or _la==55):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PerceptronMulticapaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LenguajeDominioEspecificoParser.RULE_perceptronMulticapa

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CrearMLPContext(PerceptronMulticapaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.PerceptronMulticapaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MLP(self):
            return self.getToken(LenguajeDominioEspecificoParser.MLP, 0)
        def parametrosMLP(self):
            return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ParametrosMLPContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCrearMLP" ):
                listener.enterCrearMLP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCrearMLP" ):
                listener.exitCrearMLP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCrearMLP" ):
                return visitor.visitCrearMLP(self)
            else:
                return visitor.visitChildren(self)


    class EntrenarMLPContext(PerceptronMulticapaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.PerceptronMulticapaContext
            super().__init__(parser)
            self.x = None # ExpresionContext
            self.y = None # ExpresionContext
            self.copyFrom(ctx)

        def MLP(self):
            return self.getToken(LenguajeDominioEspecificoParser.MLP, 0)
        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDominioEspecificoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ExpresionContext,i)

        def parametrosEntrenamiento(self):
            return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ParametrosEntrenamientoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntrenarMLP" ):
                listener.enterEntrenarMLP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntrenarMLP" ):
                listener.exitEntrenarMLP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntrenarMLP" ):
                return visitor.visitEntrenarMLP(self)
            else:
                return visitor.visitChildren(self)


    class GraficarPerdidaMLPContext(PerceptronMulticapaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.PerceptronMulticapaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MLP(self):
            return self.getToken(LenguajeDominioEspecificoParser.MLP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraficarPerdidaMLP" ):
                listener.enterGraficarPerdidaMLP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraficarPerdidaMLP" ):
                listener.exitGraficarPerdidaMLP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGraficarPerdidaMLP" ):
                return visitor.visitGraficarPerdidaMLP(self)
            else:
                return visitor.visitChildren(self)


    class PredecirMLPContext(PerceptronMulticapaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.PerceptronMulticapaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LenguajeDominioEspecificoParser.ID, 0)
        def MLP(self):
            return self.getToken(LenguajeDominioEspecificoParser.MLP, 0)
        def expresion(self):
            return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredecirMLP" ):
                listener.enterPredecirMLP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredecirMLP" ):
                listener.exitPredecirMLP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredecirMLP" ):
                return visitor.visitPredecirMLP(self)
            else:
                return visitor.visitChildren(self)


    class EvaluarMLPContext(PerceptronMulticapaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.PerceptronMulticapaContext
            super().__init__(parser)
            self.x = None # ExpresionContext
            self.y = None # ExpresionContext
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LenguajeDominioEspecificoParser.ID, 0)
        def MLP(self):
            return self.getToken(LenguajeDominioEspecificoParser.MLP, 0)
        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDominioEspecificoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvaluarMLP" ):
                listener.enterEvaluarMLP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvaluarMLP" ):
                listener.exitEvaluarMLP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvaluarMLP" ):
                return visitor.visitEvaluarMLP(self)
            else:
                return visitor.visitChildren(self)



    def perceptronMulticapa(self):

        localctx = LenguajeDominioEspecificoParser.PerceptronMulticapaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_perceptronMulticapa)
        self._la = 0 # Token type
        try:
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                localctx = LenguajeDominioEspecificoParser.CrearMLPContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.match(LenguajeDominioEspecificoParser.MLP)
                self.state = 264
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 265
                self.match(LenguajeDominioEspecificoParser.T__34)
                self.state = 266
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 267
                self.parametrosMLP()
                self.state = 268
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass

            elif la_ == 2:
                localctx = LenguajeDominioEspecificoParser.EntrenarMLPContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.match(LenguajeDominioEspecificoParser.MLP)
                self.state = 271
                self.match(LenguajeDominioEspecificoParser.T__10)
                self.state = 272
                self.match(LenguajeDominioEspecificoParser.T__20)
                self.state = 273
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 274
                localctx.x = self.expresion(0)
                self.state = 275
                self.match(LenguajeDominioEspecificoParser.T__1)
                self.state = 276
                localctx.y = self.expresion(0)
                self.state = 279
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 277
                    self.match(LenguajeDominioEspecificoParser.T__1)
                    self.state = 278
                    self.parametrosEntrenamiento()


                self.state = 281
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass

            elif la_ == 3:
                localctx = LenguajeDominioEspecificoParser.PredecirMLPContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 283
                self.match(LenguajeDominioEspecificoParser.ID)
                self.state = 284
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 285
                self.match(LenguajeDominioEspecificoParser.MLP)
                self.state = 286
                self.match(LenguajeDominioEspecificoParser.T__10)
                self.state = 287
                self.match(LenguajeDominioEspecificoParser.T__21)
                self.state = 288
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 289
                self.expresion(0)
                self.state = 290
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass

            elif la_ == 4:
                localctx = LenguajeDominioEspecificoParser.EvaluarMLPContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 292
                self.match(LenguajeDominioEspecificoParser.ID)
                self.state = 293
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 294
                self.match(LenguajeDominioEspecificoParser.MLP)
                self.state = 295
                self.match(LenguajeDominioEspecificoParser.T__10)
                self.state = 296
                self.match(LenguajeDominioEspecificoParser.T__35)
                self.state = 297
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 298
                localctx.x = self.expresion(0)
                self.state = 299
                self.match(LenguajeDominioEspecificoParser.T__1)
                self.state = 300
                localctx.y = self.expresion(0)
                self.state = 301
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass

            elif la_ == 5:
                localctx = LenguajeDominioEspecificoParser.GraficarPerdidaMLPContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 303
                self.match(LenguajeDominioEspecificoParser.MLP)
                self.state = 304
                self.match(LenguajeDominioEspecificoParser.T__10)
                self.state = 305
                self.match(LenguajeDominioEspecificoParser.T__36)
                self.state = 306
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 307
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosMLPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametroMLP(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDominioEspecificoParser.ParametroMLPContext)
            else:
                return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ParametroMLPContext,i)


        def getRuleIndex(self):
            return LenguajeDominioEspecificoParser.RULE_parametrosMLP

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametrosMLP" ):
                listener.enterParametrosMLP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametrosMLP" ):
                listener.exitParametrosMLP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametrosMLP" ):
                return visitor.visitParametrosMLP(self)
            else:
                return visitor.visitChildren(self)




    def parametrosMLP(self):

        localctx = LenguajeDominioEspecificoParser.ParametrosMLPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_parametrosMLP)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.parametroMLP()
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 311
                self.match(LenguajeDominioEspecificoParser.T__1)
                self.state = 312
                self.parametroMLP()
                self.state = 317
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroMLPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lista(self):
            return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ListaContext,0)


        def STRING(self):
            return self.getToken(LenguajeDominioEspecificoParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(LenguajeDominioEspecificoParser.NUMBER, 0)

        def getRuleIndex(self):
            return LenguajeDominioEspecificoParser.RULE_parametroMLP

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametroMLP" ):
                listener.enterParametroMLP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametroMLP" ):
                listener.exitParametroMLP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametroMLP" ):
                return visitor.visitParametroMLP(self)
            else:
                return visitor.visitChildren(self)




    def parametroMLP(self):

        localctx = LenguajeDominioEspecificoParser.ParametroMLPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_parametroMLP)
        try:
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(LenguajeDominioEspecificoParser.T__37)
                self.state = 319
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 320
                self.lista()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.match(LenguajeDominioEspecificoParser.T__38)
                self.state = 322
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 323
                self.match(LenguajeDominioEspecificoParser.STRING)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 3)
                self.state = 324
                self.match(LenguajeDominioEspecificoParser.T__39)
                self.state = 325
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 326
                self.match(LenguajeDominioEspecificoParser.NUMBER)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 4)
                self.state = 327
                self.match(LenguajeDominioEspecificoParser.T__40)
                self.state = 328
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 329
                self.match(LenguajeDominioEspecificoParser.NUMBER)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 5)
                self.state = 330
                self.match(LenguajeDominioEspecificoParser.T__41)
                self.state = 331
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 332
                self.match(LenguajeDominioEspecificoParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosEntrenamientoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametroEntrenamiento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDominioEspecificoParser.ParametroEntrenamientoContext)
            else:
                return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ParametroEntrenamientoContext,i)


        def getRuleIndex(self):
            return LenguajeDominioEspecificoParser.RULE_parametrosEntrenamiento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametrosEntrenamiento" ):
                listener.enterParametrosEntrenamiento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametrosEntrenamiento" ):
                listener.exitParametrosEntrenamiento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametrosEntrenamiento" ):
                return visitor.visitParametrosEntrenamiento(self)
            else:
                return visitor.visitChildren(self)




    def parametrosEntrenamiento(self):

        localctx = LenguajeDominioEspecificoParser.ParametrosEntrenamientoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parametrosEntrenamiento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.parametroEntrenamiento()
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 336
                self.match(LenguajeDominioEspecificoParser.T__1)
                self.state = 337
                self.parametroEntrenamiento()
                self.state = 342
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroEntrenamientoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(LenguajeDominioEspecificoParser.NUMBER, 0)

        def TRUE(self):
            return self.getToken(LenguajeDominioEspecificoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(LenguajeDominioEspecificoParser.FALSE, 0)

        def getRuleIndex(self):
            return LenguajeDominioEspecificoParser.RULE_parametroEntrenamiento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametroEntrenamiento" ):
                listener.enterParametroEntrenamiento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametroEntrenamiento" ):
                listener.exitParametroEntrenamiento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametroEntrenamiento" ):
                return visitor.visitParametroEntrenamiento(self)
            else:
                return visitor.visitChildren(self)




    def parametroEntrenamiento(self):

        localctx = LenguajeDominioEspecificoParser.ParametroEntrenamientoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_parametroEntrenamiento)
        self._la = 0 # Token type
        try:
            self.state = 352
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.match(LenguajeDominioEspecificoParser.T__42)
                self.state = 344
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 345
                self.match(LenguajeDominioEspecificoParser.NUMBER)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.match(LenguajeDominioEspecificoParser.T__43)
                self.state = 347
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 348
                self.match(LenguajeDominioEspecificoParser.NUMBER)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 3)
                self.state = 349
                self.match(LenguajeDominioEspecificoParser.T__44)
                self.state = 350
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 351
                _la = self._input.LA(1)
                if not(_la==54 or _la==55):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(LenguajeDominioEspecificoParser.PRINT, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDominioEspecificoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ExpresionContext,i)


        def STRING(self):
            return self.getToken(LenguajeDominioEspecificoParser.STRING, 0)

        def getRuleIndex(self):
            return LenguajeDominioEspecificoParser.RULE_impresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImpresion" ):
                listener.enterImpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImpresion" ):
                listener.exitImpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImpresion" ):
                return visitor.visitImpresion(self)
            else:
                return visitor.visitChildren(self)




    def impresion(self):

        localctx = LenguajeDominioEspecificoParser.ImpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_impresion)
        self._la = 0 # Token type
        try:
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.match(LenguajeDominioEspecificoParser.PRINT)
                self.state = 355
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 356
                self.expresion(0)
                self.state = 357
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.match(LenguajeDominioEspecificoParser.PRINT)
                self.state = 360
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 361
                self.match(LenguajeDominioEspecificoParser.STRING)
                self.state = 366
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 362
                    self.match(LenguajeDominioEspecificoParser.T__1)
                    self.state = 363
                    self.expresion(0)
                    self.state = 368
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 369
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         




