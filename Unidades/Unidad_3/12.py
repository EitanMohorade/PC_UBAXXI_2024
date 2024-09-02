'''
Escribir código que recorra los números del 1 al 20 y
determine para cada uno si es par o impar,
imprimiendo un mensaje por pantalla en cada caso.
Es decir, el output esperado sería:
> El número 1 es impar.
> El número 2 es par.
…
> El número 20 es par.
'''
def es_par_o_impar_uno_al_veinte():
    for item in range(20):
        if (item+1) % 2 == 0:
            print(f"el numero {item+1} es par")
        else:
            print(f"el numero {item+1} es impar")
es_par_o_impar_uno_al_veinte()