'''
Repetir el punto anterior pero con la expresión que determina que una letra NO es vocal.
'''

letra = str(input("escriba una letra: "))
no_vocal = letra in ['a', 'e', 'i', 'o', 'u']

if no_vocal:
  print(f"la letra {letra} es una vocal")

elif no_vocal == False:
  print(f"la letra {letra} no es una vocal")
else:
    print("ERROR")