#Ejercicio 3.
#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al 
#usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
#Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
#Fruta    Precio
#------   -------- 
#Platano  1.35
#Manzana  0.80
#Pera     0.85
#Naranja  0.70

frutas={'Platano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}
fruta = input('¿Qué fruta desea usted?: ').title()
kg = float(input('¿Cuántos kilos?: '))
if fruta in frutas:
    print(kg,'kilos de',fruta,'tiene un costo de $',frutas[fruta]*kg)
else:
    print('En este momento la fruta',fruta,'no se encuentra disponible')
