import random

print("Hola cómo te llamas?: ")
nombre = input()
respuesta = 0
print("Hola " + nombre + " hoy voy a adivinar el número que pienses entre el 1 y el 20")
print("Iré adivinando y debes decir si mi estimación es muy alta o baja")


print("El numero que pensaste es el 10? Selecciona en introduce una opción: ALTO:1 BAJO:2 ADIVINASTE:3")
respuesta = input()
respuesta = int(respuesta)
resAlto = 10

if respuesta == 1:
    print("El numero que pensaste es el 5? Selecciona en introduce una opción: ALTO:1 BAJO:2 ADIVINASTE:3")
    respuesta = input()
    respuesta = int(respuesta)
    resAlto = 15
    if respuesta == 1:
        while respuesta != 3:
            resAlto = random.randint(1, 4)
            resAlto = str(resAlto)
            print("El numero que pensaste es el " + resAlto + "? Selecciona en introduce una opción: NO:2 ADIVINASTE:3")
            respuesta = input()
            respuesta = int(respuesta)

    if respuesta == 2:
        while respuesta != 3:
            resAlto = random.randint(6, 9)
            resAlto = str(resAlto)
            print("El numero que pensaste es el " + resAlto + "? Selecciona en introduce una opción: NO:2 ADIVINASTE:3")
            respuesta = input()
            respuesta = int(respuesta)



if respuesta == 2:
    print("El numero que pensaste es el 15? Selecciona en introduce una opción: ALTO:1 BAJO:2 ADIVINASTE:3")
    respuesta = input()
    respuesta = int(respuesta)
    resAlto = 15
    if respuesta == 1:
        while respuesta != 3:
            resAlto = random.randint(11, 14)
            resAlto = str(resAlto)
            print("El numero que pensaste es el " + resAlto + "? Selecciona en introduce una opción: NO:2 ADIVINASTE:3")
            respuesta = input()
            respuesta = int(respuesta)

    if respuesta == 2:
        while respuesta != 3:
            resAlto = random.randint(16, 20)
            resAlto = str(resAlto)
            print("El numero que pensaste es el " + resAlto + "? Selecciona en introduce una opción: NO:2 ADIVINASTE:3")
            respuesta = input()
            respuesta = int(respuesta)



if respuesta == 3:
    resAlto = str(resAlto)
    print("Gracias por jugar tu numero era el: " + resAlto + " nos vemos pronto " + nombre)

