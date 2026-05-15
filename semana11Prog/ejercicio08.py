# Ejercicio 8
# 1. Define un bloque de texto de 3 lineas usando comillas triples (puedes usar un fragmento del poema de la guia).
# 2. Cuenta cuantas veces aparece la letra "a" en todo el bloque de texto.
# 3. Divide el bloque de texto por sus saltos de linea (splitlines) para convertirlo en una lista de oraciones independientes.

bloque = """La vida es sueño
y los sueños, sueños son
la esperanza nunca muere"""

conteo = bloque.count("a")

linea = bloque.splitlines()

print("bloque de texto? ", bloque)

print("cuantas veces sale la palabra a en el texto ", conteo)

print("division de lineas y lista ", linea)
