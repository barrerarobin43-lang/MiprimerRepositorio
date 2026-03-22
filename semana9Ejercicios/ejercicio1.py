"""Cree un programa que solicite al usuario su nombre completo. Luego muestre:
 El nombre en mayúsculas.
 El nombre en minúsculas.
 La cantidad de caracteres que tiene el nombre."""

nombre=input("Ingrese su nombre completo: ")
mayus= nombre.upper()
minus= nombre.lower()
cantidad= len(nombre)
print (mayus),print (minus),print(cantidad) 