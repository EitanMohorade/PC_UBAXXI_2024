'''
Se tienen letras para representar las estaciones del año:
● V para verano
● O para otoño
● I para invierno
● P para primavera
Crear una función que dada una letra, imprima por pantalla la estación del año que representa (es
decir, si se ingresa V se mostrará por pantalla el mensaje “Verano”). En caso de no representar a
ninguna estación mostrar un mensaje que diga “error”. Probar la función creada llamándola con A, P, O,
B, V e I.
'''

def estaciones_del_ano(letra):
    if letra == "V":
      return "Verano"
    elif letra == "O":
      return "Otoño"
    elif letra == "I":
      return "Invierno"
    elif letra == "P":
      return "Primavera"
    else:
      return "error"

print(estaciones_del_ano("A"))
print(estaciones_del_ano("P"))
print(estaciones_del_ano("O"))
print(estaciones_del_ano("V"))
print(estaciones_del_ano("B"))
print(estaciones_del_ano("I"))