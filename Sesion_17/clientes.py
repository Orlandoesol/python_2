import os 
import time 
#
# Gestión de clientes mediante archivos, permite Adicion, actualización, búsqueda, eliminación y listado de clientes
# 
nombreArchivo = 'E:/PIO-Programacion de Software/Logica de programacion/Sesion_17/clientes.dat' 
nombreEmpresa = 'Politecnico PIO'

def fnt_limpiarpantalla():
    try: 
        if os.name.upper()=='NT':
            os.system('cls') 
        else: 
            os.system('clear') 
    except Exception: 
        pass 
    
def esperar(tiempo=3,msg=None):
    try: 
        if msg!=None: 
            msg = f'{msg}. Por favor espere {tiempo} segundos para continuar' 
            print(msg) 
            time.sleep(tiempo) 
    except Exception: 
        pass 

def shocli(): 
    try: 
        mensaje = '\nError al listar los datos' 
        fnt_limpiarpantalla() 
        with open(nombreArchivo,'r') as f: 
            print('{0:^123}\n'.format(nombreEmpresa)) 
            print('{0:^123}\n'.format('Reporte de clientes')) 
            print('{0:<10} {1:>11} {2:<50} {3:>12} {4:<40}'.format('Tip. Ide.','Num. Ide.','Apellidos y Nombres','Teléfono','Dirección')) 
            for linea in f: 
                datos = linea.replace('\n','').split(',')
                
                print(f'{datos[0]:^10} {datos[1]:>11} {datos[2]:<50} {datos[3]:>12} {datos[4]:<40}') 
            sal = '\nListado finalizado' 
    except Exception: 
        pass 
    return mensaje 

def addcli(): 
    try: 
        fnt_limpiarpantalla() 
        mensaje = '\nNo se pudieron guardar los datos' 
        with open(nombreArchivo,'a') as f: 
            tid=input("Tipo de Identificación : ") 
            nid=input("Número de Identificación : ") 
            nom=input("Apellidos y Nombres : ") 
            tel=input("Teléfono : ") 
            dir=input("Dirección : ") 
            print(f'{tid},{nid},{nom},{tel},{dir}',file=f) 
            mensaje = '\nDatos guardados exitosamente' 
    except Exception: 
        pass 
    return mensaje 

def seacli(): 
    try: 
        fnt_limpiarpantalla() 
        sw = False 
        mensaje = '\nNo se encontró un registro que coincida con la información buscada.' 
        with open(nombreArchivo,'r') as f: 
            busqueda = input("Digite el valor a buscar : ") 
            tip = input("Buscará por N)ombre, I)dentificación o T)eléfono : ").lower() 
            for pos,linea in enumerate(f): 
                datos = linea.replace('\n','').split(',') 
                if (tip=="n" and datos[2].upper()==busqueda.upper()) or (tip=="i" and datos[1]==busqueda) or (tip=="t" and datos[3]==busqueda): 
                    sw=True 
                    break 
        if sw: 
           mensaje = f'\nSe encontró el registro buscado en la línea {pos} del archivo.' 
    except Exception: 
        pass
    return mensaje 

def fincli(busqueda): 
    try: 
        sw = False 
        pos = -10 
        with open(nombreArchivo,'r') as f: 
            for pos,linea in enumerate(f): 
                datos = linea.replace('\n','').split(',') 
                if datos[1]==busqueda: 
                    sw=True 
                    break 
    except Exception: 
        pass 
    return (sw,pos) 

# 
 # Se implementa borrado físico. Esta operación merece discutirse 
 # 

def delcli(): 
    try: 
        mensaje = '\nError al eliminar los datos.' 
        busqueda = input("Digite el número de documento : ") 
        (sw,enc) = fincli(busqueda) 
        if not sw: 
            mensaje = "\nNo se encontró ningun registro que coincida con el criterio de búsqueda" 
        else: 
            with open(nombreArchivo,'r') as f: 
                datos = f.readlines() 
                linea = datos[enc].replace('\n','').split(',') 
                print('*** DATOS DEL CLIENTE ***') 
                print(f"\tTipo de Identificación : {linea[0]}") 
                print(f"\tNúmero de Identificación : {linea[1]}") 
                print(f"\tApellidos y Nombres : {linea[2]}") 
                print(f"\tTeléfono : {linea[3]}") 
                print(f"\tDirección : {linea[4]}") 
                op = input('Confirma la eliminación del cliente [S/N] (NOTA: Este proceso es irreversible) : ').lower() 
                if op=='s': 
                    datos.pop(enc) 
                    with open(nombreArchivo,'w') as f: 
                        f.writelines(datos) 
                        sal = '\nDatos eliminados exitosamente.' 
                else: 
                       sal = '\nOperación cancelada'

    except Exception: 
        pass 
        return mensaje 

def updcli(): 
    try: 
        mensaje = '\nError al actualizar los datos.' 
        busqueda = input("Digite el número de documento : ") 
        (sw,enc) = fincli(busqueda) 
        if not sw: 
            mensaje = "\nNo se encontró ningun registro que coincida con el criterio de búsqueda" 
        else: 
            tid=input("Tipo de Identificación : ") 
            nid=input("Número de Identificación : ") 
            nom=input("Apellidos y Nombres : ") 
            tel=input("Teléfono : ") 
            dir=input("Dirección : ") 
            with open(nombreArchivo,'r') as f: 
                datos = f.readlines() 
                datos[enc] = f'{tid},{nid},{nom},{tel},{dir}\n' 
                with open(nombreArchivo,'w') as f: 
                    f.writelines(datos) 
                    mensaje = '\nDatos guardados exitosamente.' 
    except Exception: 
        pass 
        return mensaje 

def main(): 
    op = "1" 
    while op!="S": 
        os.system("cls") 
        print("\tOPCIONES DISPONIBLES\n") 
        print("\t1. Adicionar Cliente") 
        print("\t2. Buscar Cliente") 
        print("\t3. Borrar Cliente") 
        print("\t4. Actualizar Cliente") 
        print("\t5. Listar Clientes") 
        print("\tS. Salir") 
        op = input("\n\tSeleccione su opción : ").upper() 
        if op=="1": 
            esperar(msg=addcli()) 
        elif op=="2": 
            esperar(msg=seacli()) 
        elif op=="3":
            esperar(msg=delcli()) 
        elif op=="4": 
            esperar(msg=updcli()) 
        elif op=="5": 
            esperar(6,shocli()) 
        elif op!="S": 
            esperar(2,"\n\tSeleccione una opción valida") 
        else: 
            print("\tHasta la vista ...") 
main()
