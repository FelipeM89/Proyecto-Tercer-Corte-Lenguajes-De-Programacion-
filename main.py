from antlr4 import * 
import sys
from Visitor.LenguajeDominioEspecificoLexer import LenguajeDominioEspecificoLexer
from Visitor.LenguajeDominioEspecificoParser import LenguajeDominioEspecificoParser
from Visitor.Visitor import Visitor


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Leer desde archivo
        input_stream = FileStream(sys.argv[1], encoding='utf-8')
    else:
        print("Uso: python main.py <archivo>")
        sys.exit(1)
    lexer = LenguajeDominioEspecificoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    parser = LenguajeDominioEspecificoParser(stream)
    tree = parser.programa()
    
    
    if parser.getNumberOfSyntaxErrors() > 0:
        print(f"\n Se encontraron {parser.getNumberOfSyntaxErrors()} errores sintacticos")
        sys.exit(1)
    else:
        print("Analisis sintactico exitoso\n")
    try:
        evaluador = Visitor()
        evaluador.visit(tree)
        
        # Mostrar tabla de símbolos final
        evaluador.mostrar_tabla_simbolos()
        
    except Exception as e:
        print(f"\n Error de evaluacion: {e}")
        sys.exit(1)

