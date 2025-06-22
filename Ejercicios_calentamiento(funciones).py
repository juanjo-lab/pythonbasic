# Ejercicios de Funciones

# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.
"""
def saludo():
    print("¡Hola amiga!")   
# Llamada a la función saludo
saludo()    
saludo()
"""
#Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.
"""
input_nombre = input("Introduce tu nombre: ")
def saludo_nombre(nombre):
    print(f"¡Hola {nombre}!")
# Llamada a la función saludo_nombre
saludo_nombre(input_nombre)
"""
# Escribir una función que reciba un número entero positivo y devuelva su factorial.
"""
def factorial(n):
    if n < 0:
        return "El número debe ser positivo."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
# Llamada a la función factorial
try:
    numero = int(input("Introduce un número entero positivo: "))
    print(f"El factorial de {numero} es {factorial(numero)}")   
except ValueError:
    print("Por favor, introduce un número entero válido.")  
"""
# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%
"""
def calcular_factura(cantidad_sin_iva, porcentaje_iva=21):
    iva = cantidad_sin_iva * (porcentaje_iva / 100)
    total_factura = cantidad_sin_iva + iva
    return total_factura
# Llamada a la función calcular_factura
try:
    cantidad = float(input("Introduce la cantidad sin IVA: "))
    porcentaje = input("Introduce el porcentaje de IVA (deja en blanco para 21%): ")
    if porcentaje == "":
        print(f"El total de la factura es: {calcular_factura(cantidad)}")
    else:
        porcentaje = float(porcentaje)
        print(f"El total de la factura es: {calcular_factura(cantidad, porcentaje)}")
except ValueError:
    print("Por favor, introduce una cantidad válida.")
    """
# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
"""
import math
def area_circulo(radio):
    return math.pi * (radio ** 2)       
# Llamada a la función area_circulo
try:
    radio = float(input("Introduce el radio del círculo: "))
    area = area_circulo(radio)
    print(f"El área del círculo es: {area}")    
except ValueError:
    print("Por favor, introduce un número válido para el radio.")
def volumen_cilindro(radio, altura):
    area_base = area_circulo(radio)
    return area_base * altura
# Llamada a la función volumen_cilindro
try:
    altura = float(input("Introduce la altura del cilindro: "))
    volumen = volumen_cilindro(radio, altura)
    print(f"El volumen del cilindro es: {volumen}")
except ValueError:
    print("Por favor, introduce un número válido para la altura.")  
"""

# Escribir una función que reciba una muestra de números en una lista y devuelva su media.
"""
def calcular_media(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)
# Llamada a la función calcular_media
try:
    numeros = input("Introduce una lista de números separados por comas: ")
    lista_numeros = [float(num) for num in numeros.split(",")]
    media = calcular_media(lista_numeros)
    print(f"La media de los números es: {media}")
except ValueError:
    print("Por favor, introduce una lista de números válidos separados por comas.")
"""
#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
"""
def calcular_cuadrados(numeros):
    return [num ** 2 for num in numeros]
# Llamada a la función calcular_cuadrados
try:
    numeros = input("Introduce una lista de números separados por comas: ")
    lista_numeros = [float(num) for num in numeros.split(",")]
    cuadrados = calcular_cuadrados(lista_numeros)
    print(f"Los cuadrados de los números son: {cuadrados}")
except ValueError:
    print("Por favor, introduce una lista de números válidos separados por comas.")
"""
# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
"""
def calcular_estadisticas(numeros): 
    if not numeros:
        return {"media": 0, "varianza": 0, "desviacion_tipica": 0}
    
    media = sum(numeros) / len(numeros)
    varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
    desviacion_tipica = varianza ** 0.5
    
    return {
        "media": media,
        "varianza": varianza,
        "desviacion_tipica": desviacion_tipica
    }
# Llamada a la función calcular_estadisticas
try:    
    numeros = input("Introduce una lista de números separados por comas: ")
    lista_numeros = [float(num) for num in numeros.split(",")]
    estadisticas = calcular_estadisticas(lista_numeros)
    print(f"Media: {estadisticas['media']}, Varianza: {estadisticas['varianza']}, Desviación Típica: {estadisticas['desviacion_tipica']}")
except ValueError:
    print("Por favor, introduce una lista de números válidos separados por comas.")

"""
#Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
"""
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a
def mcm(a, b):
    return abs(a * b) // mcd(a, b)  
# Llamada a las funciones mcd y mcm
try:    
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    print(f"El máximo común divisor de {num1} y {num2} es: {mcd(num1, num2)}")
    print(f"El mínimo común múltiplo de {num1} y {num2} es: {mcm(num1, num2)}")
except ValueError:
    print("Por favor, introduce números enteros válidos.")
"""
#Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.
"""
def decimal_a_binario(n):       
    if n == 0:
        return "0"
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n //= 2
    return binario
def binario_a_decimal(b):
    decimal = 0
    for i, bit in enumerate(reversed(b)):
        decimal += int(bit) * (2 ** i)
    return decimal  
# Llamada a las funciones decimal_a_binario y binario_a_decimal
try:
    numero_decimal = int(input("Introduce un número decimal: "))
    print(f"El número {numero_decimal} en binario es: {decimal_a_binario(numero_decimal)}")
    
    numero_binario = input("Introduce un número binario: ")
    print(f"El número {numero_binario} en decimal es: {binario_a_decimal(numero_binario)}")
except ValueError:
    print("Por favor, introduce un número válido.")
"""
#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
def contar_palabras(cadena):
    palabras = cadena.split()
            
