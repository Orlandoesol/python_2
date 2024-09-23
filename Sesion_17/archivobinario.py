import pickle

datos = ["Julio César", "Castaño Bustos", 41, 1.72]
archivo = open("MiArchivo.dat", "wb")
pickle.dump(datos, archivo)
archivo.close()