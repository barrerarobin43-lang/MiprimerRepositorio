preguntas = ["¿Cuál es tu edad?", "¿Cuál es tu género?", "¿Cuál es tu nivel educativo?"]

respuestas = {}

for i, pregunta in enumerate(preguntas, start=1):
    respuesta = input(f"{pregunta}: ")

    # Validar respuesta (ejemplo simple: no vacía)
    if respuesta.strip() == "":
        while respuesta.strip() == "":
            print("Respuesta inválida, intenta de nuevo.")
            respuesta = input(f"{pregunta}: ")
    # Guardamos la respuesta
    respuestas[pregunta] = respuesta

edad = int(respuestas["¿Cuál es tu edad?"])

match edad:
    case edad if edad < 18:
        print("Encuestado menor de edad")
    case edad if 18 <= edad < 30:
        print("Encuestado joven adulto")
    case edad if edad >= 30:
        print("Encuestado adulto")
    case _:
        print("Categoría no definida")
