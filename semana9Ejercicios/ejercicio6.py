"""Cree un programa que solicite un nombre completo y lo separe en palabras utilizando el método split().
Luego muestre cada palabra en una línea diferente."""

nombre = input("Ingrese su nombre completo: ")
palabras = nombre.split()
print(palabras)
for palabras in palabras:
    print(palabras)