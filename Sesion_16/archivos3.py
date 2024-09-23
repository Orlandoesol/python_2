#Diseña un programa con las siguientes características:

#Que tenga una función caja que 
#    a. Cree un archivo factura.txt
#    b. Solicite al usuario nombre y precio de cada producto.
#    c. Una función adicional llamada guardaProducto(nombre, precio, archivo) que reciba el nombre 
#       y el precio de cada producto y los escriba en el archivo factura.txt
#    d. Que después de llamar a guardaProducto le pregunte al usuario si tiene o no más artículos 
#       a ingresar. Si no tiene, el programa debe detenerse.

def guardaProducto(nombre, precio, archivo):
    archivo.writelines('Producto: '+ nombre +", precio $"+str(precio)+'\r')

def caja():
    archivo = open('C:/ficheros/factura.txt', mode='a', encoding='utf-8')
    nombre = input('Nombre del producto: ')
    precio = input('Precio de: '+nombre+', $')
    guardaProducto(nombre, precio, archivo)
    continuar = True
    while continuar:
        pregunta = input('¿Desea ingresar más productos? (SI o NO): ')
        if(pregunta == 'SI' or pregunta == 'si'):
            nombre = input('Nombre del producto: ')
            precio = input('Precio de: '+nombre+', $')
            guardaProducto(nombre, precio, archivo)
        else:
            break
   
#Programa principal
caja()