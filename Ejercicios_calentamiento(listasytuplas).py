# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
"""

asignaturas = input("Escribe las asignaturas del curso separadas por comas: ").split(", ")
print("Las asignaturas del curso son:")
for asignatura in asignaturas:
    print(asignatura)
"""
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
"""
asignaturas = ["MatemAticas","Fhsica","Química","Historia","Lengua"]
for asignatura in asignaturas:
    print("Yo estudio " + asignatura.strip())       
"""
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
