##Ejercicio 1
1.0  ## Declara una variable con la cadena "  elefante  ".
2.0  ##tiliza el método correspondiente para eliminar los espacios en blanco a ambos extremos de la palabra.
3.0  ##Cuenta y muestra cuántas veces se repite la letra "e" en el texto ya limpio.

# 1. Declarar la variable
texto = "  elefante  "

# 2. Eliminar espacios al inicio y al final
texto_limpio = texto.strip()

# 3. Contar cuántas veces aparece la letra "e"
cantidad_e = texto_limpio.count("e")

# Mostrar resultados
print("Texto limpio:", texto_limpio)
print("Cantidad de 'e':", cantidad_e)
