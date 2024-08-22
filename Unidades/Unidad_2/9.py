'''
Pedirle nombre y apellido por separado e imprimir “Apellido, Nombre”.
Este proceso se llama concatenar cadenas.
'''
def nombre_completo():
    nombre = input("ingrese el nombre: ")
    apellido = input("ingrese el apellido: ")
    print(f"{apellido}, {nombre}")

nombre_completo()