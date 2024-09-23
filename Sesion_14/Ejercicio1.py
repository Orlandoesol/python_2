#Nombre del algoritmo: Puntaje total del equipo ABC Futbol Club
import os
os.system('cls')

print('*************************************************************')
print('*********** Ejercicio: PUNTAJE TOTAL DE PARTIDOS ************')
print('*************************************************************')

#Entradas:
print('Ingrese número de partidos ganados: ')
PG = int(input())
print('Ingrese número de partidos empatados: ')
PE = int(input())
print('Ingrese número de partidos perdidos: ')
PP = int(input())

#Proceso
PPG = PG * 3
PPE = PE * 1
PPP = PP * 0
PF = PPG + PPE + PPP

#Salida
print("\nResultado Final: ")
print('*************************************************************')
print('El puntaje del club ABC es: ', PF)