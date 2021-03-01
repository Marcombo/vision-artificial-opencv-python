def datos(nombre, direccion, telefono):
    if nombre == "" : print("No tengo tu nombre")
    else : print("Hola " + nombre)
    if direccion != "" : print("Vives en  "+direccion)
    else : print("No tengo tu dirección")
    if telefono != "" : print("Tu teléfono es "+telefono)
    else : print("No tengo tu teléfono")

nombre = input("¿Cómo te llamas? ")
direccion = input("¿Cuál es tu dirección? ")
telefono = input("¿Cuál es tu número de teléfono? ")

datos(telefono=telefono, nombre=nombre, direccion=direccion)


