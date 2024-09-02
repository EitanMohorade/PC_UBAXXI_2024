'''
Hacer una lista con 5 nombres, y realizar las siguientes actividades con la misma:
a. Cambiar el último elemento de la lista y cambiar el último nombre por “Juan”. Olvidándonos de
que sabemos que tiene 5 elementos, ¿Cómo podría saber cuál es el último elemento si no sé la
longitud?
b. Devolver el nombre que esté a dos posiciones del final. ¿Cómo hacemos para que nos funcione
para cualquier lista y no solo para la que tenga 5 elementos?
c. Recorrer la lista e imprimir cada nombre por pantalla.
d. Imprimir por pantalla la lista con 3 repeticiones, usar el operador repetición (*).
'''
nombres = ["jose", "mario", "martina", "dominga", "chavito"]
last = -1
last_2 = last-2
for item in range(0, len(nombres)):
    last += 1
nombres.remove(nombres[last])
nombres.append("Juan")
print(f"ultimo elemento de la lista: {nombres[last]}\n nombre a dos posiciones del final: {nombres[last_2]}\n lista entera: ")
for item in range(0, len(nombres)):
    print(nombres[item])
nombres_por_tres = nombres * 3
print("lista * 3:")
for item in range(0, len(nombres_por_tres)):
    print(nombres_por_tres[item])