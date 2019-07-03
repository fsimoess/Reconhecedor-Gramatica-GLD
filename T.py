import sys
from antlr4 import *
from GLDLexer import GLDLexer
from GLDParser import GLDParser

def main(argv):
    entrada = FileStream(argv[1])
    lexer = GLDLexer(entrada)
    palavra = CommonTokenStream(lexer)
    parser = GLDParser(palavra)

    #Executa o parser gerando a árvore, caso dê erro este será listado, senão 'passa batido'
    #Necessita ser o passo inicial da gramática na função referenciada
    arv = parser.s()

    print('Validação completa')

if __name__ == '__main__':
    main(sys.argv)