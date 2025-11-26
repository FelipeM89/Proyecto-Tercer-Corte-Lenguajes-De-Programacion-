# Lenguaje de Dominio Específico para Análisis de Datos y Machine Learning

## 🎯 Funcionalidades Implementadas

### ✅ Nuevas Funcionalidades Agregadas:

#### 1. **Condicionales IF/ELIF/ELSE**
Ahora el lenguaje soporta estructuras condicionales completas:
```
if condicion:
    instruccion
elif otra_condicion:
    instruccion
else:
    instruccion
```

#### 2. **Guardado Automático de Gráficas**
Todas las funciones de graficado ahora pueden guardar automáticamente en archivos:
- `regresion.plot(output_file="archivo.txt")` - Guarda gráfica de regresión
- `mlp.plot_loss("archivo.txt")` - Guarda gráfica de pérdida del MLP
- `graficar(x, y, "archivo.txt")` - Función general de graficado

#### 3. **Función General de Gráficas**
Nueva función `graficar(x, y, archivo)` para graficar datos arbitrarios:
```
graficar(x_datos, y_datos, "salida.txt", width=60, height=20, title="Mi Gráfica")
```

#### 4. **Algoritmo K-means para Clustering**
Implementación completa del algoritmo K-means:
```
modelo = KMeans(n_clusters=3, max_iter=100, random_state=42)
kmeans.fit(datos)
labels = kmeans.predict(nuevos_datos)
centroides = kmeans.centroids()
```

#### 5. **Expresiones Lógicas y Booleanas**
Soporte para operadores lógicos:
- `and`, `or`, `not`
- Valores booleanos: `True`, `False`

---

## 📁 Archivos Nuevos Creados

### Librerías:
1. **`Librerias/LibreriaKMeans.py`** - Implementación del algoritmo K-means

### Archivos de Ejemplo:
1. **`ejemplo_condicionales.txt`** - Ejemplos de uso de IF/ELIF/ELSE
2. **`ejemplo_kmeans.txt`** - Ejemplos de clustering con K-means
3. **`ejemplo_graficas.txt`** - Ejemplos de guardado automático de gráficas

### Archivos Modificados:
1. **`Visitor/LenguajeDominioEspecifico.g4`** - Gramática actualizada
2. **`Visitor/Visitor.py`** - Visitor con nuevas funcionalidades
3. **`Librerias/LibreriaGraficas.py`** - Funciones de graficado mejoradas
4. **`Librerias/__init__.py`** - Imports actualizados

---

## ⚙️ IMPORTANTE: Regenerar el Parser ANTLR

Después de los cambios en la gramática, necesitas regenerar los archivos del parser:

### Opción 1: Usando Java (recomendado)
```bash
cd Visitor
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor LenguajeDominioEspecifico.g4
```

### Opción 2: Usando comando antlr4 (si está en PATH)
```bash
cd Visitor
antlr4 -Dlanguage=Python3 -visitor LenguajeDominioEspecifico.g4
```

### Opción 3: Con Python antlr4-tools
```bash
pip install antlr4-tools
cd Visitor
antlr4 -Dlanguage=Python3 -visitor LenguajeDominioEspecifico.g4
```

⚠️ **DEBES ejecutar uno de estos comandos antes de poder usar el lenguaje actualizado!**

---

## 🚀 Cómo Usar

### Ejecutar un programa:
```bash
python main.py ejemplo_condicionales.txt
python main.py ejemplo_kmeans.txt
python main.py ejemplo_graficas.txt
```

### Ejemplos de Código:

#### Condicionales:
```
x = 10
if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual a 5")
else:
    print("x es menor que 5")
```

#### K-means:
```
datos = [[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6]]
modelo = KMeans(n_clusters=2, max_iter=100, random_state=42)
kmeans.fit(datos)
labels = kmeans.predict([[0, 0], [9, 9]])
print(labels)
```

#### Gráficas con guardado:
```
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
graficar(x, y, "mi_grafica.txt", title="Línea recta")
```

---

## 📊 Mejoras en Funciones Existentes

### Gráficas de Regresión:
Ahora soportan el parámetro `output_file`:
```
regresion.plot(output_file="regresion_output.txt", title="Mi Regresión", show_stats=True)
```

### Gráficas de MLP:
```
mlp.plot_loss("historial_perdida.txt")
```

---

## 🧪 Pruebas

Para probar todas las funcionalidades nuevas:

```bash
# 1. Regenerar parser (OBLIGATORIO)
cd Visitor
antlr4 -Dlanguage=Python3 -visitor LenguajeDominioEspecifico.g4
cd ..

# 2. Probar condicionales
python main.py ejemplo_condicionales.txt

# 3. Probar K-means
python main.py ejemplo_kmeans.txt

# 4. Probar gráficas
python main.py ejemplo_graficas.txt

# 5. Probar programa existente (para verificar compatibilidad)
python main.py programa_regresion.txt
```

---

## ✨ Características Técnicas

### Operadores Lógicos:
- `and` - Y lógico
- `or` - O lógico
- `not` - Negación lógica

### Valores Booleanos:
- `True`
- `False`

### Comparaciones:
- `==`, `!=`, `<`, `>`, `<=`, `>=`

### Expresiones Numéric as:
- Aritmética: `+`, `-`, `*`, `/`, `%`
- Funciones: `abs()`, `sqrt()`, `exp()`, `ln()`, `sin()`, `cos()`, `tan()`, `factorial()`, `powf()`

---

## 📝 Notas Importantes

1. **Indentación**: Los bloques de código NO requieren indentación estricta como Python. Las instrucciones simplemente se colocan después de los `:` y `NEWLINE`.

2. **Compatibilidad**: Todos los programas anteriores siguen funcionando correctamente con las nuevas características.

3. **Gráficas**: Los archivos de gráficas se guardan en formato texto ASCII, legibles con cualquier editor de texto.

4. **K-means**: Soporta datos tanto 1D como 2D (y más dimensiones en la implementación).

---

## 🐛 Solución de Problemas

### Error: "No viable alternative at input"
- Asegúrate de haber regenerado el parser con ANTLR después de modificar la gramática.

### Error: "module not found"
- Verifica que todas las librerías estén en la carpeta `Librerias/`
- Revisa que `__init__.py` tenga todos los imports

### Las gráficas no se guardan
- Verifica que el path del archivo sea válido
- Asegúrate de tener permisos de escritura en el directorio

---

## 👥 Contribución

Para agregar nuevas funcionalidades:
1. Modifica la gramática en `LenguajeDominioEspecifico.g4`
2. Regenera el parser con ANTLR
3. Implementa los métodos visitor en `Visitor.py`
4. Agrega las funciones auxiliares en las librerías apropiadas
5. Crea archivos de ejemplo

---

## 📄 Licencia

Este proyecto es para fines educativos.
