#Taller2-Saramyplaza.py

import statistics

def lista_inversa():
    lista = list(range(1, 21))
    print("Lista en orden inverso:", '-'.join(map(str, lista[::-1])))

def asignaturas():
    asignaturas = []
    notas = []
    while True:
        asignatura = input("Introduce el nombre de una asignatura (o 'fin' para terminar): ")
        if asignatura.lower() == 'fin':
            break
        asignaturas.append(asignatura)
        nota = float(input(f"Introduce la nota de {asignatura}: "))
        notas.append(nota)
    
    # Filtrar asignaturas no aprobadas
    asignaturas_repetir = [asignatura for asignatura, nota in zip(asignaturas, notas) if nota < 3.5]
    
    print("Asignaturas que debes repetir:", ', '.join(asignaturas_repetir))

def estadisticas_muestra():
    muestra = input("Introduce una muestra de números separados por comas: ")
    numeros = list(map(float, muestra.split(',')))
    
    promedio = statistics.mean(numeros)
    desviacion = statistics.stdev(numeros) if len(numeros) > 1 else 0.0
    
    print(f"Promedio: {promedio:.2f}")
    print(f"Desviación típica: {desviacion:.2f}")

def menu_listas():
    while True:
        print("\nMenú Listas:")
        print("1. Mostrar números del 1 al 20 en orden inverso")
        print("2. Eliminar asignaturas aprobadas")
        print("3. Calcular promedio y desviación típica de una muestra")
        print("4. Menú de operaciones con listas")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            lista_inversa()
        elif opcion == '2':
            asignaturas()
        elif opcion == '3':
            estadisticas_muestra()
        elif opcion == '4':
            menu_operaciones_listas()
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_operaciones_listas():
    lista = []
    
    while True:
        print("\nMenú Operaciones con Listas:")
        print("1. Añadir número a la lista")
        print("2. Añadir número en una posición")
        print("3. Longitud de la lista")
        print("4. Eliminar el último número")
        print("5. Eliminar un número por posición")
        print("6. Contar apariciones de un número")
        print("7. Posiciones de un número")
        print("8. Mostrar números")
        print("9. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            num = int(input("Introduce el número a añadir: "))
            lista.append(num)
        elif opcion == '2':
            num = int(input("Introduce el número a añadir: "))
            pos = int(input("Introduce la posición (a partir de 1): ")) - 1
            if 0 <= pos <= len(lista):
                lista.insert(pos, num)
            else:
                print("Posición no válida.")
        elif opcion == '3':
            print("Longitud de la lista:", len(lista))
        elif opcion == '4':
            if lista:
                print("Último número eliminado:", lista.pop())
            else:
                print("La lista está vacía.")
        elif opcion == '5':
            pos = int(input("Introduce la posición (a partir de 1): ")) - 1
            if 0 <= pos < len(lista):
                print("Número eliminado:", lista.pop(pos))
            else:
                print("Posición no válida.")
        elif opcion == '6':
            num = int(input("Introduce el número a contar: "))
            print("Apariciones:", lista.count(num))
        elif opcion == '7':
            num = int(input("Introduce el número para buscar posiciones: "))
            posiciones = [i+1 for i, x in enumerate(lista) if x == num]
            print("Posiciones:", ', '.join(map(str, posiciones)) if posiciones else "Número no encontrado.")
        elif opcion == '8':
            print("Números en la lista:", ', '.join(map(str, lista)))
        elif opcion == '9':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def diccionario_persona():
    persona = {}
    
    while True:
        clave = input("Introduce el dato a añadir (nombre, edad, dirección, teléfono, correo electrónico) o 'fin' para terminar: ")
        if clave.lower() == 'fin':
            break
        valor = input(f"Introduce el valor para {clave}: ")
        persona[clave] = valor
        print("Contenido del diccionario:", persona)

def cesta_compra():
    cesta = {}
    
    while True:
        articulo = input("Introduce el nombre del artículo (o 'fin' para terminar): ")
        if articulo.lower() == 'fin':
            break
        precio = float(input(f"Introduce el precio de {articulo}: "))
        cesta[articulo] = precio
    
    total = sum(cesta.values())
    print("\nLista de la compra:")
    for articulo, precio in cesta.items():
        print(f"{articulo}: ${precio:.2f}")
    print(f"Total: ${total:.2f}")

def agenda():
    agenda = {}
    
    while True:
        print("\nMenú Agenda:")
        print("1. Añadir/modificar contacto")
        print("2. Buscar contacto")
        print("3. Borrar contacto")
        print("4. Listar contactos")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            nombre = input("Introduce el nombre del contacto: ")
            if nombre in agenda:
                print(f"Teléfono actual de {nombre}: {agenda[nombre]}")
                modificar = input("¿Quieres modificar el número? (sí/no): ").lower()
                if modificar == 'sí':
                    telefono = input("Introduce el nuevo número de teléfono: ")
                    agenda[nombre] = telefono
            else:
                telefono = input("Introduce el número de teléfono: ")
                agenda[nombre] = telefono
            print("Agenda actual:", agenda)
        
        elif opcion == '2':
            cadena = input("Introduce una cadena para buscar contactos: ")
            contactos = [nombre for nombre in agenda if nombre.startswith(cadena)]
            if contactos:
                print("Contactos encontrados:", ', '.join(contactos))
            else:
                print("No se encontraron contactos.")
        
        elif opcion == '3':
            nombre = input("Introduce el nombre del contacto a borrar: ")
            if nombre in agenda:
                confirmar = input(f"¿Quieres borrar a {nombre}? (sí/no): ").lower()
                if confirmar == 'sí':
                    del agenda[nombre]
                    print("Contacto borrado.")
                else:
                    print("No se borró el contacto.")
            else:
                print("Contacto no encontrado.")
        
        elif opcion == '4':
            if agenda:
                print("Lista de contactos:")
                for nombre, telefono in agenda.items():
                    print(f"{nombre}: {telefono}")
            else:
                print("La agenda está vacía.")
        
        elif opcion == '5':
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_diccionarios():
    while True:
        print("\nMenú Diccionarios:")
        print("1. Crear un diccionario de persona")
        print("2. Crear una cesta de la compra")
        print("3. Implementar una agenda")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            diccionario_persona()
        elif opcion == '2':
            cesta_compra()
        elif opcion == '3':
            agenda()
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def main():
    while True:
        print("\nMenú Principal:")
        print("1. Menú Listas")
        print("2. Menú Diccionarios")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            menu_listas()
        elif opcion == '2':
            menu_diccionarios()
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()