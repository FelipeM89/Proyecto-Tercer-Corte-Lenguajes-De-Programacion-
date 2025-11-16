# Proyecto-Tercer-Corte-Lenguajes-De-Programacion-

## Descripción
Proyecto de lenguajes de programación que incluye una colección de bibliotecas Python para operaciones matemáticas, manipulación de archivos, gráficas, y ejecución de comandos del sistema.

## Librerías Incluidas

### 1. LibreriaAritmentica.py
Operaciones aritméticas y funciones matemáticas en Python puro:
- Operaciones básicas (suma, resta, multiplicación, división)
- Funciones avanzadas: exp, ln, sqrt, potencia
- Trigonometría: sin, cos, tan
- Factorial y otras utilidades

### 2. LibreriaFunciones.py
Funciones estadísticas y de análisis:
- Regresión lineal (OLS)
- Métricas: MSE, MAE
- Normalización: min-max, z-score
- Utilidades: mean, variance, dot product

### 3. LibreriasMatrices.py
Operaciones con matrices 2D:
- Suma, resta, multiplicación de matrices
- Transpuesta, inversa, determinante
- Multiplicación matriz-vector

### 4. LibreriaArchivoGestion.py
Gestión de archivos de texto:
- Lectura y escritura de archivos
- Manejo de CSV
- Append de contenido

### 5. LibreriaGraficas.py
Visualización de datos en ASCII:
- Gráficas de barras
- Gráficas de línea
- Exportación de puntos a CSV

### 6. LibreriaTerminal.py ⭐ **NUEVO**
Ejecución de comandos del sistema y formato de salida en terminal:
- **Ejecución de comandos**: ejecutar_comando(), ejecutar_y_capturar(), ejecutar_y_mostrar()
- **Información del sistema**: obtener_sistema_operativo(), obtener_informacion_sistema()
- **Formato de salida**: escribir_tabla(), escribir_titulo(), escribir_separador()
- Compatible con Linux, Windows y macOS

## Instalación

No requiere dependencias externas. Todas las bibliotecas usan únicamente módulos estándar de Python.

```bash
git clone https://github.com/samuelleyton2006/Proyecto-Tercer-Corte-Lenguajes-De-Programacion-.git
cd Proyecto-Tercer-Corte-Lenguajes-De-Programacion-
```

## Uso

### Ejemplo: LibreriaTerminal
```python
from Librerias.LibreriaTerminal import *

# Ejecutar comando del sistema
resultado = ejecutar_y_capturar('ls -la')
print(resultado['salida'])

# Mostrar información del sistema
info = obtener_informacion_sistema()
escribir_tabla([[k, v] for k, v in info.items()], ["Propiedad", "Valor"])

# Ejecutar con formato
ejecutar_y_graficar_salida('echo "Hola Mundo"')
```

### Ejemplo: Integración de Librerías
```python
from Librerias.LibreriaTerminal import *
from Librerias.LibreriaGraficas import GenerarGrafica

# Obtener datos y graficar
datos = [5, 12, 8, 15, 20, 3, 18, 10]
escribir_titulo("Visualización de Datos")
GenerarGrafica(datos)
```

## Testing

Ejecutar todos los tests:
```bash
cd tests
for test in test_*.py; do python3 "$test"; done
```

## Estructura del Proyecto
```
.
├── Librerias/
│   ├── LibreriaAritmentica.py
│   ├── LibreriaFunciones.py
│   ├── LibreriasMatrices.py
│   ├── LibreriaArchivoGestion.py
│   ├── LibreriaGraficas.py
│   └── LibreriaTerminal.py  ⭐ NUEVO
├── tests/
│   ├── test_aritmetica.py
│   ├── test_funciones.py
│   ├── test_matrices.py
│   ├── test_archivo_gestion.py
│   ├── test_graficas.py
│   └── test_terminal.py  ⭐ NUEVO
└── README.md
```

## Requisitos
- Python 3.6+
- Sin dependencias externas (solo módulos estándar)