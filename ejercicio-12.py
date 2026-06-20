#Libro
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def es_largo(self):
        return self.paginas > 500


# Pedir datos al usuario
titulo = input("Ingresa el título: ")
autor = input("Ingresa el autor: ")
paginas = int(input("Número de páginas: "))

#  objeto
libro = Libro(titulo, autor, paginas)






print("¿Es un libro largo?", libro.es_largo())