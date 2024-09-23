#Ejercicios con listas

#1. Pida números e incluyalos en una lista, cuando el usuario inserte el número cero (0), el 
#   programa dejará de hacerlo. Por último, muestra los números ordenados de menor a mayor.

import os
os.system('cls')

ListaNum = []
control = False

while not control:
    numero = int(input('Ingrese un número: '))
    if(numero == 0):
        control = True
    else:
        ListaNum.append(numero)

ListaNum.sort(reverse=True)
print('La lista de números: ')
print(ListaNum)