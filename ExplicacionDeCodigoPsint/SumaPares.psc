Algoritmo SumarPares
	//Sumar solo números pares usando condición lógica en Hacer-Mientras. Documentar y subir a Git.
    Definir numero, suma Como Entero
    suma <- 0  // Inicializamos la suma en cero
    
    Repetir
        Escribir "Ingresa un número (Ingresa 0 para terminar): "
        Leer numero
        
        // Condición lógica para verificar si es par y evitar sumar el 0 final
        Si numero MOD 2 = 0 Y numero <> 0 Entonces
            suma <- suma + numero
        Fin Si
        
     Hasta Que numero = 0  
    
    Escribir "La suma total de los números pares es: ", suma
FinAlgoritmo
