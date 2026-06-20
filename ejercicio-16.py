class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)


# Crear objeto
rect = Rectangulo(4, 5)

# Mostrar resultados
print("Área:", rect.area())
print("Perímetro:", rect.perimetro())