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
        4,1,69,376,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,1,0,4,0,49,8,0,11,0,12,0,50,1,0,
        5,0,54,8,0,10,0,12,0,57,9,0,1,0,5,0,60,8,0,10,0,12,0,63,9,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,74,8,1,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,88,8,2,11,2,12,2,89,1,3,1,3,1,3,1,
        3,1,3,4,3,97,8,3,11,3,12,3,98,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,124,
        8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,135,8,6,10,6,12,6,138,
        9,6,1,7,1,7,1,7,1,7,5,7,144,8,7,10,7,12,7,147,9,7,1,7,1,7,1,7,1,
        7,1,7,1,7,5,7,155,8,7,10,7,12,7,158,9,7,1,7,1,7,3,7,162,8,7,1,8,
        1,8,1,8,1,8,5,8,168,8,8,10,8,12,8,171,9,8,1,8,1,8,1,9,1,9,1,9,1,
        9,5,9,179,8,9,10,9,12,9,182,9,9,3,9,184,8,9,1,9,1,9,1,10,1,10,1,
        10,5,10,191,8,10,10,10,12,10,194,9,10,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,3,11,231,8,11,1,11,3,11,234,8,11,1,12,1,12,1,12,
        5,12,239,8,12,10,12,12,12,242,9,12,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,3,13,265,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,283,8,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,
        312,8,14,1,15,1,15,1,15,5,15,317,8,15,10,15,12,15,320,9,15,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,3,16,337,8,16,1,17,1,17,1,17,5,17,342,8,17,10,17,12,17,345,
        9,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,356,8,18,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,5,19,368,8,19,
        10,19,12,19,371,9,19,1,19,3,19,374,8,19,1,19,0,1,12,20,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,0,6,1,0,18,23,1,0,6,
        8,1,0,9,14,1,0,15,16,1,0,29,32,1,0,60,61,410,0,43,1,0,0,0,2,73,1,
        0,0,0,4,75,1,0,0,0,6,91,1,0,0,0,8,100,1,0,0,0,10,102,1,0,0,0,12,
        123,1,0,0,0,14,161,1,0,0,0,16,163,1,0,0,0,18,174,1,0,0,0,20,187,
        1,0,0,0,22,233,1,0,0,0,24,235,1,0,0,0,26,264,1,0,0,0,28,311,1,0,
        0,0,30,313,1,0,0,0,32,336,1,0,0,0,34,338,1,0,0,0,36,355,1,0,0,0,
        38,373,1,0,0,0,40,42,5,69,0,0,41,40,1,0,0,0,42,45,1,0,0,0,43,41,
        1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,46,55,3,2,1,0,
        47,49,5,69,0,0,48,47,1,0,0,0,49,50,1,0,0,0,50,48,1,0,0,0,50,51,1,
        0,0,0,51,52,1,0,0,0,52,54,3,2,1,0,53,48,1,0,0,0,54,57,1,0,0,0,55,
        53,1,0,0,0,55,56,1,0,0,0,56,61,1,0,0,0,57,55,1,0,0,0,58,60,5,69,
        0,0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,
        1,0,0,0,63,61,1,0,0,0,64,65,5,0,0,1,65,1,1,0,0,0,66,74,3,10,5,0,
        67,74,3,22,11,0,68,74,3,28,14,0,69,74,3,38,19,0,70,74,3,8,4,0,71,
        74,3,4,2,0,72,74,3,6,3,0,73,66,1,0,0,0,73,67,1,0,0,0,73,68,1,0,0,
        0,73,69,1,0,0,0,73,70,1,0,0,0,73,71,1,0,0,0,73,72,1,0,0,0,74,3,1,
        0,0,0,75,76,5,53,0,0,76,77,5,62,0,0,77,78,5,55,0,0,78,79,5,56,0,
        0,79,80,5,1,0,0,80,81,5,63,0,0,81,82,5,2,0,0,82,83,5,63,0,0,83,84,
        5,3,0,0,84,85,5,4,0,0,85,87,5,69,0,0,86,88,3,2,1,0,87,86,1,0,0,0,
        88,89,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,5,1,0,0,0,91,92,5,54,
        0,0,92,93,3,12,6,0,93,94,5,4,0,0,94,96,5,69,0,0,95,97,3,2,1,0,96,
        95,1,0,0,0,97,98,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,7,1,0,0,
        0,100,101,5,67,0,0,101,9,1,0,0,0,102,103,5,62,0,0,103,104,5,5,0,
        0,104,105,3,12,6,0,105,11,1,0,0,0,106,107,6,6,-1,0,107,108,5,1,0,
        0,108,109,3,12,6,0,109,110,5,3,0,0,110,124,1,0,0,0,111,112,5,52,
        0,0,112,113,5,17,0,0,113,114,7,0,0,0,114,115,5,1,0,0,115,116,3,20,
        10,0,116,117,5,3,0,0,117,124,1,0,0,0,118,124,3,14,7,0,119,124,3,
        18,9,0,120,124,5,63,0,0,121,124,5,62,0,0,122,124,5,66,0,0,123,106,
        1,0,0,0,123,111,1,0,0,0,123,118,1,0,0,0,123,119,1,0,0,0,123,120,
        1,0,0,0,123,121,1,0,0,0,123,122,1,0,0,0,124,136,1,0,0,0,125,126,
        10,10,0,0,126,127,7,1,0,0,127,135,3,12,6,11,128,129,10,9,0,0,129,
        130,7,2,0,0,130,135,3,12,6,10,131,132,10,8,0,0,132,133,7,3,0,0,133,
        135,3,12,6,9,134,125,1,0,0,0,134,128,1,0,0,0,134,131,1,0,0,0,135,
        138,1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,13,1,0,0,0,138,136,
        1,0,0,0,139,140,5,24,0,0,140,145,3,16,8,0,141,142,5,2,0,0,142,144,
        3,16,8,0,143,141,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,
        1,0,0,0,146,148,1,0,0,0,147,145,1,0,0,0,148,149,5,25,0,0,149,162,
        1,0,0,0,150,151,5,24,0,0,151,156,3,12,6,0,152,153,5,2,0,0,153,155,
        3,12,6,0,154,152,1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,156,157,
        1,0,0,0,157,159,1,0,0,0,158,156,1,0,0,0,159,160,5,25,0,0,160,162,
        1,0,0,0,161,139,1,0,0,0,161,150,1,0,0,0,162,15,1,0,0,0,163,164,5,
        24,0,0,164,169,3,12,6,0,165,166,5,2,0,0,166,168,3,12,6,0,167,165,
        1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,169,170,1,0,0,0,170,172,
        1,0,0,0,171,169,1,0,0,0,172,173,5,25,0,0,173,17,1,0,0,0,174,183,
        5,24,0,0,175,180,3,12,6,0,176,177,5,2,0,0,177,179,3,12,6,0,178,176,
        1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,184,
        1,0,0,0,182,180,1,0,0,0,183,175,1,0,0,0,183,184,1,0,0,0,184,185,
        1,0,0,0,185,186,5,25,0,0,186,19,1,0,0,0,187,192,3,12,6,0,188,189,
        5,2,0,0,189,191,3,12,6,0,190,188,1,0,0,0,191,194,1,0,0,0,192,190,
        1,0,0,0,192,193,1,0,0,0,193,21,1,0,0,0,194,192,1,0,0,0,195,196,5,
        57,0,0,196,197,5,5,0,0,197,198,5,26,0,0,198,199,5,1,0,0,199,234,
        5,3,0,0,200,201,5,57,0,0,201,202,5,17,0,0,202,203,5,27,0,0,203,204,
        5,1,0,0,204,205,3,12,6,0,205,206,5,2,0,0,206,207,3,12,6,0,207,208,
        5,3,0,0,208,234,1,0,0,0,209,210,5,62,0,0,210,211,5,5,0,0,211,212,
        5,57,0,0,212,213,5,17,0,0,213,214,5,28,0,0,214,215,5,1,0,0,215,216,
        3,12,6,0,216,217,5,3,0,0,217,234,1,0,0,0,218,219,5,62,0,0,219,220,
        5,5,0,0,220,221,5,57,0,0,221,222,5,17,0,0,222,223,7,4,0,0,223,224,
        5,1,0,0,224,234,5,3,0,0,225,226,5,57,0,0,226,227,5,17,0,0,227,228,
        5,33,0,0,228,230,5,1,0,0,229,231,3,24,12,0,230,229,1,0,0,0,230,231,
        1,0,0,0,231,232,1,0,0,0,232,234,5,3,0,0,233,195,1,0,0,0,233,200,
        1,0,0,0,233,209,1,0,0,0,233,218,1,0,0,0,233,225,1,0,0,0,234,23,1,
        0,0,0,235,240,3,26,13,0,236,237,5,2,0,0,237,239,3,26,13,0,238,236,
        1,0,0,0,239,242,1,0,0,0,240,238,1,0,0,0,240,241,1,0,0,0,241,25,1,
        0,0,0,242,240,1,0,0,0,243,244,5,34,0,0,244,245,5,5,0,0,245,265,5,
        63,0,0,246,247,5,35,0,0,247,248,5,5,0,0,248,265,5,63,0,0,249,250,
        5,36,0,0,250,251,5,5,0,0,251,265,5,63,0,0,252,253,5,37,0,0,253,254,
        5,5,0,0,254,265,5,66,0,0,255,256,5,38,0,0,256,257,5,5,0,0,257,265,
        5,66,0,0,258,259,5,39,0,0,259,260,5,5,0,0,260,265,5,66,0,0,261,262,
        5,40,0,0,262,263,5,5,0,0,263,265,7,5,0,0,264,243,1,0,0,0,264,246,
        1,0,0,0,264,249,1,0,0,0,264,252,1,0,0,0,264,255,1,0,0,0,264,258,
        1,0,0,0,264,261,1,0,0,0,265,27,1,0,0,0,266,267,5,58,0,0,267,268,
        5,5,0,0,268,269,5,41,0,0,269,270,5,1,0,0,270,271,3,30,15,0,271,272,
        5,3,0,0,272,312,1,0,0,0,273,274,5,58,0,0,274,275,5,17,0,0,275,276,
        5,27,0,0,276,277,5,1,0,0,277,278,3,12,6,0,278,279,5,2,0,0,279,282,
        3,12,6,0,280,281,5,2,0,0,281,283,3,34,17,0,282,280,1,0,0,0,282,283,
        1,0,0,0,283,284,1,0,0,0,284,285,5,3,0,0,285,312,1,0,0,0,286,287,
        5,62,0,0,287,288,5,5,0,0,288,289,5,58,0,0,289,290,5,17,0,0,290,291,
        5,28,0,0,291,292,5,1,0,0,292,293,3,12,6,0,293,294,5,3,0,0,294,312,
        1,0,0,0,295,296,5,62,0,0,296,297,5,5,0,0,297,298,5,58,0,0,298,299,
        5,17,0,0,299,300,5,42,0,0,300,301,5,1,0,0,301,302,3,12,6,0,302,303,
        5,2,0,0,303,304,3,12,6,0,304,305,5,3,0,0,305,312,1,0,0,0,306,307,
        5,58,0,0,307,308,5,17,0,0,308,309,5,43,0,0,309,310,5,1,0,0,310,312,
        5,3,0,0,311,266,1,0,0,0,311,273,1,0,0,0,311,286,1,0,0,0,311,295,
        1,0,0,0,311,306,1,0,0,0,312,29,1,0,0,0,313,318,3,32,16,0,314,315,
        5,2,0,0,315,317,3,32,16,0,316,314,1,0,0,0,317,320,1,0,0,0,318,316,
        1,0,0,0,318,319,1,0,0,0,319,31,1,0,0,0,320,318,1,0,0,0,321,322,5,
        44,0,0,322,323,5,5,0,0,323,337,3,18,9,0,324,325,5,45,0,0,325,326,
        5,5,0,0,326,337,5,66,0,0,327,328,5,46,0,0,328,329,5,5,0,0,329,337,
        5,63,0,0,330,331,5,47,0,0,331,332,5,5,0,0,332,337,5,63,0,0,333,334,
        5,48,0,0,334,335,5,5,0,0,335,337,5,63,0,0,336,321,1,0,0,0,336,324,
        1,0,0,0,336,327,1,0,0,0,336,330,1,0,0,0,336,333,1,0,0,0,337,33,1,
        0,0,0,338,343,3,36,18,0,339,340,5,2,0,0,340,342,3,36,18,0,341,339,
        1,0,0,0,342,345,1,0,0,0,343,341,1,0,0,0,343,344,1,0,0,0,344,35,1,
        0,0,0,345,343,1,0,0,0,346,347,5,49,0,0,347,348,5,5,0,0,348,356,5,
        63,0,0,349,350,5,50,0,0,350,351,5,5,0,0,351,356,5,63,0,0,352,353,
        5,51,0,0,353,354,5,5,0,0,354,356,7,5,0,0,355,346,1,0,0,0,355,349,
        1,0,0,0,355,352,1,0,0,0,356,37,1,0,0,0,357,358,5,59,0,0,358,359,
        5,1,0,0,359,360,3,12,6,0,360,361,5,3,0,0,361,374,1,0,0,0,362,363,
        5,59,0,0,363,364,5,1,0,0,364,369,5,66,0,0,365,366,5,2,0,0,366,368,
        3,12,6,0,367,365,1,0,0,0,368,371,1,0,0,0,369,367,1,0,0,0,369,370,
        1,0,0,0,370,372,1,0,0,0,371,369,1,0,0,0,372,374,5,3,0,0,373,357,
        1,0,0,0,373,362,1,0,0,0,374,39,1,0,0,0,29,43,50,55,61,73,89,98,123,
        134,136,145,156,161,169,180,183,192,230,233,240,264,282,311,318,
        336,343,355,369,373
    ]

class LenguajeDominioEspecificoParser ( Parser ):

    grammarFileName = "LenguajeDominioEspecifico.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "':'", "'='", "'*'", 
                     "'/'", "'%'", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'+'", "'-'", "'.'", "'suma'", "'resta'", "'multiplicar'", 
                     "'transpuesta'", "'determinante'", "'inversa'", "'['", 
                     "']'", "'RegresionLineal'", "'fit'", "'predict'", "'mse'", 
                     "'mae'", "'r2'", "'rmse'", "'plot'", "'width'", "'height'", 
                     "'left_margin'", "'point_char'", "'line_char'", "'title'", 
                     "'show_stats'", "'PerceptronMulticapa'", "'score'", 
                     "'plot_loss'", "'hidden_layers'", "'activation'", "'learning_rate'", 
                     "'max_iter'", "'random_state'", "'epochs'", "'batch_size'", 
                     "'verbose'", "'matriz'", "'for'", "'while'", "'in'", 
                     "'range'", "'regresion'", "'mlp'", "'print'", "'True'", 
                     "'False'" ]

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
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "MATRIZ", "FOR", "WHILE", "IN", "RANGE", "REGRESION", 
                      "MLP", "PRINT", "TRUE", "FALSE", "ID", "NUMBER", "ENTERO", 
                      "DECIMAL", "STRING", "COMENTARIO", "WS", "NEWLINE" ]

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
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    MATRIZ=52
    FOR=53
    WHILE=54
    IN=55
    RANGE=56
    REGRESION=57
    MLP=58
    PRINT=59
    TRUE=60
    FALSE=61
    ID=62
    NUMBER=63
    ENTERO=64
    DECIMAL=65
    STRING=66
    COMENTARIO=67
    WS=68
    NEWLINE=69

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
            while _la==69:
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
                        if not (_la==69):
                            break

                    self.state = 52
                    self.instruccion() 
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==69:
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


    class ExpresionComparacionContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LenguajeDominioEspecificoParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDominioEspecificoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LenguajeDominioEspecificoParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionComparacion" ):
                listener.enterExpresionComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionComparacion" ):
                listener.exitExpresionComparacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionComparacion" ):
                return visitor.visitExpresionComparacion(self)
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
                self.match(LenguajeDominioEspecificoParser.T__16)
                self.state = 113
                localctx.operacion = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0)):
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
            self.state = 136
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 134
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = LenguajeDominioEspecificoParser.OperacionMultDivContext(self, LenguajeDominioEspecificoParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 125
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 126
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 127
                        self.expresion(11)
                        pass

                    elif la_ == 2:
                        localctx = LenguajeDominioEspecificoParser.ExpresionComparacionContext(self, LenguajeDominioEspecificoParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 128
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 129
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32256) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 130
                        self.expresion(10)
                        pass

                    elif la_ == 3:
                        localctx = LenguajeDominioEspecificoParser.OperacionSumaRestaContext(self, LenguajeDominioEspecificoParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 131
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 132
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 133
                        self.expresion(9)
                        pass

             
                self.state = 138
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
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = LenguajeDominioEspecificoParser.MatrizMultiFilaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.match(LenguajeDominioEspecificoParser.T__23)
                self.state = 140
                self.fila()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 141
                    self.match(LenguajeDominioEspecificoParser.T__1)
                    self.state = 142
                    self.fila()
                    self.state = 147
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 148
                self.match(LenguajeDominioEspecificoParser.T__24)
                pass

            elif la_ == 2:
                localctx = LenguajeDominioEspecificoParser.MatrizUnidimensionalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(LenguajeDominioEspecificoParser.T__23)
                self.state = 151
                self.expresion(0)
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 152
                    self.match(LenguajeDominioEspecificoParser.T__1)
                    self.state = 153
                    self.expresion(0)
                    self.state = 158
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 159
                self.match(LenguajeDominioEspecificoParser.T__24)
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
            self.state = 163
            self.match(LenguajeDominioEspecificoParser.T__23)
            self.state = 164
            self.expresion(0)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 165
                self.match(LenguajeDominioEspecificoParser.T__1)
                self.state = 166
                self.expresion(0)
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 172
            self.match(LenguajeDominioEspecificoParser.T__24)
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
            self.state = 174
            self.match(LenguajeDominioEspecificoParser.T__23)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -4607182418783240190) != 0) or _la==66:
                self.state = 175
                self.expresion(0)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 176
                    self.match(LenguajeDominioEspecificoParser.T__1)
                    self.state = 177
                    self.expresion(0)
                    self.state = 182
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 185
            self.match(LenguajeDominioEspecificoParser.T__24)
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
            self.state = 187
            self.expresion(0)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 188
                self.match(LenguajeDominioEspecificoParser.T__1)
                self.state = 189
                self.expresion(0)
                self.state = 194
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
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = LenguajeDominioEspecificoParser.CrearRegresionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.match(LenguajeDominioEspecificoParser.REGRESION)
                self.state = 196
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 197
                self.match(LenguajeDominioEspecificoParser.T__25)
                self.state = 198
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 199
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass

            elif la_ == 2:
                localctx = LenguajeDominioEspecificoParser.EntrenarRegresionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.match(LenguajeDominioEspecificoParser.REGRESION)
                self.state = 201
                self.match(LenguajeDominioEspecificoParser.T__16)
                self.state = 202
                self.match(LenguajeDominioEspecificoParser.T__26)
                self.state = 203
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 204
                localctx.x = self.expresion(0)
                self.state = 205
                self.match(LenguajeDominioEspecificoParser.T__1)
                self.state = 206
                localctx.y = self.expresion(0)
                self.state = 207
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass

            elif la_ == 3:
                localctx = LenguajeDominioEspecificoParser.PredecirRegresionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 209
                self.match(LenguajeDominioEspecificoParser.ID)
                self.state = 210
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 211
                self.match(LenguajeDominioEspecificoParser.REGRESION)
                self.state = 212
                self.match(LenguajeDominioEspecificoParser.T__16)
                self.state = 213
                self.match(LenguajeDominioEspecificoParser.T__27)
                self.state = 214
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 215
                self.expresion(0)
                self.state = 216
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass

            elif la_ == 4:
                localctx = LenguajeDominioEspecificoParser.ObtenerMetricaRegresionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 218
                self.match(LenguajeDominioEspecificoParser.ID)
                self.state = 219
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 220
                self.match(LenguajeDominioEspecificoParser.REGRESION)
                self.state = 221
                self.match(LenguajeDominioEspecificoParser.T__16)
                self.state = 222
                localctx.metrica = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8053063680) != 0)):
                    localctx.metrica = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 223
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 224
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass

            elif la_ == 5:
                localctx = LenguajeDominioEspecificoParser.GraficarRegresionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 225
                self.match(LenguajeDominioEspecificoParser.REGRESION)
                self.state = 226
                self.match(LenguajeDominioEspecificoParser.T__16)
                self.state = 227
                self.match(LenguajeDominioEspecificoParser.T__32)
                self.state = 228
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2181843386368) != 0):
                    self.state = 229
                    self.parametrosPlot()


                self.state = 232
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
            self.state = 235
            self.parametroPlot()
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 236
                self.match(LenguajeDominioEspecificoParser.T__1)
                self.state = 237
                self.parametroPlot()
                self.state = 242
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
            self.state = 264
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(LenguajeDominioEspecificoParser.T__33)
                self.state = 244
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 245
                self.match(LenguajeDominioEspecificoParser.NUMBER)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.match(LenguajeDominioEspecificoParser.T__34)
                self.state = 247
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 248
                self.match(LenguajeDominioEspecificoParser.NUMBER)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 249
                self.match(LenguajeDominioEspecificoParser.T__35)
                self.state = 250
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 251
                self.match(LenguajeDominioEspecificoParser.NUMBER)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 4)
                self.state = 252
                self.match(LenguajeDominioEspecificoParser.T__36)
                self.state = 253
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 254
                self.match(LenguajeDominioEspecificoParser.STRING)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 5)
                self.state = 255
                self.match(LenguajeDominioEspecificoParser.T__37)
                self.state = 256
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 257
                self.match(LenguajeDominioEspecificoParser.STRING)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 6)
                self.state = 258
                self.match(LenguajeDominioEspecificoParser.T__38)
                self.state = 259
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 260
                self.match(LenguajeDominioEspecificoParser.STRING)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 7)
                self.state = 261
                self.match(LenguajeDominioEspecificoParser.T__39)
                self.state = 262
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 263
                _la = self._input.LA(1)
                if not(_la==60 or _la==61):
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
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                localctx = LenguajeDominioEspecificoParser.CrearMLPContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(LenguajeDominioEspecificoParser.MLP)
                self.state = 267
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 268
                self.match(LenguajeDominioEspecificoParser.T__40)
                self.state = 269
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 270
                self.parametrosMLP()
                self.state = 271
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass

            elif la_ == 2:
                localctx = LenguajeDominioEspecificoParser.EntrenarMLPContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.match(LenguajeDominioEspecificoParser.MLP)
                self.state = 274
                self.match(LenguajeDominioEspecificoParser.T__16)
                self.state = 275
                self.match(LenguajeDominioEspecificoParser.T__26)
                self.state = 276
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 277
                localctx.x = self.expresion(0)
                self.state = 278
                self.match(LenguajeDominioEspecificoParser.T__1)
                self.state = 279
                localctx.y = self.expresion(0)
                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 280
                    self.match(LenguajeDominioEspecificoParser.T__1)
                    self.state = 281
                    self.parametrosEntrenamiento()


                self.state = 284
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass

            elif la_ == 3:
                localctx = LenguajeDominioEspecificoParser.PredecirMLPContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 286
                self.match(LenguajeDominioEspecificoParser.ID)
                self.state = 287
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 288
                self.match(LenguajeDominioEspecificoParser.MLP)
                self.state = 289
                self.match(LenguajeDominioEspecificoParser.T__16)
                self.state = 290
                self.match(LenguajeDominioEspecificoParser.T__27)
                self.state = 291
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 292
                self.expresion(0)
                self.state = 293
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass

            elif la_ == 4:
                localctx = LenguajeDominioEspecificoParser.EvaluarMLPContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 295
                self.match(LenguajeDominioEspecificoParser.ID)
                self.state = 296
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 297
                self.match(LenguajeDominioEspecificoParser.MLP)
                self.state = 298
                self.match(LenguajeDominioEspecificoParser.T__16)
                self.state = 299
                self.match(LenguajeDominioEspecificoParser.T__41)
                self.state = 300
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 301
                localctx.x = self.expresion(0)
                self.state = 302
                self.match(LenguajeDominioEspecificoParser.T__1)
                self.state = 303
                localctx.y = self.expresion(0)
                self.state = 304
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass

            elif la_ == 5:
                localctx = LenguajeDominioEspecificoParser.GraficarPerdidaMLPContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 306
                self.match(LenguajeDominioEspecificoParser.MLP)
                self.state = 307
                self.match(LenguajeDominioEspecificoParser.T__16)
                self.state = 308
                self.match(LenguajeDominioEspecificoParser.T__42)
                self.state = 309
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 310
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
            self.state = 313
            self.parametroMLP()
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 314
                self.match(LenguajeDominioEspecificoParser.T__1)
                self.state = 315
                self.parametroMLP()
                self.state = 320
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
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.match(LenguajeDominioEspecificoParser.T__43)
                self.state = 322
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 323
                self.lista()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.match(LenguajeDominioEspecificoParser.T__44)
                self.state = 325
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 326
                self.match(LenguajeDominioEspecificoParser.STRING)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 3)
                self.state = 327
                self.match(LenguajeDominioEspecificoParser.T__45)
                self.state = 328
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 329
                self.match(LenguajeDominioEspecificoParser.NUMBER)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 4)
                self.state = 330
                self.match(LenguajeDominioEspecificoParser.T__46)
                self.state = 331
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 332
                self.match(LenguajeDominioEspecificoParser.NUMBER)
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 5)
                self.state = 333
                self.match(LenguajeDominioEspecificoParser.T__47)
                self.state = 334
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 335
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
            self.state = 338
            self.parametroEntrenamiento()
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 339
                self.match(LenguajeDominioEspecificoParser.T__1)
                self.state = 340
                self.parametroEntrenamiento()
                self.state = 345
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
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.match(LenguajeDominioEspecificoParser.T__48)
                self.state = 347
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 348
                self.match(LenguajeDominioEspecificoParser.NUMBER)
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.match(LenguajeDominioEspecificoParser.T__49)
                self.state = 350
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 351
                self.match(LenguajeDominioEspecificoParser.NUMBER)
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 3)
                self.state = 352
                self.match(LenguajeDominioEspecificoParser.T__50)
                self.state = 353
                self.match(LenguajeDominioEspecificoParser.T__4)
                self.state = 354
                _la = self._input.LA(1)
                if not(_la==60 or _la==61):
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
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.match(LenguajeDominioEspecificoParser.PRINT)
                self.state = 358
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 359
                self.expresion(0)
                self.state = 360
                self.match(LenguajeDominioEspecificoParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.match(LenguajeDominioEspecificoParser.PRINT)
                self.state = 363
                self.match(LenguajeDominioEspecificoParser.T__0)
                self.state = 364
                self.match(LenguajeDominioEspecificoParser.STRING)
                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 365
                    self.match(LenguajeDominioEspecificoParser.T__1)
                    self.state = 366
                    self.expresion(0)
                    self.state = 371
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 372
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
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         




