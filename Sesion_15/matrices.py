import numpy as np
import time


# Definir las matrices
matriz1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

matriz2 = np.array([
    [7, 8, 9],
    [10, 11, 12]
]) 


# Medir el tiempo de ejecución
start_time = time.time()

# Sumar las matrices
matriz_resultado = matriz1 + matriz2

end_time = time.time()

# Imprimir el resultado
print("Resultado de la suma:")
print(matriz_resultado)

# Imprimir el tiempo de ejecución
print(f"Tiempo de ejecución: {end_time - start_time} segundos")

# Convertir el tiempo de ejecución a milisegundos
execution_time_ms = (end_time - start_time) * 1000
print(f"Tiempo de ejecución: {execution_time_ms:.6f} milisegundos")