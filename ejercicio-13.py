#Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")


# Crear objeto
persona1 = Persona("Maria", 36)

# Llamar al método
persona1.saludar()