#Nombre del algoritmo: Hallar el número de micro-discos de 3.5

import math, os
os.system('cls')

#Entrada
print('Ingrese GB: ')
GB = float(input())

#Proceso
MG = GB * 1024
MD = MG / 1.44

#Salida
print("\nResultado Final: ")
print('*************************************************************')
print('Número de discos necesarios: ',math.ceil(MD))