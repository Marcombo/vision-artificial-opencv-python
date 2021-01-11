yo = {
    "nombre" : "Tomás",
    "NIF" :  1234567,
    "dirección" : "Madrid"
}

mi_perro = {
    "nombre": "Snoppy",
    "raza": "Beagle",
    "sexo": "macho",
    "edad": 10,
    "dueño": yo
}

print("---DATOS DEL PERRO---")
for clave_perro, valor_perro in mi_perro.items():
    if clave_perro == "dueño" :
        print("---DATOS DEL DUEÑO---")
        for clave_dueño, valor_dueño in valor_perro.items():
            print(clave_dueño + ":" + str(valor_dueño))
    else : print(clave_perro + ":" + str(valor_perro))
