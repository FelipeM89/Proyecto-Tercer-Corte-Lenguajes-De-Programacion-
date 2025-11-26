grammar LenguajeDominioEspecifico;

// Regla principal del programa
programa: NEWLINE* instruccion (NEWLINE+ instruccion)* NEWLINE* EOF;


// Instrucciones principales
instruccion
    : asignacion
    | regresionLineal
    | perceptronMulticapa
    | impresion
    | comentario
    | buclefor
    | buclewhile
    | condicional
    | mostrarTabla
    | operaciones
    | kmeans
    | graficar
    ;

// NUEVO: Condicionales IF/ELIF/ELSE (sin indentación compleja)
condicional
    : IF expresion ':' NEWLINE instruccion+ (ELIF expresion ':' NEWLINE instruccion+)* (ELSE ':' NEWLINE instruccion+)?
    ;

// buclefor
buclefor: FOR ID IN RANGE '(' NUMBER ',' NUMBER ')' ':' NEWLINE instruccion+;

//buclewhile
buclewhile: WHILE expresion ':' NEWLINE instruccion+;

// Comentarios
comentario: COMENTARIO;

// Asignación de variables
asignacion: ID '=' expresion;

// Expresiones
expresion
    : expresion ('*' | '/' | '%') expresion    # OperacionMultDiv
    | expresion ('==' | '!=' | '<' | '>' | '<=' | '>=') expresion  # ExpresionComparacion
    | expresion ('+' | '-') expresion          # OperacionSumaResta
    | expresion ('and' | 'or') expresion       # ExpresionLogica
    | 'not' expresion                          # ExpresionNot
    | '(' expresion ')'                        # ExpresionParentesis
    | MATRIZ '.' operacion=('suma' | 'resta' | 'multiplicar' | 'transpuesta' | 'determinante' |'inversa') '(' parametrosMatriz ')'        # OperacionMatrizExpr
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
    : ID '=' 'RegresionLineal' '(' ')'                                          # CrearRegresion
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
    | 'output_file' '=' STRING
    ;

// Perceptrón multicapa
perceptronMulticapa
    : 'mlp' '=' 'PerceptronMulticapa' '(' parametrosMLP ')'                             # CrearMLP
    | 'mlp' '.' 'fit' '(' x=expresion ',' y=expresion (',' parametrosEntrenamiento)? ')'      # EntrenarMLP
    | ID '=' 'mlp' '.' 'predict' '(' expresion ')'                                      # PredecirMLP
    | ID '=' 'mlp' '.' 'score' '(' x=expresion ',' y=expresion ')'                      # EvaluarMLP
    | 'mlp' '.' 'plot_loss' '(' (STRING)? ')'                                           # GraficarPerdidaMLP
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

// NUEVO: K-means clustering
kmeans
    : ID '=' 'KMeans' '(' parametrosKMeans ')'                                  # CrearKMeans
    | 'kmeans' '.' 'fit' '(' expresion ')'                                      # EntrenarKMeans
    | ID '=' 'kmeans' '.' 'predict' '(' expresion ')'                           # PredecirKMeans
    | ID '=' 'kmeans' '.' 'centroids' '(' ')'                                   # ObtenerCentroides
    | 'kmeans' '.' 'plot' '(' (STRING)? ')'                                     # GraficarKMeans
    ;

parametrosKMeans
    : parametroKMeans (',' parametroKMeans)*
    ;

parametroKMeans
    : 'n_clusters' '=' NUMBER
    | 'max_iter' '=' NUMBER
    | 'random_state' '=' NUMBER
    ;

// NUEVO: Gráficas generales
graficar
    : 'graficar' '(' x=expresion ',' y=expresion ',' archivo=STRING (',' parametrosGraficar)? ')'
    ;

parametrosGraficar
    : parametroGraficar (',' parametroGraficar)*
    ;

parametroGraficar
    : 'width' '=' NUMBER
    | 'height' '=' NUMBER
    | 'title' '=' STRING
    ;

// Impresión
impresion
    : PRINT '(' expresion ')'
    | PRINT '(' operaciones ')'
    | PRINT '(' STRING (',' expresion)* ')'
    ;
// Operaciones Aritmeticas
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
    : 'mostrar_tabla' '(' expresion (',' parametrosTabla)? ')'  # MostrarTablaASCII
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
//  ----------------------------------- Tokens léxicos

// Palabras reservadas 
MATRIZ: 'matriz';
FOR: 'for';
WHILE: 'while';
IF: 'if';
ELIF: 'elif';
ELSE: 'else';
IN: 'in';
RANGE: 'range';
REGRESION: 'regresion';
MLP: 'mlp';
PRINT: 'print';
TRUE: 'True';
FALSE: 'False';
// Identificadores
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Números (enteros y flotantes)

NUMBER
    : ENTERO
    | DECIMAL
    ;
ENTERO: '-'?[0-9]+;
DECIMAL: '-'?[0-9]+ ('.' [0-9]+)? ([eE] [+-]? [0-9]+)?;

// Cadenas de texto

STRING: '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'';


// Comentarios
COMENTARIO: '#' ~[\r\n]* -> skip;

// Espacios en blanco
WS: [ \t]+ -> skip;

NEWLINE: '\r'? '\n';
