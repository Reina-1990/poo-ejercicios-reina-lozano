#Clase Coche
class Coche:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def mostrar_detalles(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")


#  objeto (ejemplo)
mi_coche = Coche("Toyota", "Corolla", 2020)





mi_coche.mostrar_detalles()