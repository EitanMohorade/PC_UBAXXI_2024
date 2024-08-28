# Tipos de Estructuras de Datos

## 1. Secuencias

### 1.1. Concepto de Secuencia

Una **secuencia** es una serie de elementos que se suceden unos a otros y guardan relación entre sí. Un ejemplo común de secuencia es la **sucesión de Fibonacci**.

### 1.2. Secuencias en Python

En Python, una secuencia es un grupo de elementos con una organización interna que se almacenan de manera contigua en la memoria.

## 2. Tipos de Secuencias en Python

- **Listas**
- **Tuplas**
- **Strings**
- **Rangos**

### 2.1. Rangos (`range`)

Los **rangos** son un tipo de dato que representa una secuencia de números inmutable. Se crean utilizando la función `range()` de diferentes formas:

- `range(fin)`: Crea una secuencia desde `0` hasta `fin - 1`.

```python
  range(20)  # Genera números del 0 al 19
```

- range(comienzo, fin): Crea una secuencia desde comienzo hasta fin - 1.

```python
    range(10, 20)  # Genera números del 10 al 19

```

- range(comienzo, fin, paso): Crea una secuencia desde comienzo hasta fin - 1, incrementando según el valor de paso.

```python
    range(10, 20, 2)  # Genera números: 10, 12, 14, 16, 18
```

Observaciones:

Los valores de comienzo, fin y paso pueden ser negativos.
El valor predeterminado de paso es 1 si no se especifica.

### 2.2. Cadenas de Texto (string)

Un string es una secuencia que almacena caracteres de forma contigua y organizada internamente.

Ejemplo:

```python
    txt = 'Hola a todos'
```

Este string contiene 12 caracteres, donde cada carácter ocupa una posición específica, iniciando desde el índice 0.

### 2.3. Tuplas (tuple)

Las tuplas son secuencias inmutables que pueden contener elementos de diferentes tipos de datos, incluyendo otras estructuras.

Sintaxis:

```python

    mi_tupla = (1, 2, 'hola')
```

Ejemplos de tuplas:

```python
    (8,)
    ()
    (1, 2, 'hola')
    (a, 2, b)
```

Nota: Una tupla con un solo elemento debe incluir una coma al final, por ejemplo (8,), para diferenciarla de una simple expresión entre paréntesis.

Características:

Inmutables: No se pueden modificar después de su creación. Cualquier cambio requiere crear una nueva tupla.

```python

    a = (8, 2, 5)
    a[0] = 1  # Esto producirá un error
```

Operaciones permitidas: Se pueden realizar operaciones como concatenación y repetición, creando nuevas tuplas.

```python

    a = (1, 2)
    a = a * 3  # Resultado: (1, 2, 1, 2, 1, 2)
```

Uso práctico de tuplas: Las tuplas son útiles para estructurar datos de manera ordenada y fija, como en la creación de menús de opciones.

Ejemplo de menú con tuplas:

```python

def menu(opciones):
    '''Arma menú de opciones y devuelve selección entera
    recibe tupla con opciones de menú'''
    print('Selecciona una opción')
    for i in range(1, len(opciones)):
        print(i, '-', opciones[i])
    opc = int(input())
    while opc not in range(1, len(opciones)):
        opc = int(input())
    return opc

quesos = ('', 'cheddar', 'dambo', 'muzzarela', 'brie', 'cremoso', 'sin queso')
panes = ('', 'semillas', 'árabe', 'centeno', 'pebete', 'francés')
carnes = ('', 'hamburguesa', 'jamón cocido', 'jamón crudo', 'lomito', 'salchicha', 'mortadela', 'veggie')
salsas = ('', 'mayonesa', 'guacamole', 'ketchup', 'salsa golf', 'barbacoa', 'ranch', 'sin salsa')
acomp = ('', 'tomate', 'lechuga', 'pepinillos', 'verduras cocidas', 'berenjena escabeche', 'sin extras')

print('Armá tu sandwich')
op1 = menu(panes)
op2 = menu(carnes)
op3 = menu(quesos)
op4 = menu(acomp)
op5 = menu(salsas)
print('Tu pedido de sandwich de pan', panes[op1], 'saldrá pronto')
print('Detalle:', carnes[op2], quesos[op3], acomp[op4], salsas[op5], sep='\n')
```

### 1.2.4. Listas (type list)

Python hace una gran división en sus clases de objetos estructurados con respecto a la posibilidad que tiene cada una de ellos de cambiar dinámicamente, en partes. Aprenderemos a usar una secuencia súper flexible y potente para organizar datos: la lista. Las listas son una secuencia genérica mutable, lo que marca una gran diferencia respecto a las tuplas.

Son secuencias, por lo tanto, la organización interna importa y admiten, como todas las secuencias, un acceso directo (a el o los elementos que deseo); son mutables, por ello pueden cambiar de tamaño y de contenido total, o por partes, y son heterogéneas, por lo que pueden contener cualquier tipo de objeto (otra lista, por ejemplo). Una lista se escribe entre `[]`.

Por ejemplo:

```python
[1, 2]
[4]
[True, 'Hola', 56, (1, 2)]
```

Y se puede asignar como cualquier objeto de datos:

```python

a = [1, 2, 3]
```

Cuando precisamos una lista vacía, la creamos de la siguiente manera:

```python

lis = []
```

Para tener en cuenta

```python

a = [1, 2, 3]
b = [1, 2, 3]
```

No es igual a:

```python

a = [1, 2, 3]
b = a
```

En el primer caso, si bien a y b tienen el mismo tamaño y los mismos valores, son dos variables completamente diferentes. En cambio, en el segundo caso la variable b decimos que es una referencia a la variable a, lo que implica que si modificamos una de las dos, el cambio se ve reflejado en ambas variables.

Si efectivamente queremos tener dos estructuras separadas para que al modificar los datos de una se preserven los datos originales en otra, debemos forzar su copia. Una forma práctica de hacerlo es emplear el método copy():

```python
b = a.copy()
```

Ahora sí copiará los contenidos de la lista a en otra parte de la memoria.

La operación:

```python

lis = [1, 2, 'ya']
lis[2] = 3
```

A diferencia de con las tuplas, es válida. Si hacemos:

```python

print(lis)
```

La salida será [1, 2, 3].

A lis podremos agregarle elementos empleando métodos que realizan dos trabajos: agregan un cajoncito a la estructura y permiten colocar algo dentro (append(), insert(), extend()) o quitárselos también (pop(), remove(), clear()).

```python

lis.append(4)
print(lis)  # la salida será [1, 2, 3, 4]
```

Observación: El método append() modifica directamente lis y no requiere de volver a asignar a la lista. Si bien esa operación de reasignación es válida, estaríamos guardando en la variable lis un objeto nulo (None), que es lo que el método append() devuelve: nada. Y es que append() solo modifica, no retorna ningún valor. Y por definición en python, todas las funciones y métodos que no devuelven nada (no hay return en su cuerpo) devuelven la constante nula None.

Existe una gran variedad de trabajos necesarios para realizar sobre listas de objetos. Y también una buena oferta de métodos predefinidos en la clase para simplificar la tarea. Lo vamos a ver en la siguiente parte del apunte.

### 1.3. Operadores de Secuencias

Para todos los tipos de secuencias que vimos, tenemos definidos ciertos operadores que van a ser nuestras herramientas para programar.

- `x in s`: Devuelve `True` si `x` pertenece a `s`, `False` en caso contrario.
- `s + t`: Concatena la secuencia `s` y `t` en ese orden.
- `s * n`: Concatena `n` veces la secuencia `s`.
- `s[i]`: Referencia el elemento de la posición `i` de la secuencia `s`.
- `s[-k]`: Referencia el elemento que está `k` posiciones antes del final.
- `s[i:j]`: Referencia la porción de la secuencia `s` que va del elemento `i` al `j-1`.
- `s[i:j:k]`: Referencia la porción de la secuencia `s` que va del elemento `i` al `j-1`, con paso `k`.
- `>`, `<`, `>=`, `<=`, `!=`, `==`: Se pueden comparar dos secuencias comparables.
- `len(s)`: Devuelve la longitud de la secuencia `s`.
- `min(s)`: Devuelve el mínimo elemento de `s`.
- `max(s)`: Devuelve el máximo elemento de `s`.
- `sorted(s)`: Devuelve `s` ordenada en forma de lista.
- `reversed(s)`: Devuelve `s` invertida.
- `s.count(x)`: Devuelve el número total de ocurrencias de `x` en `s`.
- `s.index(x[, i[, j]])`: Devuelve el índice de la primera ocurrencia de `x` en `s` (en la posición `i` o superior, y antes de `j`).

### 1.3.1. Métodos Específicos de la clase list (Lista)

La clase lista tiene sus propios métodos (funciones predefinidas) que se pueden utilizar para manipular sus contenidos. Dejamos aquí varios de ellos, los más genéricos:

| Nombre            | Descripción                                                                                      | Ejemplo de Uso                       |
|-------------------|--------------------------------------------------------------------------------------------------|--------------------------------------|
| `append(valor)`   | Agrega el elemento `valor` al final de la lista.                                                  | `miLista.append(5)`                  |
| `insert(posic,valor)` | Inserta el elemento `valor` en la posición `posic`.                                              | `miLista.insert(2, 10)`              |
| `remove(valor)`   | Quita de la lista el elemento `valor`.                                                            | `miLista.remove(7)`                  |
| `pop([índice])`   | Quita de la lista el elemento de la posición `índice`.                                             | `valor = miLista.pop(3)`             |
| `extend(otraLista)` | Agrega los elementos de `otraLista` al final de la lista.                                        | `miLista.extend([8, 9, 10])`         |
| `sort()`          | Ordena la lista.                                                                                  | `miLista.sort()`                     |
| `sorted()`        | Devuelve una nueva lista ordenada (sin modificar la original).                                    | `lista_ordenada = sorted(miLista)`   |
| `reverse()`       | Invierte el orden de la lista.                                                                    | `miLista.reverse()`                  |
| `count(valor)`    | Cuenta la cantidad de apariciones de `valor` en la lista. Este método es válido para cualquier secuencia. | `cantidad = miLista.count(5)`        |
| `index(valor)`    | Devuelve el índice de la primera aparición de `valor`. Este método es válido para cualquier secuencia. | `indice = miLista.index(8)`          |
| `len()`           | Devuelve la longitud de la lista. Este método es válido para cualquier secuencia.                 | `longitud = len(miLista)`            |
| `clear()`         | Elimina todos los elementos de la lista.                                                          | `miLista.clear()`                    |
| `copy()`          | Crea una copia superficial de la lista.                                                           | `copia = miLista.copy()`             |
| `max()`           | Devuelve el valor máximo de la lista.                                                             | `maximo = max(miLista)`              |
| `min()`           | Devuelve el valor mínimo de la lista.                                                             | `minimo = min(miLista)`              |
| `sum()`           | Devuelve la suma de los elementos de la lista.                                                    | `suma = sum(miLista)`                |

### 1.4. Ejemplos

¿Cómo cargamos una lista con datos ingresados por el usuario? ¿Cómo mostramos el contenido de una lista?

Ejemplo de carga e impresión de listas:

```python

    nombres = []
    nom = input('Ingrese un nombre, * para salir: ')
    while nom != '*':
        nombres.append(nom)
        nom = input('Ingrese un nombre, * para salir: ')
    print('Lista de Nombres')
    print(nombres)
    print('Salida detallada')
    for n in nombres:
        print(n)
```

Considerando que las listas son secuencias, podemos usar solo partes de ellas, por ejemplo, para un for.

Ejemplo con Listas:

```python

    from random import randint
    a = []
    for i in range(20):
        a.append(randint(1, 35))
    print('Segunda Mitad')
    for n in a[10:]:
        print(n, end=' ')
    print()
    print('Primera Mitad')
    for n in a[:10]:
        print(n, end=' ')
    print()
```

## 1.5 Accediendo a los elementos de una secuencia

Dado que podemos armar una lista con cualquier colección de objetos, podríamos crear una lista de listas. Este recurso es el que podemos emplear para representar matrices o tablas de datos de manera sencilla; se puede armar listas de filas, donde cada fila es una lista (si necesitaré modificar los datos), y también puede ser cada fila una tupla (si no habrá cambios una vez que se haya agregado la fila).

Cuando en una lista (o estructura de datos en general) hay otro objeto estructurado, para poder acceder a objetos individuales que están dentro de otros, se debe referenciar cada nivel por separado, de izquierda a derecha, siguiendo el orden desde el más externo al más interno.

**Ejemplo:**

```python
lis = [1, 2, 3]
# Para referenciar al 2:
lis[1]
```

En la siguiente lista:

```python
lis = [1, (1, 0, 2), 3]
# Para referenciar el 2 (que está como tercer elemento de una tupla, que a su vez es el segundo elemento de la lista):
lis[1][2]
```

Y si tuviéramos:

```python
lis = [('uno', 'dos', 'tres'), (1, 2, 3)]
```

Observamos que tenemos una lista con dos elementos y cada uno es una tupla con tres elementos. La segunda tupla tiene elementos simples (no son estructuras o iterables), números; mientras que la primera tiene tres elementos que son una secuencia cada uno.

¿Cuántos niveles debes indicar para referenciar la 'u' de 'uno'?

3

¿Cómo sería eso?

```python
lis[0][0][0]
```

El [0] de la izquierda referencia la tupla ('uno', 'dos', 'tres'). El siguiente [0] (siempre sentido izquierda-derecha) referencia la string 'uno'. El último [0] referencia 'u' (de 'uno').

Para no perdernos en el intento de utilizar estructuras complejas, sólo debemos tener un esquema gráfico a mano para individualizar en qué nivel de profundidad se encuentra el dato que queremos alcanzar. Así se va bajando de nivel en nivel, referenciándolos uno por uno con un par de [] que se agregarán de izquierda a derecha por cada nivel que descendamos.

Ejemplo de armado de sándwiches:

```python

def menu(opciones):
    '''Arma menú de opciones y devuelve selección entera.
    Recibe tupla con opciones de menú.'''
    print('Selecciona una opción')
    for i in range(1, len(opciones)):
        print(i, '-', opciones[i][0])
    opc = int(input())
    while opc not in range(1, len(opciones)):
        opc = int(input())
    return opc

quesos = ('', ('cheddar', 75), ('dambo', 60), ('sin queso', 0))
panes = ('', ('árabe', 70), ('pebete', 70), ('francés', 60))
carnes = ('', ('hamburguesa', 200), ('jamón cocido', 150), ('lomito', 200), ('salchicha', 100), ('veggie', 0))

sand = []
print('Armá tu sandwich')
op1 = menu(panes)
sand.append(panes[op1][1])
op2 = menu(carnes)
sand.append(carnes[op2][1])
op3 = menu(quesos)
sand.append(quesos[op3][1])
print('Tu pedido de sandwich de pan', panes[op1][0], 'saldrá pronto')
print('Detalle:', carnes[op2][0], quesos[op3][0], sep='\n')
print('Abonar: $%.2f' % sum(sand))
```

### 1.6 Métodos de la clase str (String)

Algunos metodos comunespara la clase String son:

## Métodos de la clase str (String)

| Nombre                   | Descripción                                                                                       | Ejemplo de Uso                                   |
|--------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------|
| `capitalize()`           | Devuelve el string con la primera letra en mayúscula.                                              | `"hola".capitalize()`                           |
| `center(ancho[, relleno])` | Devuelve el string centrado con relleno a los costados.                                            | `"Python".center(10, "*")`                      |
| `count(valor)`           | Devuelve la cantidad de veces que aparece `valor` en el string.                                  | `"banana".count("a")`                           |
| `find(substring[, desde[, hasta]])` | Devuelve la primera posición de comienzo del `substring` en el string.                           | `"python".find("th")`                           |
| `rfind(substring[, desde[, hasta]])` | Devuelve la última posición de comienzo del `substring` en el string.                           | `"python programming".rfind("ing")`            |
| `format(args, *)`        | Devuelve el string formateado con valores sustituidos.                                             | `"Mi nombre es {} y tengo {} años".format("Juan", 25)` |
| `upper()`                | Devuelve el string en mayúsculas.                                                                  | `"hola".upper()`                                |
| `lower()`                | Devuelve el string en minúsculas.                                                                  | `"Hola".lower()`                                |
| `strip()`                | Devuelve el string sin espacios en blanco al inicio y al final.                                    | `" Python ".strip()`                            |
| `replace(viejo, nuevo)`  | Devuelve el string con todas las apariciones de `viejo` reemplazadas por `nuevo`.                   | `"Hello, World!".replace("Hello", "Hi")`       |
| `split([separador])`     | Devuelve una lista de substrings separados por `separador`.                                        | `"apple,banana,grape".split(",")`              |
| `join(iterable)`         | Devuelve un string que es la concatenación de los elementos en el iterable.                         | `",".join(["apple", "banana", "grape"])`       |
| `isdigit()`              | Devuelve `True` si todos los caracteres son dígitos.                                                | `"12345".isdigit()`                            |
| `isalpha()`              | Devuelve `True` si todos los caracteres son letras.                                                | `"Python".isalpha()`                           |
| `startswith(substring)`  | Devuelve `True` si el string comienza con `substring`.                                              | `"Hello, World!".startswith("Hello")`          |
| `rindex(substring[, desde[, hasta]])` | Devuelve la última posición de comienzo del `substring` en el string.                           | `"python programming".rindex("ing")`           |
| `ljust(ancho[, relleno])` | Justifica el string hacia la izquierda con relleno.                                                | `"Python".ljust(10, "-")`                      |
| `rjust(ancho[, relleno])` | Justifica el string hacia la derecha con relleno.                                                  | `"Python".rjust(10, "-")`                      |
| `maketrans(x[, y[, z]])` | Asocia en un diccionario los correspondientes caracteres de las cadenas `x` e `y`.                 | `str.maketrans("aeiou", "12345")`              |
| `translate(pares)`       | Devuelve el string con los caracteres asociados en el diccionario `pares` reemplazados.             | `"hello".translate(str.maketrans("aeiou", "12345"))` |

## 1.6.1 Ejemplos

**Ejemplo 1:**

```python
texto = "Bienvenido a mi aplicación{0}"
print(texto.format(" en Python"))
```

Retorna:

```css
Bienvenido a mi aplicación en Python
```

Ejemplo 2:

```python

texto = "Bruto: ${bruto} + IVA: ${iva} = Neto: ${neto}"
print(texto.format(bruto=100, iva=21, neto=121))
```

Retorna:

```bash
Bruto: $100 + IVA: $21 = Neto: $121
```

Ejemplo 3:

```python

tup = ('a', 'b', 'c')
print('-'.join(tup))

```

Retorna:

```css

a-b-c
```

Ejemplo 4:

```python

vocales = "aeiou"
numeros = "12345"
texto = "murcielagos"
print(texto.maketrans(vocales, numeros))
```

Retorna:

```yaml

{97: 49, 111: 52, 117: 53, 101: 50, 105: 51}
```

Ejemplo 5:

```python

vocales = "aeiou"
acentos = "áéíóú"
texto = "murcielagos"
parejas = texto.maketrans(vocales, acentos)
print(texto.translate(parejas))
```

Retorna:

```css
múrcíélágós
```
