'''
Obtener una palabra e imprimir la cantidad de letras.
'''
def cant_letras(palabra):
    letras = 0
    for letra in palabra:
        letras += 1
    return letras

print(cant_letras("oa"))