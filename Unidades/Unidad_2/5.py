'''
Crear un programa que le solicite al usuario 5 enteros y muestre por pantalla el promedio de ellos.
Es muy común usar variables para acumular valores.
'''
#no usare el ciclo for pq aun no lo aprendimos
num_1 = int(input("ingresa el numero 1 entero: "))
num_2 = int(input("ingresa el numero 2 entero: "))
num_3 = int(input("ingresa el numero 3 entero: "))
num_4 = int(input("ingresa el numero 4 entero: "))
num_5 = int(input("ingresa el numero 5 entero: "))

promedio = (num_1 + num_2 + num_3 + num_4 + num_5) / 5

print(f"el promedio de los 5 numeros que ingresaste es de: {promedio}")