#Ciclo FOR

# Escribir un programa que pida al usuario un número entero y muestre por pantalla si 
# es un número primo o no.

n = int(input('Introduzca un número mayor que 2: '))
for i in range(2, n):
    if (n % i == 0):
        break
if(i + 1) == n:
    print(str(n),"es primo")
else:
    print(str(n),"no es primo")
    
# DIV = /
# MOD = %
# Y = and
# O = or
#No = not