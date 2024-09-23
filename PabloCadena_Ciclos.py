print("Bienvenido a la tienda online RunFusion, donde encontraras todo sobre tus productos deportivos")

def menu():
    print("\n**** Menu de Opciones ****")
    print("1. Ver lista de productos")
    print("2. Ver referencia productos")
    print("3. Iniciar compra")
    print("4. Realizar otro pedido")
    print("5. Salir del sitio Web")
    print("\n ************************************")

cliente = input("Por favor ingrese su nombre: ") .capitalize()

listaProductos = { "Zapatos" : {"1.1 Ascis" : 1500000, "1.2 Adidas": 800000, "1.3 Reebok": 600000, "1.4 Nike": 700000, "1.5 On Cloudrunner": 400000},
                 "Gorras" : {"2.1 Ascis": 20000, "2.2 Salmon": 30000, "2.3 Nike":40000},
                 "Geles":{"3.1 Going":15000, "3.2 PX":20000, "3.3 Gu":10000}
                 }

def recorrerLista():
    print("1. CATEGORIA ZAPATOS:")
    for clave, valor in listaProductos["Zapatos"].items():
        print(" "f"{clave}: {valor}")
    print("2. CATEGORIA GORRAS:")
    for clave, valor in listaProductos["Gorras"].items():
        print(" "f"{clave}: {valor}")
    print("3. CATEGORIA GELES:")
    for clave, valor in listaProductos["Geles"].items():
        print(" "f"{clave}: {valor}")

def refProductos():
    catCompra = input(f"Por favor {cliente} digite el numero de la categoria que desea revisar: ")
    if catCompra == '1':
        print("Refererencia de las marcas de esta categoria")
        print(" ""Ascis = Rerencia No. 1.1 \n Adidas = Rerencia No. 1.2 \n Reebok = Rerencia No. 1.3 \n Nike = Rerencia No. 1.4 \n On Cloudrunner = Rerencia No. 1.5")
    elif catCompra == '2':
        print("Refererencia de las marcas de esta categoria")
        print(" ""Ascis = Rerencia No. 2.1 \n Salmon = Rerencia No. 2.2 \n Nike = Rerencia No. 2.3")
    elif catCompra == '3':
        print("Refererencia de las marcas de esta categoria")
        print(" ""Going= Rerencia No. 3.1 \n PX = Rerencia No. 3.2 \n Gu = Rerencia No. 2.3")

cantCompra = int(input(f"Por favor {cliente} cantidad de productos a comprar hoy: "))

def cobro():
    total_amount = 0
    for i in range(1,cantCompra+1):
        refProducto = input(f"{cliente} Digite el codigo del producto {i} a comprar: ")
        cantidad = int(input(f"{cliente} Digite la cantidad de productos de la compra {i} que: "))
        if refProducto == '1.1':
            precio = listaProductos["Zapatos"].get('1.1 Ascis')
            print(f"El valor unitario del producto {i} es de: {precio}")
            subtotal = {precio * cantidad}
            total_amount += subtotal
            print(f"El valor total la cantidad pedida es de: {subtotal}")
        elif refProducto == '1.2':
            precio = listaProductos["Zapatos"].get('1.2 Adidas')
            print(f"El valor unitario del producto {i} es de: {precio}")
            subtotal2 = {precio * cantidad}
            print(f"El valor total la cantidad pedida es de: {subtotal2}")
        elif refProducto == '1.3':
            precio = listaProductos["Zapatos"].get('1.3 Reebok')
            print(f"El valor unitario del producto {i} es de: {precio}")
            subtotal3 = {precio * cantidad}
            print(f"El valor total la cantidad pedida es de: {subtotal3}")
        elif refProducto == '1.4':
            precio = listaProductos["Zapatos"].get('1.4 Nike')
            print(f"El valor unitario del producto {i} es de: {precio}")
            subtotal4 = {precio * cantidad}
            print(f"El valor total la cantidad pedida es de: {subtotal4}")
        elif refProducto == '1.5':
            precio = listaProductos["Zapatos"].get('1.5 On Cloudrunner')
            print(f"El valor unitario del producto {i} es de: {precio}")
            subtotal5 = {precio * cantidad}
            print(f"El valor total la cantidad pedida es de: {subtotal5}")
        elif refProducto == '2.1':
            precio = listaProductos["Gorras"].get('2.1 Ascis')
            print(f"El valor unitario del producto {i} es de: {precio}")
            subtotal6 = {precio * cantidad}
            print(f"El valor total la cantidad pedida es de: {subtotal6}")
        elif refProducto == '2.2':
            precio = listaProductos["Gorras"].get('2.2 Salmon')
            print(f"El valor unitario del producto {i} es de: {precio}")
            subtotal7 = {precio * cantidad}
            print(f"El valor total la cantidad pedida es de: {subtotal7}")
        elif refProducto == '2.3':
            precio = listaProductos["Gorras"].get('2.3 Nike')
            print(f"El valor unitario del producto {i} es de: {precio}")
            subtotal8 = {precio * cantidad}
            print(f"El valor total la cantidad pedida es de: {subtotal8}")
        elif refProducto == '3.1':
            precio = listaProductos["Geles"].get('3.1 Going')
            print(f"El valor unitario del producto {i} es de: {precio}")
            subtotal9 = {precio * cantidad}
            print(f"El valor total la cantidad pedida es de: {subtotal9}")
        elif refProducto == '3.2':
            precio = listaProductos["Geles"].get('3.2 PX')
            print(f"El valor unitario del producto {i} es de: {precio}")
            subtotal10 = {precio * cantidad}
            print(f"El valor total la cantidad pedida es de: {subtotal10}")
        elif refProducto == '3.3':
            precio = listaProductos["Geles"].get('3.3 Going')
            print(f"El valor unitario del producto {i} es de: {precio}")
            subtototal11 = {precio * cantidad}
            print(f"El valor total la cantidad pedida es de: {subtototal11}")
            i += 1
            totalPagar1 = {subtotal1 + subtotal2 + subtotal3 + subtotal4 + subtotal5 + subtotal6 + subtotal7 + subtotal8 + subtotal9 + subtotal10 + subtototal11}
            print(f"El cliente {cliente} debe pagar un total de: {totalPagar1} pesos")
    while True:
        respuesta = input(f"Desea ingresar mas productos al pedidio? (Si - No): ").capitalize()
        if respuesta.strip() == "Si":
            refProducto = input(f"{cliente} Digite el codigo del producto {i} a comprar: ")
            cantidad = int(input(f"{cliente} Digite la cantidad de productos de la compra {i} que: "))
            if refProducto == '1.1':
                precio = listaProductos["Zapatos"].get('1.1 Ascis')
                print(f"El valor unitario del producto {i} es de: {precio}")
                subtotal1 = {precio * cantidad}
                print(f"El valor total la cantidad pedida es de: {subtotal1}")
            elif refProducto == '1.2':
                precio = listaProductos["Zapatos"].get('1.2 Adidas')
                print(f"El valor unitario del producto {i} es de: {precio}")
                subtotal2 = {precio * cantidad}
                print(f"El valor total la cantidad pedida es de: {subtotal2}")
            elif refProducto == '1.3':
                precio = listaProductos["Zapatos"].get('1.3 Reebok')
                print(f"El valor unitario del producto {i} es de: {precio}")
                subtotal3 = {precio * cantidad}
                print(f"El valor total la cantidad pedida es de: {subtotal3}")
            elif refProducto == '1.4':
                precio = listaProductos["Zapatos"].get('1.4 Nike')
                print(f"El valor unitario del producto {i} es de: {precio}")
                subtotal4 = {precio * cantidad}
                print(f"El valor total la cantidad pedida es de: {subtotal4}")
            elif refProducto == '1.5':
                precio = listaProductos["Zapatos"].get('1.5 On Cloudrunner')
                print(f"El valor unitario del producto {i} es de: {precio}")
                subtotal5 = {precio * cantidad}
                print(f"El valor total la cantidad pedida es de: {subtotal5}")
            elif refProducto == '2.1':
                precio = listaProductos["Gorras"].get('2.1 Ascis')
                print(f"El valor unitario del producto {i} es de: {precio}")
                subtotal6 = {precio * cantidad}
                print(f"El valor total la cantidad pedida es de: {subtotal6}")
            elif refProducto == '2.2':
                precio = listaProductos["Gorras"].get('2.2 Salmon')
                print(f"El valor unitario del producto {i} es de: {precio}")
                subtotal7 = {precio * cantidad}
                print(f"El valor total la cantidad pedida es de: {subtotal7}")
            elif refProducto == '2.3':
                precio = listaProductos["Gorras"].get('2.3 Nike')
                print(f"El valor unitario del producto {i} es de: {precio}")
                subtotal8 = {precio * cantidad}
                print(f"El valor total la cantidad pedida es de: {subtotal8}")
            elif refProducto == '3.1':
                precio = listaProductos["Geles"].get('3.1 Going')
                print(f"El valor unitario del producto {i} es de: {precio}")
                subtotal9 = {precio * cantidad}
                print(f"El valor total la cantidad pedida es de: {subtotal9}")
            elif refProducto == '3.2':
                precio = listaProductos["Geles"].get('3.2 PX')
                print(f"El valor unitario del producto {i} es de: {precio}")
                subtotal10 = {precio * cantidad}
                print(f"El valor total la cantidad pedida es de: {subtotal10}")
            elif refProducto == '3.3':
                precio = listaProductos["Geles"].get('3.3 Going')
                print(f"El valor unitario del producto {i} es de: {precio}")
                subtototal11 = {precio * cantidad}
                print(f"El valor total la cantidad pedida es de: {subtototal11}")
                i += 1
                totalPagar2 = {subtotal1 + subtotal2 + subtotal3 + subtotal4 + subtotal5 + subtotal6 + subtotal7 + subtotal8 + subtotal9 + subtotal10 + subtototal11}
                print(f"El cliente {cliente} debe pagar un total de: {totalPagar1 + totalPagar2} pesos")
            else:
                print(f"El cliente {cliente} debe pagar un total de: {totalPagar1} pesos")
        else:
            print(f"El cliente {cliente} debe pagar un total de: {totalPagar1} pesos")
            print(f"Fin del encargo")



while True:
    menu()
    opcion = input("Seleccione una opcion y coloque el numero de esta: ")
    if opcion == "1":
        recorrerLista()
    elif opcion == "2":
        refProductos()
    elif opcion == "3":
        cobro()
    #elif opcion == "4":
        
    elif opcion == "5":
        print("GRACIAS POR SU VISITA, ESPERAMOS PODERLO AYUDAR EN UNA PROXIMA OPORTUNIDAD")
        break
    else:
        print("Opcion no valida, seleccione una opcion del menu")








