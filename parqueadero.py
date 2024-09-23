from datetime import datetime

# Inicialización del parqueadero
vehiculos = [f'v{i+1}' for i in range(50)]
motos = [f'm{i+1}' for i in range(25)]
parqueadero = [['.' for _ in range(10)] for _ in range(5)] + [['.' for _ in range(10)] for _ in range(3)]

# Variables para tarifas
tarifa_vehiculo = 1000  # tarifa por hora para vehículos
tarifa_moto = 800       # tarifa por hora para motos
descuento = 0.15        # 15% de descuento

# Registro de vehículos y alquileres
registros = {}
alquileres = {}

def mostrar_matriz():
    print("\nMatriz del Parqueadero:")
    for i in range(len(parqueadero)):
        if i < 5:
            print(" ".join(vehiculos[i*10:(i+1)*10]))
        else:
            print(" ".join(motos[(i-5)*10:(i-4)*10]))
    print("\nEstado Actual:")
    for fila in parqueadero:
        print(" ".join(fila))
    print("***************************************")

def alquilar_espacio(placa, tipo):
    if tipo == "vehiculo":
        espacios = vehiculos
        letra = 'A'
    elif tipo == "moto":
        espacios = motos
        letra = 'A'
    else:
        print("Tipo de vehículo no válido.")
        return

    for i in range(len(espacios)):
        if parqueadero[i//10][i%10] == '.':
            parqueadero[i//10][i%10] = letra
            alquileres[placa] = (espacios[i], letra)
            print(f"Espacio alquilado: {espacios[i]} para la placa {placa}.")
            return
    
    print("No hay espacios disponibles para alquilar.")

def registrar_entrada(placa, tipo):
    if tipo == "vehiculo":
        espacios = vehiculos
        tarifa = tarifa_vehiculo
    elif tipo == "moto":
        espacios = motos
        tarifa = tarifa_moto
    else:
        print("Tipo de vehículo no válido.")
        return

    for i in range(len(espacios)):
        if parqueadero[i//10][i%10] == '.':
            parqueadero[i//10][i%10] = 'O'
            registros[placa] = (espacios[i], datetime.now(), tarifa)
            print(f"Vehículo registrado: {espacios[i]} para la placa {placa}.")
            return
    
    print("No hay espacios disponibles para registrar el vehículo.")

def registrar_salida(placa):
    if placa in registros:
        espacio, entrada, tarifa = registros[placa]
        tiempo_ocupado = datetime.now() - entrada
        horas = int(tiempo_ocupado.total_seconds() / 3600) + (1 if tiempo_ocupado.seconds % 3600 > 0 else 0)

        # Cálculo de la tarifa
        costo = horas * tarifa
        if horas > 4:  # Aplica descuento si ocupó más del 70% de la jornada
            jornada = 16  # 6am a 10pm
            if horas >= (jornada * 0.7):
                costo -= costo * descuento
                print("Se aplica un 15% de descuento.")
        
        print(f"La factura para la placa {placa} es: ${costo:.2f}")
        # Libera el espacio
        for i in range(len(vehiculos)):
            if vehiculos[i] == espacio:
                parqueadero[i//10][i%10] = '.'
                break
        del registros[placa]
    else:
        print("No se encontró registro para esta placa.")

def informe_ocupacion():
    vehiculos_ocupados = [v for v, estado in registros.items() if estado[0] in vehiculos]
    motos_ocupadas = [v for v, estado in registros.items() if estado[0] in motos]
    
    print(f"Vehículos: Alquilados (0), {', '.join(vehiculos_ocupados)}")
    print(f"Motos: Alquilados (0), {', '.join(motos_ocupadas)}")

def menu():
    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Mostrar matriz del parqueadero")
        print("2. Alquiler (entrada del vehículo por placa y tipo (vehículo o moto))")
        print("3. Registrar (hora entrada del vehículo por placa y tipo (vehículo o moto))")
        print("4. Registrar Salida de vehículo")
        print("5. Informe Ocupación")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_matriz()
        elif opcion == "2":
            placa = input("Ingrese la placa: ")
            tipo = input("Ingrese tipo (vehiculo/moto): ").lower()
            alquilar_espacio(placa, tipo)
        elif opcion == "3":
            placa = input("Ingrese la placa: ")
            tipo = input("Ingrese tipo (vehiculo/moto): ").lower()
            registrar_entrada(placa, tipo)
        elif opcion == "4":
            placa = input("Ingrese la placa: ")
            registrar_salida(placa)
        elif opcion == "5":
            informe_ocupacion()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    print("¡Bienvenido al sistema de gestión de parqueadero!")
    menu()




