'''
 Crear una función que dado un número, devuelva su valor absoluto. El valor absoluto de un número es
el mismo número sin considerar el signo.
Por ejemplo, el absoluto de 2 es 2 (|2| = 2) y el absoluto de -4 es 4 (|-4|=4).
'''

def valor_absoluto(numero):
 if numero < 0:
   return numero * -1
 else:
   return numero

print(valor_absoluto(-8))