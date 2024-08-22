# Sentencias Básicas

Para crear un programa hay q seguir una serie de sentencias que se ejecutan de arriba hacia abajo, esto se lo llama como ``Flujo de Control de un Programa`` (FCP).

## Comunicación con el Usuario

En Python, la comunicación con el usuario se realiza a través del teclado (entrada) y la pantalla (salida). Para agarrar el dato del usuario, usamos la función ``input()``. Para mostrar información, utilizamos la función ``print()``.

## Manejo de Datos

Los datos en un programa pueden ser constantes (valores fijos) o variables (valores que pueden cambiar). Es importante nombrar las variables de manera clara y consistente, preferiblemente en minúsculas, y utilizar nombres descriptivos como numero o edad_mayor_hijo.

## Tipos de Datos

Python maneja varios tipos de datos predefinidos:

* Entero (``int``): números enteros.
* Real (``float``): números decimales.
* Complejo (``complex``): números con parte real e imaginaria.
* Booleano (``bool``): valores True o False.
* Texto (``str``): cadenas de caracteres, que pueden ser manipuladas como secuencias.

Al escribir un programa, Python reconoce automáticamente el tipo de dato y lo maneja en consecuencia.

## Operadores en Python

Python tiene varios operadores para realizar operaciones aritméticas y de manipulación de texto.

## Operadores Aritméticos

* ``+`` Suma: 10 + cant
* ``-`` Resta: saldo - pago
* ``*`` Producto: a * 20
* ``/`` División con Precisión Decimal: a / 3.5
* ``//`` División Entera: a // 12
* ``%`` Resto: numPar % 2
* ``+=`` Suma Abreviada: a += 3 (equivale a a = a + 3)
* ``-=`` Resta Abreviada: a -= 3 (equivale a a = a - 3)
* ``*=`` Producto Abreviado: a *= 3 (equivale a a = a * 3)
* ``/=`` División Abreviada: a /= 3 (equivale a a = a / 3)
* ``//=`` División Entera Abreviada: a //= 3 (equivale a a = a // 3)
* ``%=`` Resto Abreviado: a %= 3 (equivale a a = a % 3)

## Operadores de Edición de Texto

* ``+`` Concatenación: 'hola' + ' juan' → 'hola juan'
* ``*`` Repetición: 'ja' * 3 → 'jajaja'
* ``[k] o [-k]`` Selección de Caracter: a = 'hola', a[0] → 'h'
* ``[i:j:p]`` Selección de Porción de Texto: a[0:2] → 'ho'
* ``+=`` Concatenación Abreviada: a += 'y chau' → 'holay chau'
* ``*=`` Repetición Abreviada: a *= 2 → 'holahola'

## Escribiendo un Programa en Python

Para mostrar un mensaje en pantalla, como "Hola Mundo":

``` python
    print('Hola Mundo')
```

Esto mostrará en pantalla: Hola Mundo.

### Ejemplo Práctico

Si queremos preguntar la edad de Juan y mostrarla:

``` python
    print('Ingrese la edad de Juan')
    edad = input()  # El usuario ingresa la edad
    print('La edad de Juan es', edad)
```

Si el usuario ingresa 25, la salida será: La edad de Juan es 25.

## Nota Importante sobre la Operación de Asignación

La operación de asignación no es conmutativa, lo que significa que el orden de los elementos en la expresión es crucial. En Python, siempre debes escribir el nombre de la variable a la izquierda del signo igual (=) y la expresión que producirá el valor a la derecha. Aquí algunos ejemplos:

* digito = '2'
Asigna el carácter '2' a la variable digito.

* saludo = 'hola'
Asigna el texto 'hola' a la variable saludo.

* numero = 3 * 2
Asigna el resultado de multiplicar 3 por 2 a la variable numero.

* n = n + 0 - 2.15
Actualiza el valor de n sumando 0 y restando 2.15, asignando el resultado nuevamente a n (esto sobrescribe el valor anterior de n).

## Input y Output

Cuando usas la función input(), el usuario generalmente ve que el programa espera un dato, pero no siempre sabe qué información se espera. Para aclarar esto, colocamos un print() explicativo antes del input(). Otra opción es usar el argumento opcional de input() que permite mostrar un mensaje antes de esperar el ingreso del usuario.

Ejemplo:

```python
    edad = input('Ingrese la edad de Juan: ')
    print('La edad de Juan es', edad)
```

## Extensión del Programa

Supongamos que queremos extender el programa para preguntar la edad de cualquier persona, no solo de Juan.

```python
    print('¿Quién?')
    nombre = input()
    print()
    edad = input(f'Ingrese la edad de {nombre}: ')
    print(f'La edad de {nombre} es {edad}')
```

Ejecución:

```sh
    ¿Quién?
    Ana
    Ingrese la edad de Ana: 17
    La edad de Ana es 17
```

## Manipulación de Cadenas con Variables

Ejemplo de Programa para Calcular la Edad de un Hermano Mayor:

```python
    nomMen = input('¿Quién? ')
    edadMen = int(input(f'Ingresa la edad de {nomMen}: '))
    nomMay = input(f'¿Cómo se llama el hermano mayor de {nomMen}? ')
    diferen = int(input(f'¿Cuántos años más tiene {nomMay}? '))
    edadMay = edadMen + diferen

    print(f'{nomMen} tiene {edadMen} años')
    print(f'{nomMay} es mayor y tiene {edadMay} años')
```

Ejecución:

```sh

    ¿Quién? Ana
    Ingresa la edad de Ana: 17
    ¿Cómo se llama el hermano mayor de Ana? Luis
    ¿Cuántos años más tiene Luis? 3
    Ana tiene 17 años
    Luis es mayor y tiene 20 años
```

## Conversión de Datos

La función int() se usa para convertir el ingreso de texto en un número entero, permitiendo realizar operaciones aritméticas.

## Comentarios en el Código

En Python, se usan # para comentarios de una línea y triple comillas ''' o """ para comentarios multilínea.

Ejemplos de Comentarios:

```python
    print('Hola a todos')  # Saludo por pantalla

    ''' 
    Este es un comentario de varias líneas.
    Puede contener mucha información sobre el código.
    '''
```

## Funciones en Python

Las funciones permiten reutilizar código y mejorar la organización del programa. Una función en Python se define con def, seguida del nombre de la función y paréntesis () que pueden contener parámetros. El cuerpo de la función debe estar indentado y puede contener un return para devolver un valor.

Ejemplo de Función Simple:

```python
    def suma(a, b):
        return a + b

    resultado = suma(3, 5)
    print(resultado)  # Imprime: 8
```

## Programa que Realiza una Operación Aritmética

```python
    print('Cálculo de Operación')
    num1 = input('Num 1: ')
    num2 = input('Num 2: ')
    op = input('Operador (+ - * / // %): ')
    result = eval(num1 + op + num2)
    print(num1, op, num2, '=', result)
```

Este programa pide dos números y un operador, luego realiza la operación indicada y muestra el resultado.

## Nota sobre la Función eval()

La función eval() permite evaluar una expresión en forma de texto y obtener el resultado, siempre que el texto sea compatible con una expresión aritmética válida.

Ejemplo de Ejecución:

```python
    # Cálculo de Operación
    Num 1: 112
    Num 2: 33
    Operador (+ - * / // %): %
```

## Implementación con Funciones

Ahora, reescribiremos la versión anterior del programa utilizando funciones para encapsular la lógica de cálculo. Esto mejora la organización del código y lo hace más modular y reutilizable.

```python
    def calculo(n1, n2, op):
    return eval(n1 + op + n2)

    # Cálculo de operación aritmética binaria
    print('Cálculo de Operación')
    num1 = input('Num 1: ')
    num2 = input('Num 2: ')
    op = input('Operador (+ - * / // %): ')
    result = calculo(num1, num2, op)

    print(num1, op, num2, '=', result, sep='')
```

Esta versión del programa produce el mismo resultado que la versión anterior. Para el usuario, ambas versiones son indistinguibles en términos de resultado, pero internamente funcionan de manera diferente.

## Diferencias Internas

* Encapsulación del Cálculo: En la versión con funciones, el cálculo se encapsula dentro de la función calculo(), lo que permite separar la lógica del cálculo de la interacción con el usuario.
* Nombres de Argumentos: Los nombres de los argumentos en la invocación de la función y en su definición pueden ser los mismos o diferentes, lo importante es que se respete el orden en que se pasan los valores.
* Parámetros y Argumentos: Al invocar la función, se deben pasar valores que sean el resultado de evaluar una expresión válida, como una constante, el contenido de una variable, el resultado de otra función, o una operación. Por otro lado, en la definición de la función, los argumentos deben ser variables que representen los valores a recibir
