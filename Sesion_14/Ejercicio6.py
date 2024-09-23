#Algoritmo por el método Binary Search(Búsqueda binaria)

#Función del método Binary Search
def binarySearch(array, target):
    izq, der = 0, len(array) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if(array[medio] == target):
            return medio
        elif(array[medio] < target):
            izq = medio + 1
        else:
            der = medio - 1
    
    return -1


array = [4, 5, 29, 37, 56, 83, 100]
target = 56
print(binarySearch(array, target))