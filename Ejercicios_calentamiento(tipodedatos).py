# Ejercicios de tipo de datos

# Ejercicio 1: Calcular el cociente y el resto de una división

""" 
divisor = int(input("Enter a divisor: "))
dividendor = int(input("Enter a dividend: "))
c = dividendor // divisor
r = dividendor % divisor
print("El cociente es:" + str(c))
print("El resto es:"+ str(r))
"""

# Ejercicio 2: Calcular el capital obtenido en una inversión
""" 
input_inicial = float(input("Ingrese el capital inicial: "))
input_tasa = float(input("Ingrese la tasa de interés anual (en %): "))  
input_tiempo = int(input("Ingrese el tiempo de la inversión (en años): "))
capital_final = input_inicial * (1 + input_tasa / 100) ** input_tiempo  
print("El capital final después de " + str(input_tiempo) + " años es: " + str(capital_final))   
"""

# Ejercicio 3: Juguetería vende Payasos 112g y muñecas 75g. ¿Cuánto pesa el paquete?
""" 
payasos = int(input("Ingrese el número de payasos vendidos: "))
muñecas = int(input("Ingrese el número de muñecas vendidas: "))
peso_payasos = payasos * 112  # Peso total de los payasos
peso_muñecas = muñecas * 75  # Peso total de las muñecas
peso_total = peso_payasos + peso_muñecas  # Peso total del paquete
print("El peso total del paquete es: " + str((peso_total)) + " gramos")  # Mostrar el peso total del paquete
""" 

#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
# Ejercicio 4: Barras de pan 3.49 cada una. El pan que no es del día tiene un descuento del 60%.
input_barras_no_frescas = int(input("Ingrese el número de barras de pan vendidas que no son del día: "))
precio_barras = 3.49  # Precio habitual de una barra de pan
descuento = 0.60  # Descuento del 60%
precio_descuento = precio_barras * descuento  # Calcular el descuento
precio_final = precio_barras - precio_descuento  # Calcular el precio final después del descuento
costo_total = input_barras_no_frescas * precio_final  # Calcular el costo total
print("Precio habitual de una barra de pan: " + str(precio_barras) + "€")  # Mostrar el precio habitual
print("Descuento por no ser fresca: " + str(precio_descuento) + "€")  # Mostrar el descuento   
print("Precio final de una barra de pan después del descuento: " + str(precio_final) + "€")  # Mostrar el precio final
print("Costo total por las barras de pan vendidas que no son del día: " + str(costo_total) + "€")  # Mostrar el costo total 
 