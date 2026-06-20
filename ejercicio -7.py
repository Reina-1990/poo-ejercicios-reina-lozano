#Número mayor
lista = [3, 7, 2, 9, 5]

mayor = lista[0]
for num in lista:
    if num > mayor:
        mayor = num

print("Mayor:", mayor)
