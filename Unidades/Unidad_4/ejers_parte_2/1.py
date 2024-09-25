'''
Hacer una función que reciba un string y que imprima solamente los caracteres que sean vocales
'''
def vocales(string):
    vocales = ["a", "e", "i", "o", "u"]
    letras = []
    for item in string.lower():
        if item in vocales:
            letras.append(item)
    return letras
for item in vocales("HolA manolaeu"):
    print(item)