"""Solicite al usuario una frase y reemplace todas las apariciones de
   la palabra "Python" por "Programación" utilizando el método replace()"""
   
frase = input("Ingrese una frase: ")
remplazo = frase.replace("python", "Programacion")
print(remplazo)