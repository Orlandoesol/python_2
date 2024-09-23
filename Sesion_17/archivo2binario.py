import pickle

archivo = open("MiArchivo.dat", "rb")
datos = pickle.load(archivo)
archivo.close()

for i in datos:
    print(i)