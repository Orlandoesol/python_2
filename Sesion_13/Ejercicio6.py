# Ejercicio 1.
# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono, y lo guarde
# en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive 
# en #<direccion> y su número de teléfono es <teléfono>.

nombre = input('Nombre: ')
edad = input('Edad: ')
direccion = input('Dirección: ')
telefono = input('Telefono: ')

persona = {'nombre': nombre,'edad':edad,'direccion':direccion,'telefono':telefono}
print(persona['nombre'],'tiene',persona['edad'],'años, vive en', persona['direccion'], 'y su teléfono es: ',persona['telefono'])