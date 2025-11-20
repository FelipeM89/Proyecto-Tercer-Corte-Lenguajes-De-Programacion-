grammar lenguajeDominiEspecifico;

// Regla principal del programa
programa: instruccion+ EOF;

// Instrucciones principales
instruccion
    : asignacion
    | operacionMatriz
    | regresionLineal
    | perceptronMulticapa
    | impresion
    | comentario
    ;

// Comentarios
comentario: COMENTARIO;

// Asignación de variables
asignacion: ID '=' expresion;

// Expresiones
expresion
    : expresion ('*' | '/' | '%') expresion    # OperacionMultDiv
    | expresion ('+' | '-') expresion          # OperacionSumaResta
    | '(' expresion ')'                        # ExpresionParentesis
    | matriz                                   # ExpresionMatriz
    | lista                                    # ExpresionLista
    | NUMBER                                   # ExpresionNumero
    | ID                                       # ExpresionVariable
    | STRING                                   # ExpresionString
    ;

// Definición de matrices
matriz
    : '[' fila (',' fila)* ']'               # MatrizMultiFila
    | '[' expresion (',' expresion)* ']'     # MatrizUnidimensional
    ;

fila: '[' expresion (',' expresion)* ']';

// Listas
lista: '[' (expresion (',' expresion)*)? ']';

// Operaciones con matrices
operacionMatriz
    : 'matriz' '.' operacion=('suma' | 'resta' | 'multiplicar' | 'transpuesta' | 'determinante' | 'inversa') 
      '(' parametrosMatriz ')'                                        # OperacionMatrizBasica
    | ID '=' 'matriz' '.' operacion=('suma' | 'resta' | 'multiplicar' | 'transpuesta' | 'determinante' | 'inversa') 
      '(' parametrosMatriz ')'                                        # AsignacionOperacionMatriz
    ;

parametrosMatriz
    : expresion (',' expresion)*
    ;

// Regresión lineal
regresionLineal
    : 'regresion' '=' 'RegresionLineal' '(' ')'                                          # CrearRegresion
    | 'regresion' '.' 'fit' '(' x=expresion ',' y=expresion ')'                          # EntrenarRegresion
    | ID '=' 'regresion' '.' 'predict' '(' expresion ')'                                 # PredecirRegresion
    | ID '=' 'regresion' '.' metrica=('mse' | 'mae' | 'r2' | 'rmse') '(' ')'           # ObtenerMetricaRegresion
    | 'regresion' '.' 'plot' '(' (parametrosPlot)? ')'                                  # GraficarRegresion
    ;

parametrosPlot
    : parametroPlot (',' parametroPlot)*
    ;

parametroPlot
    : 'width' '=' NUMBER
    | 'height' '=' NUMBER
    | 'left_margin' '=' NUMBER
    | 'point_char' '=' STRING
    | 'line_char' '=' STRING
    | 'title' '=' STRING
    | 'show_stats' '=' ('True' | 'False')
    ;

// Perceptrón multicapa
perceptronMulticapa
    : 'mlp' '=' 'PerceptronMulticapa' '(' parametrosMLP ')'                             # CrearMLP
    | 'mlp' '.' 'fit' '(' x=expresion ',' y=expresion (',' parametrosEntrenamiento)? ')'      # EntrenarMLP
    | ID '=' 'mlp' '.' 'predict' '(' expresion ')'                                      # PredecirMLP
    | ID '=' 'mlp' '.' 'score' '(' x=expresion ',' y=expresion ')'                      # EvaluarMLP
    | 'mlp' '.' 'plot_loss' '(' ')'                                                     # GraficarPerdidaMLP
    ;

parametrosMLP
    : parametroMLP (',' parametroMLP)*
    ;

parametroMLP
    : 'hidden_layers' '=' lista
    | 'activation' '=' STRING
    | 'learning_rate' '=' NUMBER
    | 'max_iter' '=' NUMBER
    | 'random_state' '=' NUMBER
    ;

parametrosEntrenamiento
    : parametroEntrenamiento (',' parametroEntrenamiento)*
    ;

parametroEntrenamiento
    : 'epochs' '=' NUMBER
    | 'batch_size' '=' NUMBER
    | 'verbose' '=' ('True' | 'False')
    ;

// Impresión
impresion
    : 'print' '(' expresion ')'
    | 'print' '(' STRING (',' expresion)* ')'
    ;

// Tokens léxicos

// Palabras reservadas (ya definidas en las reglas)

// Identificadores
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Números (enteros y flotantes)
NUMBER: [0-9]+ ('.' [0-9]+)? ([eE] [+-]? [0-9]+)?;

// Cadenas de texto
STRING: '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'';

// Comentarios
COMENTARIO: '#' ~[\r\n]* -> skip;

// Espacios en blanco
WS: [ \t\r\n]+ -> skip;