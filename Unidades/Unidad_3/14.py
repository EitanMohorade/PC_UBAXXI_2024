'''
Crear una función que reciba un número entero e imprima los números primos entre 0 y el número
ingresado.
AYUDA: un número es primo cuando solamente es divisible por sí mismo y por 1,
es decir que para ver
si es primo hay que ver que el módulo (%) de ese número con los
anteriores hasta el 1 (sin incluirlo) sea
distinto de 0, o sea que no sea divisible
'''
def nums_primos(entero):
    for num in range(2, entero + 1):
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            print(f"{num} es primo")
nums_primos(32)