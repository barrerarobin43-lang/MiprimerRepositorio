# Ejercicio 7
# 1. Toma el texto numérico "42".
# 2. Rellenalo con ceros a la izquierda hasta que alcance una longitud total de 5 caracteres.
# 3. Verifica mediante un método booleano si esa nueva cadena generada termina con el número "2".

texto = "42"

relleno = texto.zfill(5)

compro = relleno.endswith("2")

print("Texto rellenado ", relleno)

print("termina con un 2? ", compro)
