import random

print("Hola cómo te llamas?: ")
nombre = input()
respuesta = 0
print("Hola " + nombre + " hoy voy a adivinar el número que pienses entre el 1 y el 20")
print("Iré adivinando y debes decir si mi estimación es muy alta o baja")

limInferior = 1
limSuperior = 20

while respuesta != 3:
    resAlto = random.randint(limInferior, limSuperior)
    print("El numero que pensaste es el " + str(resAlto) + "? Selecciona una opción:")
    print("1: Mi numero es mayor que " + str(resAlto))
    print("2: Mi numero es menor que " + str(resAlto))
    print("3: Adivinaste")
    respuesta = int(input())
    if respuesta == 1:
        limInferior = resAlto + 1
    elif respuesta == 2:
        limSuperior = resAlto - 1
    if limInferior == limSuperior:
        print("Gracias por jugar tu numero era el: " + str(resAlto))
        print("Nos vemos pronto " + nombre + "!")      
        break
    if limInferior > limSuperior:
        print("Me estas mintiendo")
        print("Ya no quiero jugar")
        break


if respuesta == 3:
    print("Gracias por jugar tu numero era el: " + str(resAlto))
    print("Nos vemos pronto " + nombre + "!")