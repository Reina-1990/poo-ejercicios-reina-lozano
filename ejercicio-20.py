class Smartphone:
    def __init__(self, marca, modelo, ram):
        self.marca = marca
        self.modelo = modelo
        self.ram = ram

    def encender(self):
        print(f"El {self.marca} {self.modelo} se ha encendido")


# Crear objeto
celular = Smartphone("Samsung", "Galaxy S21", "8GB")

# Llamar método
celular.encender()