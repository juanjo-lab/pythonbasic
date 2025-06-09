# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
""""
input_usuario = input("Introduce una divisa (Euro, Dollar, Yen): ")
divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
if input_usuario in divisas:
    print("El símbolo de " + input_usuario + " es " + divisas[input_usuario])
"""
# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""
input_nombre = str(input("Introduce tu nombre: "))
input_edad = str(input("Introduce tu edad: "))
input_direccion = str(input("Introduce tu dirección: "))
input_telefono = str(input("Introduce tu número de teléfono: "))
Datos = {'Nombre': input_nombre, 'Edad': input_edad, 'Direccion': input_direccion, 'Telefono': input_telefono}
print("{} tiene {} años, vive en {} y su número de teléfono es {}.".format(Datos['Nombre'], Datos['Edad'], Datos['Direccion'], Datos['Telefono']))
"""
# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
"""
Fruta = {'Plátano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}
input_fruta = str(input("Introduce una fruta (Plátano, Manzana, Pera, Naranja): "))
if input_fruta in Fruta:
    input_kilos = float(input("Introduce el número de kilos: "))
    precio = Fruta[input_fruta] * input_kilos
    print("El precio de {} kilos de {} es {:.2f}€.".format(input_kilos, input_fruta, precio))
"""
# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
"""
input_fecha = input("Introduce una fecha en formato dd/mm/aaaa: ")
fecha_partes = input_fecha.split('/')
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
print("La fecha es: {} de {} de {}".format(fecha_partes[0], meses[int(fecha_partes[1]) - 1], fecha_partes[2]))
"""
# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
"""
Asignaturas = {'Matematicas':6,'Fisica':4,'Quimica':5}
total_creditos = 0
for asignatura, creditos in Asignaturas.items():
    print("{} tiene {} créditos.".format(asignatura, creditos))
    total_creditos += creditos
print("El número total de créditos del curso es {}.".format(total_creditos))
"""
#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""
Datos = {}
while True:
    clave = input("Introduce el nombre del dato (o 'salir' para terminar): ")
    if clave.lower() == 'salir':
        break
    valor = input(f"Introduce el valor para {clave}: ")
    Datos[clave] = valor
    print("Contenido del diccionario:", Datos)
print("Diccionario final:", Datos)
"""
# Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
"""
print("Bienvenido a tu cesta de la compra")
print("Puedes introducir artículos y sus precios. Escribe 'salir' para terminar.")
Cesta = {}
while True:
    articulo = input("Introduce el artículo (o 'salir' para terminar): ")
    if articulo.lower() == 'salir':
        break
    precio = float(input(f"Introduce el precio de {articulo}: "))
    Cesta[articulo] = precio
total = sum(Cesta.values())
print("\nLista de la compra:")
for articulo, precio in Cesta.items():
    print(f"{articulo}: {precio:.2f}€") 
print(f"Coste total: {total:.2f}€")
"""
# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""
facturas = {}
while True:
    factura = input("¿Deseas añadir una nueva factura, pagar una existente o terminar? (añadir/pagar/terminar): ").lower()
    if factura == 'añadir':
        numero_factura = input("Introduce el número de factura: ")
        coste = float(input("Introduce el coste de la factura: "))
        facturas[numero_factura] = coste
        print(f"Factura {numero_factura} añadida con un coste de {coste:.2f}€.")
    elif factura == 'pagar':
        print("Facturas pendientes:")
        for numero, coste in facturas.items():
            print(f"Factura {numero}: {coste:.2f}€")    
        numero_factura = input("Introduce el número de factura a pagar: ")
        if numero_factura in facturas:
            coste = facturas.pop(numero_factura)
            print(f"Factura {numero_factura} pagada. Se ha cobrado {coste:.2f}€.")
        else:
            print(f"No existe una factura con el número {numero_factura}.")
    elif factura == 'terminar':
        break
    else:
        print("Opción no válida. Por favor, elige 'añadir', 'pagar' o 'terminar'.")
    total_cobrado = sum(facturas.values())
    total_pendiente = sum(facturas.values())
    print(f"Cantidad cobrada hasta el momento: {total_cobrado:.2f}€")
    print(f"Cantidad pendiente de cobro: {total_pendiente:.2f}€")
"""
# Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:
# Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
# Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# # Preguntar por el NIF del cliente y mostrar sus datos.
# Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.

def mostrar_cliente(nif):
    if nif in clientes:
        cliente = clientes[nif]
        print(f"NIF: {nif}, Nombre: {cliente['nombre']}, Dirección: {cliente['direccion']}, Teléfono: {cliente['telefono']}, Correo: {cliente['correo']}, Preferente: {'Sí' if cliente['preferente'] else 'No'}")
    else:
        print("Cliente no encontrado.")
def listar_clientes(preferente=False):
    for nif, cliente in clientes.items():
        if preferente and not cliente['preferente']:
            continue
        print(f"NIF: {nif}, Nombre: {cliente['nombre']}")
def main():
    clientes = {}
    while True:
        
    

