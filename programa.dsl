# ========================================
# EJEMPLO COMPLETO - ANÁLISIS DE DATOS
# ========================================

print("=== ANÁLISIS DE DATOS CON DSL ===\n");

# ----------------------------
# 1. OPERACIONES MATEMÁTICAS
# ----------------------------
print("--- 1. Cálculos Matemáticos ---");

pi = 3.141592653589793;
radio = 5;

# Área del círculo: π * r²
area = pi * powf(radio, 2);
print("Radio:", radio);
print("Área del círculo:", area);

# Volumen de esfera: (4/3) * π * r³
volumen = 4 / 3 * pi * powf(radio, 3);
print("Volumen de la esfera:", volumen);

# Trigonometría
angulo = pi / 4;
seno_45 = sin(angulo);
coseno_45 = cos(angulo);
print("sen(45°):", seno_45);
print("cos(45°):", coseno_45);

# ----------------------------
# 2. MATRICES
# ----------------------------
print("\n--- 2. Operaciones con Matrices ---");

A = [[2, 3], [1, 4]];
B = [[5, 2], [1, 3]];

print("Matriz A:", A);
print("Matriz B:", B);

# Suma
C = matriz.suma(A, B);
print("A + B =", C);

# Multiplicación
D = matriz.multiplicar(A, B);
print("A * B =", D);

# Determinante
det_A = matriz.determinante(A);
print("det(A) =", det_A);

# ----------------------------
# 3. CONDICIONALES Y BUCLES
# ----------------------------
print("\n--- 3. Control de Flujo ---");

# Clasificación de números
numeros = [15, 28, 33, 42, 51, 67, 73, 88, 95];
print("Números:", numeros);

contador_pares = 0;
contador_impares = 0;

for (i in range(0, 9)) {
    # Simulación de acceso (en práctica real usaríamos indexación)
    if (i == 0) { 
        num = 15; 
    }
    if (i == 1) { num = 28; }
    if (i == 2) { 
        num = 33; 
        
    }
    if (i == 3) { num = 42; }
    if (i == 4) { num = 51; }
    if (i == 5) { num = 67; }
    if (i == 6) { num = 73; }
    if (i == 7) { num = 88; }
    if (i == 8) { num = 95; }
    
    resto = mod(num, 2);
    
    if (resto == 0) {
        contador_pares = contador_pares + 1;
    } else {
        contador_impares = contador_impares + 1;
    }
}

print("Números pares:", contador_pares);
print("Números impares:", contador_impares);

# ----------------------------
# 4. REGRESIÓN LINEAL
# ----------------------------
print("\n--- 4. Regresión Lineal ---");

# Datos: Horas de estudio vs Calificación
horas = [1, 2, 3, 4, 5, 6, 7, 8];
calificaciones = [50, 55, 65, 70, 75, 85, 90, 95];

print("Horas de estudio:", horas);
print("Calificaciones:", calificaciones);

# Crear y entrenar modelo
modelo_reg = RegresionLineal();
modelo_reg.fit(horas, calificaciones);

# Métricas
r2_score = modelo_reg.r2();
rmse_score = modelo_reg.rmse();

print("R² Score:", r2_score);
print("RMSE:", rmse_score);

# Predicción
horas_futuras = [9, 10];
predicciones = modelo_reg.predict(horas_futuras);
print("Predicción para 9-10 horas:", predicciones);

# Visualizar
print("\nGráfica de Regresión:");
modelo_reg.plot(width=60, height=15, title="Horas vs Calificacion");

# ----------------------------
# 5. TABLA DE RESULTADOS
# ----------------------------
print("\n--- 5. Tabla de Resultados ---");

resultados = [
    [1, "Matemáticas", area],
    [2, "Det(A)", det_A],
    [3, "R² Score", r2_score],
    [4, "RMSE", rmse_score]
];

mostrar_tabla(resultados, max_rows=10, show_index=True);

# ----------------------------
# 6. RESUMEN FINAL
# ----------------------------
print("\n--- Resumen del Análisis ---");
print("Total de operaciones: 5 módulos");
print("1. Cálculos matemáticos: OK");
print("2. Operaciones matriciales: OK");
print("3. Control de flujo: OK");
print("4. Regresión lineal: OK");
print("5. Visualización de datos: OK");

print("\n✓ Análisis completado exitosamente");