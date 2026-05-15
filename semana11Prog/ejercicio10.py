# Ejercicio 10
# 1. Toma la cadena "Python2026".
# 2. Verifica si el texto es estrictamente alfanumérico (solo letras y números, sin espacios ni símbolos).
# 3. Si lo es, convierte el texto a minúsculas y luego separa la palabra de los números reemplazando "2026" por una cadena vacia "".

cadena = "Python2026"

combrobante = cadena.isalnum()

print("Es alfanumerico? ", combrobante)

if combrobante == True:
    cadenaminus = cadena.lower()
    print("cadena en minuscula ", cadenaminus)

    cadena_remplazo = cadenaminus.replace("2026", "")
    print("cadena remplazo ", cadena_remplazo)
else:
    print("no es alfanumerico")
