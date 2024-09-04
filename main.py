import random

print("***Generador de contraseñas***")

contador = 0
digitos = 10

caracteres = "QWERTYUIOPÑLKJHGFDSAZXCVBNM1234567890qwertyuiopñlkjhgfdsazxcvbnm"
contraseña = ""
while contador < digitos:
    seleccion = random.randint(0,len(caracteres))
    contraseña = contraseña + caracteres[seleccion]

    contador = contador + 1

print(f"Esta es tu contraseña generada: {contraseña}")
