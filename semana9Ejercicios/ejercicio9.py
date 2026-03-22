"""Solicite al usuario una frase y muestre si la frase empieza con la palabra "Hola".
Puede utilizar el método startswith()."""

frase = input("Ingrese una frase: ")
saberInicio = frase.startswith("Hola")
print(saberInicio)