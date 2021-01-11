def hola(nombre = "ninguno"):
    if nombre == "ninguno" : print("Hola")
    else : print("Hola " + nombre)

hola()
nombre = input("¿Cómo te llamas? ")
hola(nombre)


