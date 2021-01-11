from random import randint

numero1 = randint(1, 10)
numero2 = randint(1, 10)
numero = numero1 + numero2

respuesta = int(input("Cuánto es " + str(numero1) + " + " + str(numero2) + "? "))

if respuesta == numero:
    print("¡Correcto!")
else:
    print("No es correcto, la respuesta es " + str(numero))
