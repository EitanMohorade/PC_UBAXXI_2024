'''
Repetir pero para la expresión que permite saber si un número es par y menor a 10.
'''
num = int(input("escriba un numero: "))

par = num % 2 == 0
menor_10 = num < 10

if par & menor_10:
  print(f"numero {num} par y menor a 10")
else:
  print(f"numero {num} no cumple con las condiciones de ser par y menor de 10 simultaneamente")