n = int(input('Cantidad de vendedores: '))
i = 0
while(i < n):
    nombre = input(f'Nombre del vendedor {(i+1)}: ')
    sb = float(input('Salario Base, $'))
    venta1 = float(input('Venta 1, $'))
    venta2 = float(input('Venta 2, $'))
    venta3 = float(input('Venta 3, $'))
    comisiones = (venta1 + venta2 + venta3) * 0.1
    neto = sb + comisiones
    print(f'El salario neto del vendedor',i+1,'que corresponde a: ',nombre,'es de $',neto)
    i+=1