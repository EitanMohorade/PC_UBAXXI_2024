'''
Crear una secuencia con números distintos, y luego devolver el elemento máximo y el mínimo.
'''
lista=[3,5,34,8,9,3,4,6,8,3,123,1]
maxim = lista[0]
minim = lista[0]
for item in range(len(lista)):
    if lista[item] >= maxim:
        maxim = lista[item]
    elif lista[item] <=  minim:
        minim = lista[item]
print(f"el maximo de la lista es {maxim} y el minimo es {minim}")