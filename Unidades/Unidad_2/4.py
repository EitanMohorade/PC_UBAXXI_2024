'''
Escribir un programa que le pida a un usuario su año de nacimiento y otro año, y le diga qué edad tenía
el usuario en el año ingresado.
'''

fecha_nacimiento = int(input("escriba en que ano naciste: "))
ano_actual = int(input("decime un ano y yo te digo cuantos anos tuviste en esa fecha: "))

edad = ano_actual - fecha_nacimiento

print(f"usted tiene/tuvo {edad} en {ano_actual}")