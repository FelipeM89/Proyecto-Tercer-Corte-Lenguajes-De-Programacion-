
from Visitor.lenguajeDominiEspecificoLexer import lenguajeDominiEspecificoLexer
from Visitor.lenguajeDominiEspecificoParser import lenguajeDominiEspecificoParser
from Visitor.Visitor import Visitor


def ejecutar_archivo(ruta):
    input_stream = FileStream(ruta, encoding="utf-8")
    lexer = lenguajeDominiEspecificoLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = lenguajeDominiEspecificoParser(tokens)
    
    tree = parser.programa()
    visitor = Visitor()
    visitor.visit(tree)


if __name__ == "__main__":
    ejecutar_archivo("programa.dsl")