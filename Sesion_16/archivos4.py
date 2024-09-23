import os, time
nomArchivo = 'Estudiantes.dat'

def fnt_limpiarpantalla():
    try:
        if(os.name.upper()=='NT'):
            os.system('cls')
        else:
            os.system('clear')
    except Exception:
        pass

def esperar(tiempo=3,msg=None):
    try:
        if(msg != None):
            msg = f'{msg}. Por favor espere {tiempo} segundos para continuar'
            print(msg)
            time.sleep(tiempo)
    except Exception:
        pass

def add_registro():
    try:
        fnt_limpiarpantalla()
        msg = '\nNo se guardó el nuevo estudiante'
        with open(nomArchivo,'a') as f:
            codigo = input('Código del estudiante: ')
            nombre = input('Nombre: ')
            n1 = input('Nota 1: ')
            n2 = input('Nota 2: ')
            n3 = input('Nota 3: ')
            print(f'{codigo},{nombre},{n1},{n2},{n3}',file=f)
            msg = 'Datos guardados exitosamente'
            f.close()
    except Exception:
        pass
    return msg

def promedio():
    prom = 0
    with open(nomArchivo,'r') as f:
        codigo = input('Código del estudiante: ')
        for i in f:
            valores = i.strip().split(',')
            datosInt = list(map(float,valores[3:]))
            sumaNotas = sum(datosInt)
            prom = sumaNotas / len(datosInt)
        if(prom >= 3.5):
            aprobado = "Aprobado"
        else:
            aprobado = "Reprobado"
        print("Codigo: {} - Promedio: {}-{}".format(valores[0],prom,aprobado))

def menu():
    print('******* GESTIÓN DE NOTAS      *******')
    print('*** 1- Agregar estudiante         ***')
    print('*** 2- Actualizar estudiante      ***')
    print('*** 3- Borrar estudiante          ***')
    print('*** 4- Listar estudiantes         ***')
    print('*** 5- Promedio de un estudiante  ***')
    print('*** 6- Promedio del curso         ***')
    print('*** 7- Salir                      ***')
    print('*************************************')

while True:
    fnt_limpiarpantalla()
    menu()
    opc = int(input('Escoja la opción: '))
    if(opc == 1):
        esperar(msg=add_registro())
        input('Presione <ENTER> para continuar')
    elif(opc == 5):
        esperar(msg=promedio())
        input('Presione <ENTER> para continuar')
    elif(opc == 7):
        print('FIN')
        break
    else:
        print('Error, intente de nuevo')