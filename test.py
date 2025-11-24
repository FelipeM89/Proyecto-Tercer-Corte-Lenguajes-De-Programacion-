from antlr4 import *
from Visitor.LenguajeDominioEspecificoLexer import LenguajeDominioEspecificoLexer
from Visitor.LenguajeDominioEspecificoParser import LenguajeDominioEspecificoParser

codigo = """suma = matriz.suma([[1,2]], [[3,4]])
"""

input_stream = InputStream(codigo)
lexer = LenguajeDominioEspecificoLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = LenguajeDominioEspecificoParser(token_stream)

# Intenta parsear
tree = parser.programa()

# Si llegamos aquí, el parsing fue exitoso
print("✅ Parsing exitoso!")
print(f"Errores: {parser.getNumberOfSyntaxErrors()}")