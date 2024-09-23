#Algoritmo por el método BubbleSort (Ordenamiento por Burbuja)

#Función del método BubbleSort
def bubbleSort(array):
    n = len(array)
    for i in range(n):
        #Bandera para detectar si hubo un intercambio en esta pasada
        bandera = False
        #Ultimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            #Comparar el elemento actual con el siguiente
            if(array[j] > array[j+1]):
                #Intercambiar si están en el orden incorrecto
                array[j], array[j+1] = array[j+1], array[j]
                bandera = True
        #Si no hubo intercambios, el arreglo ya está ordenado
        if not bandera:
            break



array = [64, 34, 25, 12, 22, 11, 90]
print('Arreglo inicial:\n',array)
print('*************************************************************')
bubbleSort(array)
print('Arreglo ordenado:\n',array)