#Las combinaciones o coeficientes binomiales son una serie de números que indican 
#la cantidad de formas en que se pueden extraer subconjuntos a partir de un 
# conjunto dado. Para calcular combinaciones se debe utilizar la siguiente fórmula:

#C = n! / m! * (n-m)!

#Crear la función factorial
def factorial(num):
    f = 1
    for i in range(1, num+1):
        f = f * i
    return f

#Programa principal
n = int(input('Tamaño del conjunto: '))
m = int(input('Tamaño del grupo a crear: '))
nf = factorial(n)
mf = factorial(m)
nmf = factorial(n-m)
c = nf / (mf * nmf)
print('La cantidad de combinaciones es: ',c)
