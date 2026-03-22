"""Solicite al usuario una frase y verifique si la frase termina con un punto ".".
Puede utilizar el método endswith()."""

frase = input("Ingrese una frase: ")
puntoFinal = frase.endswith(".")
print(puntoFinal)
