# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
""""
edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("No eres mayor de edad.") 
"""

# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""
contraseña ="contraseña"
contraseña_usuario = input("Introduce la contraseña: ")
if contraseña_usuario.lower() == contraseña.lower():
    print("Contraseña correcta.")
else:
    print("Contraseña incorrecta.")
"""

#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
input_usuario = input("Que pizza desea Vegetariana [1[ o No Vegetariana [2]: ")

match input_usuario:
    case "1":   
        print("Ingredientes disponibles para la pizza vegetariana:")
        print("1. Pimiento")
        print("2. Tofu")
        ingrediente = input("Elija un ingrediente: ")
        if ingrediente == "1":
            ingrediente_seleccionado = "Pimiento"
        elif ingrediente == "2":
            ingrediente_seleccionado = "Tofu"
        else:
            print("Ingrediente no válido.")
            ingrediente_seleccionado = ""
        if ingrediente_seleccionado:
            print("Has elegido una pizza vegetariana con: Mozzarella, Tomate y " + ingrediente_seleccionado + ".")
    case "2":
        print("Ingredientes disponibles para la pizza no vegetariana:")
        print("1. Peperoni")
        print("2. Jamón")
        print("3. Salmón")
        ingrediente = input("Elija un ingrediente: ")
        if ingrediente == "1":
            ingrediente_seleccionado = "Peperoni"
        elif ingrediente == "2":
            ingrediente_seleccionado = "Jamón"
        elif ingrediente == "3":
            ingrediente_seleccionado = "Salmón"
        else:
            print("Ingrediente no válido.")
            ingrediente_seleccionado = ""
        if ingrediente_seleccionado:
            print(f"Has elegido una pizza no vegetariana con: Mozzarella, Tomate y " + ingrediente_seleccionado + ".")
