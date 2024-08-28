'''
Crear el programa al que sea imposible ganarle en el juego de “Piedra, papel o tijera”. Cada elemento va
a ser representado con una letra: R para piedra, P para papel y T para tijera.
a. Hacer una función que le haga al usuario ingresar alguna de esas letras, e imprima por pantalla
la jugada para ganarle. Por ejemplo:

> ¡Juguemos! Ingresá piedra ( R), papel (P) o tijera (T)
> P
> Tijera. ¡Te gané!

ATENCIÓN: Observar cómo se usa una frase inicial para darle a entender al usuario lo que tiene
que hacer (en este caso ingresar alguna de las tres letras).
b. Mostrar por pantalla el mensaje “NO vale” cuando el usuario ingresa una letra no válida
(distinta de R, P o T).
'''
def piedra_papel_tijera():
    letra = input("Juguemos! ingresa piedra (R), papel (P) o tijera (T): ")
    if letra == "R":
      print(f"tu jugada fue {letra} \n . Papel: Te gane.")
    elif letra == "P":
      print(f"tu jugada fue {letra} \n . Tijera: Te gane.")
    elif letra == "T":
        print(f"tu jugada fue {letra} \n . Piedra: Te gane.")
    else:
        print("NO vale")
    
piedra_papel_tijera()