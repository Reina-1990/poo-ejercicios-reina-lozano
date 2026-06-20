class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def estudiar(self):
        print(f"{self.nombre} está estudiando {self.carrera}")


# objeto 
est = Estudiante("Reina Maria Lozano Cardenas", 36, "Desarrollo de Software")

# Llamar método
est.estudiar()