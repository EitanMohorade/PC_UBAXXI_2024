'''
. Escribir código que dado dos enteros, determine si la suma de ambos da menos que 100. Si la suma de
ambos es menor a 100, calcular cuánto falta para llegar a 100 y mostrar por pantalla un mensaje con
ese valor. Si la suma es mayor a 100, mostrar un mensaje diciendo “Llega a 100”.
Extra: ¿Cómo harían para que el programa quede generalizado para cualquier límite, a elección del
usuario, y no solo para 100?.
'''

def calculos(entero_1, entero_2, numero_a_llegar):
    suma = entero_1 + entero_2
    if suma < numero_a_llegar:
        falta = numero_a_llegar - suma
        print(f"Hace falta {falta} para que la suma entre {entero_1} y {entero_2} llegue a {numero_a_llegar}.")
    elif suma >= numero_a_llegar:
        print(f"Llega a {numero_a_llegar}")

calculos(50, 45, 100)