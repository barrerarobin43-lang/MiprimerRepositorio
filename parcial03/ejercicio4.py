for i in range(1, 50):

    # Detener proceso en 42
    if i == 42:
        break

    # Saltar múltiplos de 3
    if i % 3 == 0:
        continue

    # Procesar registros válidos
    print(f"Procesando registro ID: {i}")