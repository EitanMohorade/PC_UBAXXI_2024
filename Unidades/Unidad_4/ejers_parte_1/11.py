'''
Se tiene la siguiente lista de palabras: ["entender", "pueden", "humanos", "los", "que", "código",
"escriben", "programadores", "buenos", "Los", "entiende.", "computadora", "una", "que", "código",
"escribe", "tonto", "Cualquier"]. Hacer una función que reciba una lista, y devuelva un string uniendo
las palabras desde el final de la lista hasta el principio con un " " (espacio) entre cada una, para formar
la frase. (ver funciones de listas y strings).
'''
palabras=["entender", "pueden", "humanos", "los", "que", "código",
"escriben", "programadores", "buenos", "Los", "entiende.", "computadora", "una", "que", "código",
"escribe", "tonto", "Cualquier"]
def escribir(lista):
    lista.reverse()
    lista_completa = " ".join(lista)
    print(lista_completa)
escribir(palabras)