#Nombre del algoritmo: distancia entre los puntos A y B
import math, os
os.system('cls')

#Entrada
print('Ingrese las coordenadas del punto A: ')
AX = float(input('Ax: '))
AY = float(input('Ay: '))
print('Ingrese las coordenadas del punto B: ')
BX = float(input('Bx: '))
BY = float(input('By: '))

#Proceso
D = math.sqrt((math.pow(AX-BX, 2)) + (math.pow(AY-BY,2)))
#D = ( (AX-BX)** 2 + (AY-BY)**2 ) ** 0.5

#Salida
print("\nResultado Final: ")
print('*************************************************************')
print('La distancia es: ',D)