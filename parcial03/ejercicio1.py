codigo = input("Ingrese el código de rastreo (AÑO-CATEGORÍA-PAÍS): ")

if not codigo:
    print("Error: El código no puede estar vacío.")
else:
    inicio = codigo.find("-") + 1
    fin = codigo.rfind("-")
    categoria = codigo[inicio:fin]

    print(" Categoría:", categoria)

    print("🚚", "Ruta Local" if codigo.endswith("SV") else "Ruta Internacional")
