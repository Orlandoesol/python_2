def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    return a / b

def menu():
    print('1- SUMA')
    print('2- RESTA')
    print('3- MULTIPLICACION')
    print('4- DIVISION')

control = True
while control:
    try:
        x = int(input('Número 1: '))
        y = int(input('Número 2: '))
        menu()
        opc = int(input('Elija la operación matemática a realizar: '))
        if(opc == 1):
            print('La suma es: ',suma(x,y))
            break
        elif(opc == 2):
            print('La resta es: ',resta(x,y))
            break
        elif(opc == 3):
            print('La multiplicación es: ',multiplicacion(x,y))
            break
        elif(opc == 4):
            print('La división es: ',division(x,y))
            break
        else:
            print('Opción inválida, intente de nuevo!')
    except ZeroDivisionError:
        print('Es indeterminado, no se puede hacer')
    except:
        print('Error')