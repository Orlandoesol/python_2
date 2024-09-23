def archivos():
    archivo = open('C:/ficheros/miarchivo.txt','r')
    linea = archivo.readline()
    print(linea)
    print('Leí la primera línea. Vamos por la segunda!!')
    linea = archivo.readline()
    print(linea)
    
archivos()
    