'''
Se quiere mejorar el programa para enseñar
matemáticas pensado en el ejercicio anterior. Ahora se
necesita una funcionalidad que permita a los niños
aprender las tablas. Crear una función que reciba un
número entero e imprima por pantalla la tabla de ese número del 1 al 10.
'''
def aprender_las_tablas(entero):
    for item in range(10):
        print(f"{item+1} * {entero} = {(item+1) * entero}")
aprender_las_tablas(7)