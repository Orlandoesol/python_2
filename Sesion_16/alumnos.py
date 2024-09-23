#Operaciones CRUD(Create, Read, Update, Delete)
import os

def fnt_limpiarCLS():
    os.system('cls')

#Base de datos: Alumno
def bd_alumnos():
    alumno = {
        'Alu01': ['María','Alvarez',3.1,4.8,5.0],
        'Alu02': ['Antonio','Berrio',2.1,3.8,4,1],
        'Alu03': ['Margarita','Cespedes',1.6,4.8,4.9],
        'Alu04': ['Jesus','Davidson',3.1,2.8,5.0],
        'Alu05': ['Adriana','Hernandez',3.8,4.3,3.9]
    }
    
    return alumno

#Agregar
def agregar_alumno(alumno):
    cod_alu = input('Código del estudiante: ')
    if cod_alu in alumno:
        print('El alumno ya se encuentra ingresado en la base de datos')
    else:
        alu = input('Ingrese los datos del alumno: \n').split(',')
        alu[2] = float(alu[2])
        alu[3] = float(alu[3])
        alu[4] = float(alu[4])
        alumno[cod_alu] = alu
        print('El alumno ha sido registrado')
        print()
        listar_alumno(alumno)
    return alumno

#Listar
def listar_alumno(bd_alumnos):
    print('***************************************')
    for key in bd_alumnos:
        print(key,':',bd_alumnos[key])
    print('***************************************')
    
#Promedio de un estudiante
def Promedio(bd_alumnos):
    prom = 0
    for i in bd_alumnos:
        prom = (bd_alumnos[i][2] + bd_alumnos[i][3] + bd_alumnos[i][4]) / 3
        bd_alumnos[i].append(round(prom,2))
    listar_alumno(bd_alumnos)
    return bd_alumnos

def menu():
    print('GESTION DE NOTAS')
    print('1- Agregar alumno')
    print('2- Actualizar alumno')
    print('3- Borrar alumno')
    print('4- Mostrar alumnos')
    print('5- Promedio por cada estudiante')
    print('6- Estudiante con mayor promedio')
    print('7- Estudiante con menor promedio')
    print('8- Promedio general del curso')
    print('9- Salir')
    
#Programa principal
control = True
while control:
    fnt_limpiarCLS()
    menu()
    opc = int(input('Elija su opción: '))
    if(opc == 1):
        estudiante = bd_alumnos()
        agregar_alumno(estudiante)
        input('Presione <ENTER> para continuar')
    elif(opc == 5):
        estudiante = bd_alumnos()
        Promedio(estudiante)
        input('Presione <ENTER> para continuar')
    elif(opc == 9):
        print('FIN')
        control = False
    else:
        print('Error intente de nuevo')
        input('Presione <ENTER> para continuar')
