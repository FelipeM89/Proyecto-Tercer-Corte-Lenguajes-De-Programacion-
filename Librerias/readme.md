# LibreriaArchivoGestion

Lectura y escritura de archivos y CSV 

## leer_txt(path)
Funcion para leer un archivo, el path es el nombre del archivo

Devuelve una cadena que contiene todas las lineas del archivo separadas por '\n'

# Ejemplo: 
```bash
un dia
vi una
```
# Output
"un dia\n vi una"
## escribir_txt(path, contenido)

Sobreescribe un archivo con la cadena del contenido, devuelve true si se escribio el contenido. Si el archivo no existe, se crea un archivo y se escribe el contenido 

## append_txt(path,contenido)
Agrega al final de un archivo una cadena de texto, devuelve true si la agrego

## guardar_csv(path,rows,sep=',')

Guarda datos en formato csv, rows puede ser una lista de cadenas de texto o numeros.
sep, es el tipo de separador por el cual los datos van a hacer almacenados (por default es ',')
## Ejemplo
```bash
guardar_csv("f.csv", [[1,2,3],[4,5,6]])
```
output:
```bash
1,2,3
4,5,6
```
## cargar_csv(path, sep=',', tipo=float)

Lee el archivo path, identifica el tipo de separador del archivo y el tipo de dato del archivo. Devuelve una lista de los datos almacenados por el path

# Ejemplo
```bash
archivo.csv

1,2,3
4,5,6

cargar_csv("archivo.csv")
```
Output:

```bash
[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
```

---
# LibreriaAritmetica

## abs_val(x)

Valor absoluto de x

## factorial(n)

Fctorial de un numero

## exp(x)
Implementacion con series de taylor para hallar la exponencia de e^x

## ln(x)

Funcion de logaritmo para x, mediante la reduccion de rango y serie de taylor
## sqrt(x)
Funcion raiz para x
## powf(x,y)
Exponenciacion de x^y 

## sin(x)

Funcion de seno mediante serie de taylor 

## cos(x)
Funcion de coseno mediante serie de taylor

## tan(x)
Funcion de tangente mediante serie de taylor

## division(a,b)

Division con manejo de errores
## modulo(a,b)
Modulo con manejo de errores



# LibreriaFuncion

Se encarga de imprimir puntos en el plano (x,y) mediante caracteres ascii

## render_ascii(x,y, width=80,height=20, left_margin=9, point_char='*', title)

Permite renderizar una lista de valores x,y con diferentes parametros:
- width: Ancho del area
- height: Alto del area
- lef_margin: margen
- point_char: caracter para representar los puntos
- title: titulo opcional
# Libreria Funciones

## mean(xs)

Devuelve la media de los datos

## variance(xs)

Devuelve la varianza de los datos

## std(xs)
Devuelve la desviacion estandar

## dot (a,b)

Calcula el producto escalar de dos vectores (a,b), devuelve un float

## min_max_normalize(xs)

Utiliza la normalizacion minima-maxima [0,1] de los datos ingresados, devuelve una lista con los datos normalizados
## Ejemplo

```bash

[10,20,30]
```
Output:

```bash
[0.0,0.5,1.0]
```
## z_score(xs)

Devuelve la cantidad de desviaciones estandar que esta ese valor por encima o debajo de la media

```bash
xs = [1, 2, 3] → media = 2, sd ≈ 0.8165 
 z ≈ [-1.2247, 0.0, 1.2247].
```

## mse(y_true,y_pred)
Calcula el error cuadratico medio entre los datos de la muestra y los datos que predice el modelo.
Cuanto menor es este dato, mejor es la prediccion.
## mae(y_true,y_pred)
Calcula el error absoluto medio. Mide el error promedio de la muestra. 
Cuanto mayor mae, peor la prediccion
## rmse(y_true,y_pred)
Calcula la raiz del error cuadratico medio. Este mide el error promedio de las predicciones, a menor valor, mejor prediccion.
## r2(y_true,y_pred)
calcula el coeficiente de determinacion R, una métrica que indica que fracción de la varianza de la variable objetivo es explicada por el modelo.
R² = 1.0: predicciones perfectas (ss_res = 0).
R² = 0.0: el modelo predice tan mal como usar la media (ss_res = ss_tot).
R² negativo: el modelo es peor que predecir siempre la media (ss_res > ss_tot).
R² cercano a 1 → mejor ajuste; cercano a 0 → ajuste pobre.

## regresion_lineal(x,y)
Crea una regresion lineal mediante minimos cuadrados ordinarios.
Devuelve la pendiente m y la coordenada del origen b
## predict_linear(X,m,b)
Predice los datos X, teniendo en cuenta la pendiente y la coordenada de origen.

# LibreriaGraficas

## guardar_puntos(path,xs,ys)
Guarda los datos en formato csv con nombre de archivo path

## print_hist(vals,bin=10)

Genera un histograma de los datos en formato ascii

# LibreriaPerceptronMC

## sigmoid (x)
Funcion de activacion logistica, mapea cualquier real a (0,1)
## dsigmoid (x)
Calcula la derivada de la sigmoide repecto a su entrada
## Clase PerceptronMulticapa(layers, learning_rate=0.1,seed=1234)




# LibreriaRegresionLineal

## Clase regresion_lineal_model
Primero instanciar la clase:
model = regresion_lineal_model()

## fit(x,y)
Ajusta el modelo de regresion lineal con los datos x,y

## predict(x)
Predice los valores dados una lista de x usando el modelo ajustado

## mse()

Calcula el error cuadratico medio del modelo

## mae()
Calcula el error absoluto medio

## r2()
Calcula el coeficiente de determinacion
## rmse()
Calcula la raiz del error cuadratico medio
## render_ascii_regression(width=80, height=20,left_margin=9, point_char='*', line_char='-', title= optional, show_stats=true)

Renderiza un gráfico ASCII con puntos (x,y) y la recta de regresiOn y = m x + b.
Devuelve el contenido como string
- width: ancho del Area de dibujo (sin contar margen izquierdo para labels).
- height: alto del Area de dibujo.
- left_margin: espacio para etiquetas.
- point_char: caracter para representar los puntos de datos.
- line_char: caracter para representar la línea de regresión.
- title: titulo opcional para el gráfico.
- show_stats: mostrar estadísticas de la regresión.

# LibreriaMatrices
