'''
Se quiere hacer un sistema en la facultad para que un alumno pueda
ir guardando las materias que va
haciendo. Para eso, crear una función que le pregunte al usuario la materia
que quiere almacenar, e ir
guardando la información en una lista hasta que ingrese una ‘X’. ¿
Qué funciones de listas no permiten insertar en una lista?
'''
#Medio que los  ejers no son tan claros, asi que voy a delirar

materias = ["matematicas", "algebra", "quimica"] # lista base


def guardado_de_materias(lista_materias):
    print("Que materia quieres almacenar? ")
    materias_guardadas = []
    for materia in lista_materias:
        print(f"{materia}")
        decision = input("Toca X para seleccionar u otra cosa para pasar: ")
        if decision == "X":
            print(f"seleccionaste la materia {materia}")
            materias_guardadas.append(materia)

guardado_de_materias(materias)