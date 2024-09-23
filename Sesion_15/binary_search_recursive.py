def binary_search_recursive(arr, target, low, high):
    # Caso base: el rango de búsqueda se vuelve inválido
    if low > high:
        return -1
    
    # Calcular el punto medio
    mid = (low + high) // 2
    
    # Verificar si el objetivo está en el punto medio
    if arr[mid] == target:
        return mid
    # Si el objetivo es menor que el punto medio, buscar en la mitad izquierda
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    # Si el objetivo es mayor que el punto medio, buscar en la mitad derecha
    else:
        return binary_search_recursive(arr, target, mid + 1, high)

# Función principal para iniciar la búsqueda
def binary_search(arr, target):
    return binary_search_recursive(arr, target, 0, len(arr) - 1)

# Ejemplo de uso
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7

# Llamada a la función principal de búsqueda binaria
index = binary_search(arr, target)

print(f"Índice de {target}: {index}")  # Debería imprimir 3, ya que 7 está en el índice 3