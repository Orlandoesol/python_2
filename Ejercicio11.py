cn = 0
cpos = 0
cneg = 0

n = int(input('Cantidad de números: '))
for i in range(n):
    num = int(input(f'Número {(i+1)}: '))
    if(num == 0):
        cn +=1
    elif(num > 0):
        cpos +=1
    else:
        cneg +=1

print('Cantidad de positivos: ',cpos)
print('Cantidad de negativos: ',cneg)
print('Cantidad de neutros: ',cn)