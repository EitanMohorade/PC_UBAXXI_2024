'''
Escribir la expresión para saber si un número es más grande que otro. Guardarla en una variable de tipo
bool e imprimirla por pantalla para ver su valor
'''
num_1 = int(input("escriba un numero: "))
num_2 = int(input("escriba otro numero: "))
es_mayor = num_1 > num_2
if es_mayor:
  print(f"numero {num_1} mayor a {num_2}")
else:
    print(f"numero {num_1} menor o igual a {num_2}")