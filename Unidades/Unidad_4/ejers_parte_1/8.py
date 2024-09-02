'''
Se quiere guardar información de los siguientes países: Francia, Argentina, Japón, Alemania, Perú.
a. Crear una tupla para cada país que contenga su nombre, su capital y el continente donde se
encuentra.
b. Guardar las tuplas en una lista.
c. Hacer una función que reciba por parámetros la lista, e imprima la información de cada país
con el siguiente formato:
País: <nombre>
Capital: <capital>
Continente: <continente>
Por ejemplo:
País: Japón
Capital: Tokio
Continente: Asia
'''
francia = ("Francia", "París", "Europa")
argentina = ("Argentina", "Buenos Aires", "América del Sur")
japon = ("Japón", "Tokio", "Asia")
alemania = ("Alemania", "Berlín", "Europa")
peru = ("Perú", "Lima", "América del Sur")
paises = [francia, argentina, japon, alemania, peru]
def datos_de_pais(lista_paises):
    for pais in lista_paises:
        print(f"Pais: {pais[0]}\nCapital: {pais[1]}\nContinente: {pais[2]}\n")
datos_de_pais(paises)