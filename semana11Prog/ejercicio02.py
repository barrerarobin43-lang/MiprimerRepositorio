# Ejercicio 2
# 1. Toma la cadena de texto "Su nombre"".
# 2. Convierte el texto para que la primera letra de cada una de las palabras este en mayúscula.
# 3. Reemplaza la palabra "Su nombre" por "Su apellido" en el nuevo texto generado.
nombre = "robin christopher"
print("nombre normal:", nombre)

nombre_mayus = nombre.title()
print("nombre con la primera letra en masyucula:", nombre_mayus)

nombre_nuevo = nombre_mayus.replace("Robin Christopher", "Barrera Vasquez")
print("Nombre reemplazado:", nombre_nuevo)
