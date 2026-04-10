# Ejercicio 12
# 1. Toma el nombre de archivo "Sunombre.txt".
# 2. Remueve el sufijo ".txt" y posteriormente remueve el prefijo "ING. ".
# 3. Toma el texto que quede limpio, convertido a minúsculas.

nombre = "ING.Robin.txt"
print("asi normal: ", nombre)

remover = nombre.removesuffix(".txt").removeprefix("ING.")

minusculas = remover.lower()

print("ya limpio es: ", minusculas)
