'''
Una librería tiene un sistema que guarda los nombres
de todos los libros que tienen en una lista de la
siguiente forma: [“El principito”, “It”, “Sherlock Holmes”...].
Se quiere saber cuántos libros repetidos
tienen. Hacer código que imprima para cada título,
cuántos ejemplares hay.
Aclaración: No se sabe la cantidad de elementos que tiene la lista,
la lista nombrada es solo un ejemplo.
'''
libros = ["El principito", "It", "Sherlock Holmes", "Sherlock Holmes", "Sherlock Holmes"]
def repetido(biblioteca):
    libros_contados = []
    for libro in biblioteca:
        if libro not in libros_contados:
            libros_contados.append(libro)
    for libro in libros_contados:
        print(f"El libro '{libro}' tiene {biblioteca.count(libro)} ejemplares")
repetido(libros)