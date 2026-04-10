# Ejercicio 6
# 1. Toma el texto "Su nombre".
# 2. Aplica el método de normalización fuerte (casefold) para prepararlo para una comparación ignorando mayúsculas.
# 3. Verifica si el texto resultante está compuesto únicamente por caracteres alfabéticos (letras) devolviendo un valor booleano.

Texto = "RobinBarrera"

Ignor = Texto.casefold()

comprobacion = Ignor.isalpha()

print("texto ya normal ", Ignor)
print("solo letras? ", comprobacion)
