def hola(nombre = "anónimo"):
    if nombre == "anónimo" : print("Hola")
    else : print("Hola " + nombre)

hola()
nombre = input("¿Cómo te llamas? ")
hola(nombre)
