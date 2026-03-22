"""Solicite al usuario una frase y muestre cuántas letras tiene la frase sin contar los espacios. 
Puede utilizar el método replace() para eliminar los espacios."""

frase = input("Ingrese una frase cuan grande quiera")
espacios0 = frase.replace(" ", "")
letras = len(espacios0)
print(letras)