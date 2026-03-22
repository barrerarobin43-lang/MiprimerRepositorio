"""Cree un programa que solicite una frase al usuario. Luego muestre:
 La frase original.
 La frase en mayúsculas.
 La frase en minúsculas."""
 
frase = input("ingrese una frase que quiera: ")
mayus = frase.upper()
minus = frase.lower()
print ("frase original:",frase),print("En mayusculas:",mayus),print("En minusculas:",minus)