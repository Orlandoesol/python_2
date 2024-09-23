def archivo():
    archivo = open('C:/ficheros/miarchivo.txt','r')
    texto = archivo.read()
    print(texto)
    
archivo()