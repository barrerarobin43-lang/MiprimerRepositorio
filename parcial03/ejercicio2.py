from decimal import Decimal

total = Decimal("0")

while True:
    try:
        entrada = input("Ingrese el precio del producto (0 para salir): ")

        if not entrada:
            print(" Error: El valor no puede estar vacío.")
            continue

        precio = Decimal(entrada)

        if precio == 0:
            break
        total += precio

    except ValueError:
        print(" Advertencia: Ingrese solo números válidos.")
        continue

print(f" Total a cobrar: {total}")
