# EJERCICIOS DE CALENTAMIENTO (CADENAS)
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""
input_usuario = input("Introduce tu nombre: ")
numero_repeticiones = int(input("Introduce un número entero: "))
for i in range(numero_repeticiones):
    print(input_usuario)
"""
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
""""
input_usuario = input("Introduce tu nombre")
input_usuario = input("Introduce tu nombre completo: ")
print(input_usuario.lower())
print(input_usuario.upper())
print(input_usuario.title())
"""
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
""""
input_usuario = input("Introduce tu nombre en la consola: ")
numero_letras = len(input_usuario) 
print("El nombre " + input_usuario.upper() + " tiene " + str(numero_letras) + " letras.")
"""

# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
""""
input_telefono=input("Introduce tu numero de telefono con el formato prefijo-número-extensión: ")
if input_telefono.startswith("+34-") and "-" in input_telefono:
    numero = input_telefono.split("-")[1]
    print("El número de teléfono sin el prefijo y la extensión es: " + numero)
"""
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
"""
input_frase = input("Introduce una frase: ")
frase_invertida = input_frase[::-1] 
print("La frase invertida es: " + frase_invertida)
"""
#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""
input_frase = input("Introduce una frase: ")
input_vocal = input("Introduce una vocal: ")    
if input_vocal.lower() in "aeiou":
    frase_modificada = input_frase.replace(input_vocal, input_vocal.upper())
    print("La frase modificada es: " + frase_modificada)
"""
#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
"""
input_email = input("Introduce tu correo electrónico: ")
if "@" in input_email:
    nombre_usuario = input_email.split("@")[0]
    nuevo_email = nombre_usuario + "@ceu.es"
    print("Tu nuevo correo electrónico es: " + nuevo_email)
"""
#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

"""
input_fecha = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")
if "/" in input_fecha:
    partes_fecha = input_fecha.split("/")
    if len(partes_fecha) == 3:
        dia = partes_fecha[0].zfill(2)  # Asegura que el día tenga dos dígitos
        mes = partes_fecha[1].zfill(2)  # Asegura que el mes tenga dos dígitos
        anio = partes_fecha[2]
        print(f"Día: {dia}, Mes: {mes}, Año: {anio}")
    else:
        print("Formato de fecha incorrecto. Asegúrate de usar dd/mm/aaaa.")
"""

#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
"""
input_cesta = input("Introduce los productos de la cesta de la compra, separados por coma: ")
productos = input_cesta.split(",")
for producto in productos:
    print(producto.strip())  # Utiliza strip() para eliminar espacios en blanco al inicio y al final de cada producto
"""
