'''
 Crear una lista que contenga los números del 1 al 10, luego recorrerla y guardar en otra lista esos
números elevados al cuadrado.
'''
numeros = [1,2,3,4,5,6,7,8,9,10]
numeros_alcuadrado = []
for numero in numeros:
    print(f"numero: {numero} elevado al cuadrado es: {pow(numero, 2)}")
    numeros_alcuadrado.append(pow(numero, 2))