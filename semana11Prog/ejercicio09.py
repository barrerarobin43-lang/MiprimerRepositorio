# Ejercicio 9
# 1. Toma la cadena "Any time y Anytime".
# 2. Reemplaza todas las apariciones de "Any time" (con espacio) por "Always".
# 3. Convierte todo el texto resultante a mayusculas.

cadena = "Any time y Anytime"

remplazo = cadena.replace("Any time", "Always")

print("Remplazada ", remplazo)

mayus = remplazo.upper()

print("En mayusculas ", mayus)
