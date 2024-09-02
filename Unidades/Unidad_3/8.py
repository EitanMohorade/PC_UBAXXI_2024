'''
Se quiere hacer un programa para enseñar a unos niños a contar.
Crear una función que reciba un
número entero e imprima por pantalla los números
del 1 hasta ese número con la estructura de control
iterativa for.
'''
def aprender_a_contar(entero):
    for item in range(entero):
        print(item+1)
aprender_a_contar(5)