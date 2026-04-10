# Ejercicio 3
# 1. Crea una variable con el texto "ING. Su nombre".
# 2. Remueve el prefijo "ING. " de la cadena.
# 3. Convierte el texto restante completamente a letras mayusculas.
# 1. Crear la variable con el texto
texto = "ING. Robin"

# 2. Remover el prefijo "ING. "
texto_sin_prefijo = texto.removeprefix("ING.")

# 3. Convertir el texto restante a mayúsculas
resultado = texto_sin_prefijo.upper()

print("resultado es ", texto_sin_prefijo)
