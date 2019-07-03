# Reconhecedor de GLD
Reconhece e valida gramáticas GLD utilizando Python e Antlr.

## Uso

- Primeiro é necessário possuir um arquivo .txt (gr.txt) contendo a definição formal de uma gramática:
```
G = ({}, {}, S, {})
```
- Depois executa-se o parser de gramáticas:
```
python gr.py gr.txt
```
- A partir disso os arquivos antlr são gerados (parser, lexer, etc) com o seguinte comando:
```
java -Xmx500M -cp antlr.jar org.antlr.v4.Tool -Dlanguage=Python3 GLD.g4
```
Sendo antlr.jar o caminho do JAR de antlr, a linguagem/API escolhida python3 e o arquivo de gramáticas GLD.g4

- Aí rodam-se os testes com um arquivo qualquer (exemplo T.py) obtendo funções para uma palavra a ser testada (exemplo a.txt):
```
python T.py a.txt
```

**Obs.: Caso o arquivo de gramática TXT for modificado, é necessário refazer todos os passos. Caso o arquivo G4 seja modificado, apenas a partir do passo de compilação do JAR necessita ser refeito.**
