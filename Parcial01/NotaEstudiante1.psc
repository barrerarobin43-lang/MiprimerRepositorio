Algoritmo NotaEstudiante
		Definir nota Como Entero
		
		Escribir "¿Cual ha sido su nota?"
		Leer nota
		
		Si nota < 0 Entonces
			Escribir "Solo números positivos"
		Sino Si nota > 10 Entonces
				Escribir "Solo de 0 a 10"
			Sino Si nota >= 6 Entonces
					Escribir "tu nota es " nota ", aprobado"
				Sino Si nota = 5 Entonces
						Escribir "Recuperación"
					Sino
						Escribir "Reprobado con " nota 
					FinSi
				FinSi
			FinSi
		FinSi
		
					
FinAlgoritmo

