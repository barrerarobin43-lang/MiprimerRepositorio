"""Cree un programa que solicite un correo electrónico y verifique si contiene el símbolo @.
Si lo contiene, muestre el mensaje: "El correo parece válido".
Si no lo contiene, muestre el mensaje: (El correo no es válido)"""

correo = input("Ingrese su correo Electronico: ")
if "@" in correo :
    print("Parece un correo válido")
else:
    print("El correo no es válido")