grammar LenguajeDominioEspecifico;

// Regla principal del programa
programa: instruccion* EOF;

// Instrucciones principales
instruccion
    : asignacion
    | regresionLineal
    | perceptronMulticapa
    | prediccionModelo
    | impresion
    | comentario
    | buclefor
    | buclewhile
    | condicional
    | mostrarTabla
    | operaciones ';'
    | kmeans
    | graficar
    ;

// Condicionales IF/ELIF/ELSE con llaves
condicional
    : IF '(' expresion ')' '{' instruccion* '}' (ELIF '(' expresion ')' '{' instruccion* '}')* (ELSE '{' instruccion* '}')?
    ;

// Bucle for con llaves
buclefor
    : FOR '(' ID IN RANGE '(' expresion ',' expresion ')' ')' '{' instruccion* '}'
    ;

// Bucle while con llaves
buclewhile
    : WHILE '(' expresion ')' '{' instruccion* '}'
    ;

// Comentarios
comentario: COMENTARIO;

// Asignación de variables
asignacion: ID '=' expresion ';';

// Expresiones
expresion
    : expresion ('*' | '/' | '%') expresion    # OperacionMultDiv
    | expresion ('==' | '!=' | '<' | '>' | '<=' | '>=') expresion  # ExpresionComparacion
    | expresion ('+' | '-') expresion          # OperacionSumaResta
    | expresion ('and' | 'or') expresion       # ExpresionLogica
    | 'not' expresion                          # ExpresionNot
    | '(' expresion ')'                        # ExpresionParentesis
    | MATRIZ '.' operacion=('suma' | 'resta' | 'multiplicar' | 'transpuesta' | 'determinante' | 'inversa') '(' parametrosMatriz ')'  # OperacionMatrizExpr
    | ID '.' 'centroids'                       # AccesoCentroides
    | 'RegresionLineal' '(' ')'                # CrearRegresion
    | operaciones                              # ExpresionOperacion
    | matriz                                   # ExpresionMatriz
    | lista                                    # ExpresionLista
    | NUMBER                                   # ExpresionNumero
    | ID                                       # ExpresionVariable
    | STRING                                   # ExpresionString
    | TRUE                                     # ExpresionBooleano
    | FALSE                                    # ExpresionBooleano
    ;

// Definición de matrices
matriz
    : '[' fila (',' fila)* ']'               # MatrizMultiFila
    | '[' expresion (',' expresion)* ']'     # MatrizUnidimensional
    ;

fila: '[' expresion (',' expresion)* ']';

// Listas
lista: '[' (expresion (',' expresion)*)? ']';

parametrosMatriz
    : expresion (',' expresion)*
    ;

// Regresión lineal
regresionLineal
    : ID '.' 'fit' '(' x=expresion ',' y=expresion ')' ';'                     # EntrenarRegresion
    | target=ID '=' modelo=ID '.' metrica=('mse' | 'mae' | 'r2' | 'rmse') '(' ')' ';' # ObtenerMetricaRegresion
    | ID '.' 'plot' '(' (parametrosPlot)? ')' ';'                              # GraficarRegresion
    ;

// Predicción genérica (funciona para regresión, MLP, kmeans)
prediccionModelo
    : target=ID '=' modelo=ID '.' 'predict' '(' expresion ')' ';'              # PredecirModelo
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
    | 'output_file' '=' STRING
    ;

// Perceptrón multicapa
perceptronMulticapa
    : ID '=' 'PerceptronMulticapa' '(' parametrosMLP ')' ';'                        # CrearMLP
    | ID '.' 'fit' '(' x=expresion ',' y=expresion (',' parametrosEntrenamiento)? ')' ';' # EntrenarMLP
    | target=ID '=' modelo=ID '.' 'score' '(' x=expresion ',' y=expresion ')' ';'   # EvaluarMLP
    | ID '.' 'plot_loss' '(' (STRING)? ')' ';'                                      # GraficarPerdidaMLP
    ;

parametrosMLP
    : parametroMLP (',' parametroMLP)*
    ;

parametroMLP
    : 'layers' '=' lista
    | 'learning_rate' '=' NUMBER
    | 'seed' '=' NUMBER
    ;

parametrosEntrenamiento
    : parametroEntrenamiento (',' parametroEntrenamiento)*
    ;

parametroEntrenamiento
    : 'epochs' '=' NUMBER
    | 'batch_size' '=' NUMBER
    | 'verbose' '=' ('True' | 'False')
    ;

// K-means clustering
kmeans
    : ID '=' 'KMeans' '(' parametrosKMeans ')' ';'                             # CrearKMeans
    | ID '.' 'fit' '(' expresion ')' ';'                                       # EntrenarKMeans
    | ID '.' 'plot' '(' (parametrosGraficarKMeans)? ')' ';'                    # GraficarKMeans
    ;

parametrosKMeans
    : parametroKMeans (',' parametroKMeans)*
    ;

parametroKMeans
    : 'n_clusters' '=' NUMBER
    | 'max_iter' '=' NUMBER
    | 'seed' '=' NUMBER
    ;

parametrosGraficarKMeans
    : parametroGraficarKMeans (',' parametroGraficarKMeans)*
    ;

parametroGraficarKMeans
    : 'width' '=' NUMBER
    | 'height' '=' NUMBER
    | 'output_file' '=' STRING
    ;

// Gráficas generales
graficar
    : 'graficar' '(' x=expresion ',' y=expresion (',' parametrosGraficar)? ')' ';'
    ;

parametrosGraficar
    : parametroGraficar (',' parametroGraficar)*
    ;

parametroGraficar
    : 'width' '=' NUMBER
    | 'height' '=' NUMBER
    | 'title' '=' STRING
    | 'output_file' '=' STRING
    ;

// Impresión
impresion
    : PRINT '(' expresion (',' expresion)* ')' ';'
    ;

// Operaciones Aritméticas
operaciones
    : 'abs' '(' expresion ')'
    | 'factorial' '(' expresion ')'
    | 'exp' '(' expresion ')'
    | 'ln' '(' expresion ')'
    | 'sqrt' '(' expresion ')'
    | 'powf' '(' parametrosOp ')'
    | 'sin' '(' expresion ')'
    | 'cos' '(' expresion ')'
    | 'tan' '(' expresion ')'
    | 'div' '(' parametrosOp ')'
    | 'mod' '(' parametrosOp ')'
    ;

parametrosOp
    : expresion ',' expresion
    ;

// Tablas estilo pandas
mostrarTabla
    : 'mostrar_tabla' '(' expresion (',' parametrosTabla)? ')' ';'  # MostrarTablaASCII
    ;

parametrosTabla
    : parametroTabla (',' parametroTabla)*
    ;

parametroTabla
    : 'max_rows' '=' NUMBER
    | 'max_cols' '=' NUMBER
    | 'max_col_width' '=' NUMBER
    | 'floatfmt' '=' STRING
    | 'show_index' '=' (TRUE | FALSE)
    | 'headers' '=' lista
    ;

// ----------------------------------- Tokens léxicos

// Palabras reservadas (deben ir ANTES de ID)
MATRIZ: 'matriz';
FOR: 'for';
WHILE: 'while';
IF: 'if';
ELIF: 'elif';
ELSE: 'else';
IN: 'in';
RANGE: 'range';
PRINT: 'print';
TRUE: 'True';
FALSE: 'False';
GRAFICAR: 'graficar';
MOSTRAR_TABLA: 'mostrar_tabla';
KMEANS: 'KMeans';
PERCEPTRON: 'PerceptronMulticapa';
REGRESION: 'RegresionLineal';

// Identificadores (va DESPUÉS de las palabras reservadas)
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Números (enteros y flotantes)
NUMBER
    : '-'? [0-9]+ ('.' [0-9]+)? ([eE] [+-]? [0-9]+)?
    ;

// Cadenas de texto
STRING: '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'';

// Comentarios
COMENTARIO: '#' ~[\r\n]* -> skip;

// Espacios en blanco
WS: [ \t\r\n]+ -> skip;