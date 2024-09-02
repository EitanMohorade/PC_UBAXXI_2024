# 1. Recursos con Listas

Las listas, strings, rangos y tuplas son tipos de secuencias en Python. Como Python utiliza un enfoque de programación **Orientado a Objetos (OO)**, todas las operaciones y métodos definidos para secuencias se aplican a estas estructuras. Esto se debe a la herencia de propiedades en OO.

## Métodos de Listas

| Método                   | Definición                                                                                         | Ejemplo                                         |
|--------------------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------|
| `append(valor)`          | Agrega el elemento `valor` al final de la lista.                                                  | `lista = [2, 3, 5]`<br>`lista.append(1)`<br>`# la lista queda: [2, 3, 5, 1]` |
| `insert(posición, valor)` | Inserta el elemento `valor` en la posición `posición`.                                              | `lista = ['h', 'l', 'a']`<br>`lista.insert(1, 'o')`<br>`# la lista queda: ['h', 'o', 'l', 'a']` |
| `remove(valor)`          | Quita de la lista el elemento `valor`.                                                             | `lista = [1, 3, 5]`<br>`lista.remove(3)`<br>`# la lista queda: [1, 5]` |
| `pop([índice])`          | Quita de la lista el elemento de la posición `índice`. Si no se usa este parámetro, se quita el último elemento. | `lista = ['d', 'i', 'a', 'a']`<br>`valor = lista.pop()`<br>`# la lista queda: ['d', 'i', 'a']`<br>`# y en la variable valor queda guardado el elemento que sacamos (en este caso 'a')` |
| `extend(otra_lista)`    | Agrega al final de la lista `otra_lista`.                                                            | `lista = [1, 2, 2]`<br>`otra_lista = [4, 7]`<br>`lista.extend(otra_lista)`<br>`# la lista queda: [1, 2, 2, 4, 7]` |
| `sort([reverse=True], [key=función])` | Ordena la lista. Si se emplea el parámetro `reverse`, en orden descendente; si se usa `key`, con criterio de ordenamiento `función`. | `lista = [1, 4, 3, 2]`<br>`lista.sort()`<br>`# la lista queda: [1, 2, 3, 4]` |
| `reverse()`              | Invierte el orden de la lista (el primero pasa a ser último).                                      | `lista = ['h', 'o', 'l', 'a']`<br>`lista.reverse()`<br>`# la lista queda: ['a', 'l', 'o', 'h']` |
| `count(valor)`           | Cuenta la cantidad de apariciones de `valor` en la lista.                                          | `lista = [4, 1, 2, 5, 1]`<br>`cantidad = lista.count(1)`<br>`# la lista queda igual y cantidad vale 2 porque el 1 aparece dos veces` |
| `index(valor)`           | Devuelve la posición de la primera aparición de `valor` en la lista.                              | `lista = [1, 4, 3, 2]`<br>`lugar = lista.index(4)`<br>`# la lista queda igual y lugar vale 1 porque el 4 está en la posición 1` |

## Ordenamiento de Estructuras

### Métodos de Ordenamiento

En Python, podemos ordenar listas y otras secuencias utilizando dos enfoques principales: el método `sort()` y la función `sorted()`.

- **`sort()`**: Ordena la lista sobre la que se aplica y no devuelve nada (modifica la lista original).

  ```python
    lista = [4, 1, 2, 7]
    lista.sort()
    # lista queda: [1, 2, 4, 7]
    ```

- sorted(): Devuelve una nueva lista ordenada, sin modificar la original (se puede usar con cualquier secuencia).

```python
    lista = [4, 1, 2, 7]
    lista_ordenada = sorted(lista)
    # lista queda igual, lista_ordenada es: [1, 2, 4, 7]
```

Conceptos Clave

- Algoritmos de Ordenamiento: Se encargan de reordenar los elementos de una estructura de datos. No importa el estado inicial; el resultado final debe ser el mismo.
- Esfuerzo Computacional: Ordenar puede ser costoso en términos de rendimiento, especialmente con listas grandes. Sin embargo, Python ofrece métodos eficientes para estas tareas.

Implicaciones:

- Al usar sort(), la lista original es modificada.
- Al usar sorted(), se crea una nueva lista ordenada sin alterar la original.

## Ordenamiento y Reversión de Secuencias

### Función `sorted()` y Método `sort()`

- **`sorted()`**:
  - Devuelve una nueva lista ordenada.
  - Puede ordenar en forma descendente usando el argumento `reverse=True`.
  - Ejemplo:

    ```python
        lista = [10, 22, -3.5, 0]
        print('Lista inicial:')
        print(lista)
        print('Lista ordenada descendente:')
        lista_ordenada = sorted(lista, reverse=True)
        print(lista_ordenada)
        # Salida:
        # Lista inicial:
        # [10, 22, -3.5, 0]
        # Lista ordenada descendente:
        # [22, 10, 0, -3.5]
    ```

- **`sort()`**:
  - Ordena la lista original in-place.
  - También puede ordenar en forma descendente usando el argumento `reverse=True`.
  - Ejemplo:

    ```python
        lista = [10, 22, -3.5, 0]
        print('Lista inicial:')
        print(lista)
        print('Lista ordenada descendente:')
        lista.sort(reverse=True)
        print(lista)
        # Salida:
        # Lista inicial:
        # [10, 22, -3.5, 0]
        # Lista ordenada descendente:
        # [22, 10, 0, -3.5]
    ```

### Diferencias Clave

- `sort(reverse=True)` vs. `reverse()`:
  - `sort(reverse=True)` ordena la lista en forma descendente.
  - `reverse()` solo invierte el orden de los elementos sin ordenarlos.
  - Ejemplo:

    ```python
    lista = [10, 22, -3.5, 0]
    lista.sort(reverse=True)
    # [22, 10, 0, -3.5]

    lista.reverse()
    # [-3.5, 0, 10, 22]
    ```

- **Ejemplo con `reverse()` y `sort()`**:

```python
  lista = [10, 22, -3.5, 0]
  lista.reverse()  # Invierte el orden
  lista.sort()      # Ordena en forma ascendente
  # Resultado: [-3.5, 0, 10, 22]
```

## 1.1.2. Usando Criterios de Ordenamiento no Estándar

### Ordenamiento de Strings

El método `sort()` y la función `sorted()` ordenan elementos en una lista basándose en el código Unicode. Para una comparación más adecuada (como ordenar alfabéticamente sin distinguir mayúsculas de minúsculas), podemos usar el argumento `key`.

#### Ejemplo: Ordenar Strings Ignorando Mayúsculas/Minúsculas

- **Código Original**:

```python
  lista = ['Juan', 'ana', 'sergio', 'ELEna', 'ELEONORA', 'anALía']
  print('Lista Inicial')
  for n in lista:
      print(n)
  lista.sort(key=str.lower)
  print('\nLista Ordenada')
  for n in lista:
      print(n)
```

Salida:

```css

Lista Inicial
Juan
ana
sergio
ELEna
ELEONORA
anALía

Lista Ordenada
ana
anALía
ELEna
ELEONORA
Juan
sergio
```

Ejemplo: Ordenar por Longitud de Strings
Código:

```python

lista = ['Juan', 'ana', 'sergio', 'ELEna', 'ELEONORA', 'anALía']
print('Lista Inicial')
for n in lista:
    print(n)
lista.sort(key=len)
print('\nLista Ordenada')
for n in lista:
    print(n)
```

Salida:

```css

Lista Inicial
Juan
ana
sergio
ELEna
ELEONORA
anALía

Lista Ordenada
ana
Juan
ELEna
sergio
anALía
ELEONORA
```

Funciones Personalizadas para Ordenamiento
Si los criterios de ordenamiento no están cubiertos por las funciones estándar, podemos definir nuestra propia función para el parámetro key.

Ejemplo: Ordenar por Cantidad de Vocales
Código:

```python

def cant_vocales(palabra):
    palabra = palabra.lower()
    cant = 0
    for v in 'aeiouáéíóú':
        cant += palabra.count(v)
    return cant

lista = ['Juan', 'ana', 'sergio', 'ELEna', 'ELEONORA', 'anALía']
print('Lista Inicial')
for n in lista:
    print(n)
lista.sort(reverse=True, key=cant_vocales)
print('\nLista Ordenada')
for n in lista:
    print(n)
```

Salida:

```css

Lista Inicial
Juan
ana
sergio
ELEna
ELEONORA
anALía

Lista Ordenada
ELEONORA
anALía
sergio
ELEna
Juan
ana
```

## 1.2. Map y Filter

Función map()

map() aplica una función a cada elemento de una secuencia y devuelve un iterable con los resultados.

Sintaxis:

```python

map(función, secuencia)
```

Ejemplo: Elevar al Cuadrado Cada Elemento de una Lista
Código:

```python

def cuadrado(numero):
    return numero * numero

lista = [3, 6, 1, 2]
print("Lista:", lista)
nueva_lista = list(map(cuadrado, lista))
print("Nueva lista:", nueva_lista)
```

Salida:

```yaml

Lista: [3, 6, 1, 2]
Nueva lista: [9, 36, 1, 4]
```

Nota: map() devuelve un iterable que se puede convertir en lista usando list(), si es necesario para su visualización.

## 1.2.2. Filter()

La función `filter()` selecciona elementos de una secuencia basándose en una función booleana (una función que devuelve `True` o `False`). Solo los elementos para los que la función devuelve `True` son incluidos en la secuencia resultante.

### Sintaxis de `filter()`

```python
filter(función, secuencia)
```

- función: Evalúa cada elemento de la secuencia.
- secuencia: La secuencia de elementos a filtrar.
Ejemplo: Filtrar Palabras que Empiezan con 'm'
Código:

```python

def empieza_con_m(palabra):
    return palabra[0] == 'm'

lista = ["manzana", "balde", "molde", "marrón", "carro", "pera"]
print("Lista:")
for i in lista:
    print(i)
print()
nueva_lista = list(filter(empieza_con_m, lista))
print("Nueva lista:")
for n in nueva_lista:
    print(n)
```

Salida:

```yaml

Lista:
manzana
balde
molde
marrón
carro
pera

Nueva lista:
manzana
molde
marrón
```

Ejemplo: Cuadrados y Números Pares
Código:

```python

def cuadrado(x):
    return x ** 2

def par(x):
    return x % 2 == 0

lista = [1, 2, 3, 4, 5, 6]
print('Lista Original')
print(lista)

lis = list(map(cuadrado, lista))
print('Lista de cuadrados')
print(lis)

filtro = list(filter(par, lista))
print('Lista de Pares')
print(filtro)
```

Salida:

```csharp

Lista Original
[1, 2, 3, 4, 5, 6]

Lista de cuadrados
[1, 4, 9, 16, 25, 36]

Lista de Pares
[2, 4, 6]
```

Nota: filter() devuelve un iterable, por lo que se debe convertir a lista usando list() para almacenar los resultados en una variable y trabajar con ellos.