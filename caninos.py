import os

lista_caninos = []
control = True

while control:
    os.system('cls')
    opc = int(input('\nMENÚ DE OPCIONES\n1. Registrar canino\n2. Mostrar caninos\n3. Actualizar caninos\n4. Salir\n ->'))
    if opc == 1:
        os.system('cls')
        print('****************************************')
        print('******** Registro de caninos ***********')
        print('****************************************')
        nombre = input('Nombre del canino: ')
        edad = input('Edad del canino: ')
        raza = input('Raza del canino: ')
        registro = nombre + ' ' + edad + ' ' +raza
        lista_caninos.append(registro)
        enter = input('\nRegistro realizado con éxito <ENTER>')
    if opc == 2:
        os.system('cls')
        print('****************************************')
        print('********* Listado de caninos ***********')
        print('****************************************')
        for i in range(len(lista_caninos)):
            print((i+1),'->'+lista_caninos[i])
        enter = input('\n<ENTER>')
    if opc == 3:
        os.system('cls')
        print('***********************************')
        print('******* Actualizar caninos ********')
        print('***********************************')
        #Tarea
    if opc == 4:
        os.system('cls')
        print('Gracias por utilizar el programa')
        break 