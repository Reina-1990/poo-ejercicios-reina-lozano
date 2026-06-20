#clase Animal
class Animal:
    def sonido(self):
        print("Sonido")

class Perro(Animal):
    def sonido(self):
        print("Guau")

class Gato(Animal):
    def sonido(self):
        print("Miau")

Perro().sonido()
Gato().sonido()