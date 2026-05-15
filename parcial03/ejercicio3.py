lecturas = []
for i in range(5):
    valor = int(input(f"Ingrese la lectura {i+1}: "))
    lecturas.append(valor)
for temp in lecturas:
    match temp:
        case 0:
            print("❄️ Alerta: Punto de Congelación")
        case 100:
            print("🔥 Alerta: Punto de Ebullición")
        case _:
            estado = "Estado: Estable" if 10 <= temp <= 30 else "Estado: Crítico"
            print(f"🌡️ {estado}")
