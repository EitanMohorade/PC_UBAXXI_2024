'''
Crear un programa que le solicite al usuario dos números enteros y luego imprima por pantalla:
● la suma de ambos números
● la resta de ambos números
● la multiplicación de ambos números
● la división entera de ambos números
● el resto
Más adelante podríamos crear nuestra propia calculadora :)
'''
num_1 = int(input("ingrese un numero 1 entero: "))
num_2 = int(input("ingrese un numero 2 entero: "))

suma = num_1 + num_2
resta = num_1 - num_2
multi = num_1 * num_2
division = num_1 / num_2
resto = num_1 % num_2

#la \n es para dar un salto de linea en el print y que quede todo mas bonito juas
print(f"resultados de: \n suma: {suma} \n resta: {resta} \n multiplicacion: {multi} \n division: {division} \n resto: {resto}")