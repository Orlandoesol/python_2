#   Cree dos listas: Productos y Precios y realice un menú en el cual:
#   muestre, elimine, agregue y realice la operación de una compra.
import os

listaProductos = []
listaPrecios = []

def fnt_limpiarpantalla():
    os.system('cls')

def agregar():
    print('Agregar producto')
    producto = input('Ingrese el producto: ').capitalize()
    listaProductos.append(producto)
    precio = float(input('Precio, $:'))
    listaPrecios.append(precio)
    
def mostrar():
    for i in range(len(listaProductos)):
        print('-'+listaProductos[i],": $",listaPrecios[i])
    
def eliminar():
    print('Eliminar producto')
    producto = input('Ingrese el producto a eliminar: ')
    indice = listaProductos.index(producto)
    listaProductos.remove(producto)
    listaPrecios.pop(indice)
        

def menu():
    print('1 - Agregar producto')
    print('2 - Mostrar productos')
    print('3 - Eliminar productos')
    print('4 - Total compra')
    print('5 - Salir')
    
#Programa principal
control = True
while control:
    fnt_limpiarpantalla()
    menu()
    op = int(input('Elija la opción a realizar: '))
    if op == 1:
        fnt_limpiarpantalla()
        agregar()
        print('Su producto ha sido agregado!')
        input('Presione <ENTER> para continuar...')
    elif op == 2:
        fnt_limpiarpantalla()
        print('Listado de productos')
        mostrar()
        input('Presione <ENTER> para continuar...')
    elif op == 3:
        fnt_limpiarpantalla()
        eliminar()
        print('Su producto ha sido eliminado')
        input('Presione <ENTER> para continuar...')
    elif op == 4:
        fnt_limpiarpantalla()
        print('Total de la compra')
        mostrar()
        print('Total $',sum(listaPrecios))
        input('Presione <ENTER para continuar...')
    elif op == 5:
        print('Salir')
        control = False
    else:
        print('Opción incorrecta, intente de nuevo!')
        input('Presione <ENTER> para continuar...')        