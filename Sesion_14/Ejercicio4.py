#Algoritmo del método QuickSort (Ordenamiento Rápido)

#Función para el método QuickSort
def quickSort(array):
    if(len(array)) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quickSort(left) + middle + quickSort(right)


array = [3, 6, 8, 10, 1, 2, 1]
print('Arreglo inicial:\n ',array)
print('*************************************************************')
print('Arreglo ordenado mediante QuickSort:\n ',quickSort(array))
    