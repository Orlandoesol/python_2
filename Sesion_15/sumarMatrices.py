import time

def sumar_matrices(matriz1, matriz2):
    # Verifica que las matrices tengan las mismas dimensiones
    if len(matriz1) != len(matriz2) or any(len(fila1) != len(fila2) for fila1, fila2 in zip(matriz1, matriz2)):
        raise ValueError("Las matrices deben tener las mismas dimensiones")
    
    # Inicializa la matriz resultante con ceros
    filas = len(matriz1)
    columnas = len(matriz1[0])
    matriz_resultado = [[0] * columnas for _ in range(filas)]
    
    # Suma las matrices
    for i in range(filas):
        for j in range(columnas):
            matriz_resultado[i][j] = matriz1[i][j] + matriz2[i][j]
    return matriz_resultado

# Ejemplo de uso
matriz1 = [
    [5, 8, 9],
    [4, 5, 6]
]

matriz2 = [
    [7, 8, 9],
    [10, 11, 12]
]

# Medir el tiempo de ejecución
start_time = time.time()
resultado = sumar_matrices(matriz1, matriz2)
end_time = time.time()
print("Resultado de la suma:")
for fila in resultado:
    print(fila)
    
# Convertir el tiempo de ejecución a milisegundos
execution_time_ms = (end_time - start_time) * 1000
print(f"Tiempo de ejecución: {execution_time_ms:.6f} milisegundos")