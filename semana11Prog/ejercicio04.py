# Ejercicio 4
# 1. Toma la palabra "CANTANDO".
# 2. Convierte toda la cadena a letras minusculas.
# 3. Elimina el sufijo "ando" de la palabra resultante y encuentra en que indice (posicion) quedo la letra "t".

palabra = "CANTANDO"

minus = palabra.lower()

sinSufijo = minus.removesuffix("ando")

indice_t = sinSufijo.find("t")

print("la palabra final es ", sinSufijo)
print("el lugar de la letra es ", indice_t)
