#Palíndromo
texto = input("Texto: ").lower().replace(" ", "")

if texto == texto[::-1]:
    print("Es palíndromo")
else:
    print("No es palíndromo")
    