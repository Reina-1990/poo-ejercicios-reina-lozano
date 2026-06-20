class Juego:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero

    def jugar(self):
        print("Iniciando", self.titulo)

j = Juego("Minecraft", "Sandbox")
j.jugar()
