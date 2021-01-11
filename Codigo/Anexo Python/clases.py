class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def ladrar(self):
        print("¡Guau!")

class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def mostrarAtributos(self):
        print("Nombre de la persona: " + self.nombre)
        print("DNI: " + str(self.dni))

class Cliente(Persona):
    def __init__(self, nombre, dni, perro):
        Persona.__init__(self, nombre, dni)
        self.perro = perro
    def mostrarAtributos(self):
        super().mostrarAtributos()
        print("Nombre del perro: " + self.perro.nombre)
        print("Raza: " + self.perro.raza)

mi_perro = Perro("Rufo", "pastor alemán")
yo = Cliente("Tomás", 1234, mi_perro)
yo.mostrarAtributos()





