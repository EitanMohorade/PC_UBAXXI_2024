'''
Un matrimonio está organizando una fiesta y tiene que armar una lista de invitados. Cada uno tiene su propia
tupla y guarda en ella a todos los que quiere invitar.
 Si alguien cancela tienen que sacarlo de la tupla.
Hacer una función que reciba la tupla y un nombre, y devuelva una nueva tupla sin el nombre pasado
por parámetro.
Las tuplas son inmutables, entonces ¿Cómo podemos hacer para “eliminar” un elemento de una tupla?
Recordemos que las tuplas tienen definido el operador +, pero no el operador -.
'''

def fun(lista,num):
    if num in range(0,9,2):
        resultado=lista[num//2].upper()
    else:
        resultado='Indefinido'
    return resultado
print(fun(['cero','dos','cuatro','seis','ocho'], 4))