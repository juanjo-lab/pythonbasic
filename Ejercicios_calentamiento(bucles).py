# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""
input_usuario = input("Introduce una palabra: ")
for i in range(10):
    print(input_usuario)    
"""
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
"""
input_usuario = int(input("Introduce un número entero: "))
for i in range(1, input_usuario + 1):
    for j in range(i):
        print("*", end="")
    print()  # Salto de línea después de cada fila del triángulo    
"""
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""
print("Tabla de multiplicar del 1 al 10:")
for i in range(1, 11):
    for j in range(1,11):
        multiplicacion = i * j
        print( str(int(i)) + " x " + str(int(j)) + " = " + str(int(multiplicacion)))
"""

# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1
"""
input_usuario = int(input("Introduce un número entero: "))
for i in range(1, input_usuario + 1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print()  # Salto de línea después de cada fila del triángulo
"""
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""
input_contraseña = "contraseña"
while True:
    input_usuario = input("Introduce la contraseña: ")
    if input_usuario == input_contraseña:
        print("Contraseña correcta.")
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
"""
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""
input_usuario = int(input("Introduce un número entero: "))
if input_usuario < 2:
    print(f"{input_usuario} no es un número primo.")
else:
    es_primo = True
    for i in range(2, int(input_usuario ** 0.5) + 1):
        if input_usuario % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{input_usuario} es un número primo.")
    else:
        print(f"{input_usuario} no es un número primo.")
"""
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""
input_usuario = input("Introduce una palabra: ")
for letra in reversed(input_usuario):
    print(letra)  # Muestra cada letra de la palabra introducida empezando por la última
"""
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
"""
input_frase = input("Introduce una frase: ")
input_letra = input("Introduce una letra: ")
contador = 0
for letra in input_frase:
    if letra == input_letra:
        contador += 1   
print("La letra " + input_letra + " aparece " + str(int(contador)) + " veces en la frase.")  # Muestra el número de veces que aparece la letra en la frase
"""
#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""
input_usuario = ""
while input_usuario.lower() != "salir": 
    input_usuario = input("Introduce algo (escribe 'salir' para terminar): ")
    if input_usuario.lower() != "salir":
        print(input_usuario)  # Muestra el eco de lo que el usuario introduzca  
"""
