#Clase Circulo
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)


# Crear objeto
c = Circulo(5)

# Mostrar resultado
print("Área del círculo:", c.area())