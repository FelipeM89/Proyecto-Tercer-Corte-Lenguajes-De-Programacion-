"""
LibreriaKMeans.py
Implementación de K-Means clustering sin dependencias externas
"""

from Librerias.LibreriaAritmetica import LCG, sqrt


class KMeans:
    def __init__(self, n_clusters=3, max_iter=100, seed=1234):
        """
        Inicializa K-Means
        
        Args:
            n_clusters: Número de clusters
            max_iter: Máximo de iteraciones
            seed: Semilla para generación aleatoria
        """
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.seed = seed
        self.rng = LCG(seed)
        self.centroids = None
        self.labels = None
        self.data = None
    
    def _distancia_euclidiana(self, p1, p2):
        """Calcula distancia euclidiana entre dos puntos"""
        if len(p1) != len(p2):
            raise ValueError("Los puntos deben tener la misma dimensión")
        
        suma = 0.0
        for i in range(len(p1)):
            suma += (p1[i] - p2[i]) ** 2
        
        return sqrt(suma)
    
    def _inicializar_centroides(self, X):
        """Inicializa centroides aleatoriamente desde los datos"""
        n = len(X)
        indices = []
        
        # Seleccionar n_clusters índices únicos aleatorios
        while len(indices) < self.n_clusters:
            idx = self.rng.randint(0, n - 1)
            if idx not in indices:
                indices.append(idx)
        
        # Copiar puntos seleccionados como centroides
        centroids = []
        for idx in indices:
            centroids.append(X[idx][:])  # Copia del punto
        
        return centroids
    
    def _asignar_clusters(self, X):
        """Asigna cada punto al centroide más cercano"""
        labels = []
        
        for punto in X:
            distancias = []
            for centroid in self.centroids:
                dist = self._distancia_euclidiana(punto, centroid)
                distancias.append(dist)
            
            # Encontrar el índice del centroide más cercano
            min_dist = distancias[0]
            min_idx = 0
            for i in range(1, len(distancias)):
                if distancias[i] < min_dist:
                    min_dist = distancias[i]
                    min_idx = i
            
            labels.append(min_idx)
        
        return labels
    
    def _actualizar_centroides(self, X, labels):
        """Recalcula centroides como la media de los puntos asignados"""
        dim = len(X[0])
        nuevos_centroides = []
        
        for k in range(self.n_clusters):
            # Encontrar todos los puntos asignados al cluster k
            puntos_cluster = []
            for i in range(len(X)):
                if labels[i] == k:
                    puntos_cluster.append(X[i])
            
            if len(puntos_cluster) == 0:
                # Si no hay puntos, mantener el centroide anterior
                nuevos_centroides.append(self.centroids[k][:])
            else:
                # Calcular la media de cada dimensión
                nuevo_centroid = []
                for d in range(dim):
                    suma = 0.0
                    for punto in puntos_cluster:
                        suma += punto[d]
                    nuevo_centroid.append(suma / len(puntos_cluster))
                
                nuevos_centroides.append(nuevo_centroid)
        
        return nuevos_centroides
    
    def _centroides_cambiaron(self, viejos, nuevos, tol=1e-6):
        """Verifica si los centroides cambiaron significativamente"""
        for i in range(len(viejos)):
            dist = self._distancia_euclidiana(viejos[i], nuevos[i])
            if dist > tol:
                return True
        return False
    
    def fit(self, X):
        """
        Entrena el modelo K-Means
        
        Args:
            X: Lista de puntos, donde cada punto es una lista de coordenadas
               Ejemplo: [[1, 2], [3, 4], [5, 6]]
        """
        if not X or not X[0]:
            raise ValueError("Los datos de entrada no pueden estar vacíos")
        
        self.data = [punto[:] for punto in X]  # Copia de los datos
        
        # Inicializar centroides
        self.centroids = self._inicializar_centroides(X)
        
        # Algoritmo iterativo
        for iteracion in range(self.max_iter):
            # Asignar puntos a clusters
            self.labels = self._asignar_clusters(X)
            
            # Actualizar centroides
            nuevos_centroides = self._actualizar_centroides(X, self.labels)
            
            # Verificar convergencia
            if not self._centroides_cambiaron(self.centroids, nuevos_centroides):
                print(f"K-Means convergió en {iteracion + 1} iteraciones")
                break
            
            self.centroids = nuevos_centroides
        
        return self
    
    def predict(self, X):
        """
        Predice el cluster para nuevos puntos
        
        Args:
            X: Lista de puntos a clasificar
        
        Returns:
            Lista de etiquetas de cluster
        """
        if self.centroids is None:
            raise ValueError("El modelo no ha sido entrenado. Llama a fit() primero.")
        
        return self._asignar_clusters(X)
    
    def plot_clusters(self, width=80, height=20):
        """
        Genera una visualización ASCII de los clusters (solo para 2D)
        
        Returns:
            String con la gráfica ASCII
        """
        if self.data is None or self.labels is None:
            return "No hay datos para graficar. Entrena el modelo primero."
        
        if len(self.data[0]) != 2:
            return "La visualización solo está disponible para datos 2D"
        
        # Extraer coordenadas X e Y
        xs = [punto[0] for punto in self.data]
        ys = [punto[1] for punto in self.data]
        
        # Rangos
        xmin, xmax = min(xs), max(xs)
        ymin, ymax = min(ys), max(ys)
        
        # Padding
        if xmax == xmin:
            xmin -= 0.5
            xmax += 0.5
        if ymax == ymin:
            ymin -= 0.5
            ymax += 0.5
        
        xpad = (xmax - xmin) * 0.05
        ypad = (ymax - ymin) * 0.05
        xmin -= xpad
        xmax += xpad
        ymin -= ypad
        ymax += ypad
        
        # Grid
        grid = [[' ' for _ in range(width)] for _ in range(height)]
        
        # Caracteres para cada cluster
        chars = ['*', 'o', '+', 'x', '#', '@', '%', '&']
        
        # Dibujar puntos
        for i, punto in enumerate(self.data):
            x, y = punto[0], punto[1]
            cluster = self.labels[i]
            char = chars[cluster % len(chars)]
            
            # Mapear a grid
            col = int((x - xmin) / (xmax - xmin) * (width - 1))
            row = int((ymax - y) / (ymax - ymin) * (height - 1))
            
            col = max(0, min(width - 1, col))
            row = max(0, min(height - 1, row))
            
            grid[row][col] = char
        
        # Dibujar centroides
        for i, centroid in enumerate(self.centroids):
            x, y = centroid[0], centroid[1]
            col = int((x - xmin) / (xmax - xmin) * (width - 1))
            row = int((ymax - y) / (ymax - ymin) * (height - 1))
            
            col = max(0, min(width - 1, col))
            row = max(0, min(height - 1, row))
            
            grid[row][col] = str(i)  # Centroide marcado con su número
        
        # Construir output
        lines = ["=== K-Means Clusters ==="]
        lines.append(f"Clusters: {self.n_clusters}")
        lines.append("")
        
        for row in grid:
            lines.append(''.join(row))
        
        lines.append("")
        lines.append("Leyenda:")
        for i in range(self.n_clusters):
            char = chars[i % len(chars)]
            lines.append(f"  Cluster {i}: {char}  (Centroide: {i})")
        
        return '\n'.join(lines)


# Ejemplo de uso
if __name__ == "__main__":
    # Datos de ejemplo (2D)
    datos = [
        [1.0, 2.0], [1.5, 1.8], [5.0, 8.0],
        [8.0, 8.0], [1.0, 0.6], [9.0, 11.0],
        [8.0, 2.0], [10.0, 2.0], [9.0, 3.0]
    ]
    
    # Crear y entrenar modelo
    kmeans = KMeans(n_clusters=3, max_iter=100, seed=42)
    kmeans.fit(datos)
    
    print("Centroides finales:")
    for i, c in enumerate(kmeans.centroids):
        print(f"  Cluster {i}: {c}")
    
    print("\nEtiquetas:")
    print(kmeans.labels)
    
    print("\nVisualización:")
    print(kmeans.plot_clusters())
    
    # Predecir nuevos puntos
    nuevos = [[0.0, 0.0], [8.0, 9.0]]
    pred = kmeans.predict(nuevos)
    print(f"\nPredicciones para {nuevos}: {pred}")