# Ciclos

## 1.1 Introducción

Imagina que en una fábrica se requiere un procedimiento para entrenar al personal nuevo. Se describe un procedimiento simple para la descarga de 3 cajas de material desde un camión:

1. Abrir la puerta del depósito y encender luces.
2. Ir al garage donde está el camión.
3. Abrir las puertas traseras del camión.
4. Tomar una caja con ambas manos, asegurándola.
5. Caminar con la caja hasta el depósito.
6. Colocar la caja en el sector correspondiente.
7. Repetir el proceso para las siguientes cajas.
8. Apagar luces y cerrar la puerta del depósito.
9. Cerrar y trabar las puertas del camión.
10. Avisar al transportista el fin de la descarga.

Este procedimiento es específico para 3 cajas, pero si varía la cantidad de cajas, el procedimiento se vuelve más complejo y repetitivo.

Para hacer el procedimiento más general:

1. Abrir la puerta del depósito y encender luces.
2. Ir al garage donde está el camión.
3. Abrir las puertas traseras del camión.
4. Tomar una caja, asegurándola.
5. Caminar con la caja hasta el depósito.
6. Colocar la caja en su lugar.
7. Repetir el proceso mientras queden cajas.
8. Cerrar y trabar las puertas del camión.
9. Avisar al transportista el fin de la descarga.
10. Apagar luces y cerrar la puerta del depósito.

Este enfoque es más compacto y cubre todas las posibles cantidades de cajas en un envío.

Los algoritmos escritos hasta ahora se parecen más al primer procedimiento, por lo que se introduce una nueva herramienta para escribir pasos repetidos de manera compacta: **ciclos**, **bucles** o **sentencias iterativas**. Estas permiten repetir automáticamente un conjunto de instrucciones.

## 2. ¿Qué es un Ciclo?

Un ciclo es una estructura de control iterativa que permite ejecutar repetidamente un conjunto de instrucciones. Es una herramienta útil cuando necesitamos que una parte del código se ejecute múltiples veces. Los ciclos permiten escribir programas de manera más compacta y eficiente.

### 2.1. Definiciones

1. **Cuerpo**: Es la parte del ciclo que se ejecuta repetidamente.
2. **Condición o Invariante**: Determina si el cuerpo del ciclo se ejecutará nuevamente o si se debe salir del ciclo.
3. **Estado Previo**: Valores de las variables antes de que el ciclo comience.
4. **Paso**: Cambio de valor en alguna de las variables de la condición.

### 2.2. ¿Cómo funciona un Ciclo?

Cuando el flujo de control del programa llega a un ciclo, primero se evalúa la condición. Si es verdadera, se ejecuta el cuerpo del ciclo. Una vez terminado, el flujo vuelve a la condición para evaluarla nuevamente. Este proceso se repite hasta que la condición sea falsa, momento en el cual se sale del ciclo.

## 3. While

El `while` es una estructura de ciclo que permite ejecutar el cuerpo del ciclo mientras la condición sea verdadera. La sintaxis básica en Python es:

```python
while condición:
    instrucción 1
    instrucción 2
```

Importante: Asegúrate de usar indentación adecuada con la tecla TAB para que Python pueda distinguir el cuerpo del ciclo del resto del código.

### Ejemplo de while

Para contar cuántos múltiplos de 3 hay entre 5 números ingresados por el usuario, puedes usar el siguiente código:

```python
print('Ingresá 5 números enteros')
total_mult = 0
veces = 0
while veces < 5:
    num = int(input('Número: '))
    if num % 3 == 0:
        total_mult += 1
    veces += 1
print('Vinieron:', total_mult, 'múltiplos de 3')
```

## 2.2. Break y Continue

### 2.2.1. break

La instrucción break sale inmediatamente del ciclo y continúa con la ejecución de las instrucciones siguientes al ciclo.

Ejemplo:

```python
numero = 10
while numero > 0:
    if numero % 3 == 0:
        print("El primer número divisible por 3 es:", numero)
        break
    numero += 1
```

### 2.2.2. continue

La instrucción continue salta a la siguiente iteración del ciclo, omitiendo el resto del código en el bloque para esa iteración.

Ejemplo:

```python
numero = 1
while numero <= 10:
    if numero % 2 == 0:
        numero += 1
        continue
    print(numero)
    numero += 1
```

En ambos casos, break y continue alteran el flujo del ciclo, evitando que se ejecute el código subsecuente en la iteración actual.

## 2.3. Consideraciones del `while`

Es crucial evitar redundancias en el código y no hacer preguntas innecesarias.

### Ejemplo de redundancia

Si la condición del `while` es `numero < 3`, el bucle continuará ejecutándose hasta que `numero` llegue a 3. Una vez que `numero` es igual a 3, el `while` termina automáticamente. Por lo tanto, si ya sabemos que la condición del `while` hará que el código termine cuando `numero` sea 3, no es necesario usar un `if` adicional para verificar esto después del `while`.

Además, el uso de `continue` es redundante en este contexto, ya que al llegar a la última línea del bucle `while`, el ciclo simplemente vuelve a empezar. El `continue` se utiliza cuando queremos forzar el salto al siguiente ciclo.

### Ejemplo de código simplificado

```python
while numero < 3:
    # Código que se ejecuta mientras numero < 3
    numero += 1
# Código que se ejecuta después del while, si numero es 3
```

## 3. for

El bucle for en Python itera sobre un iterable, automatizando el manejo del estado previo y del paso.

Sintaxis

```python
for var in iterable:
    instrucción 1
    instrucción 2
    ...
```

Un iterable es una estructura que se puede recorrer, como una lista o un rango.

### Ejecución del for

El for asigna el primer valor del iterable a la variable de control (var) y ejecuta el cuerpo del bucle. Luego, asigna el siguiente valor y repite el proceso hasta que no haya más valores en el iterable.

Ejemplos de uso de rangos

```python
range(1, 10)  # 1, 2, 3, 4, 5, 6, 7, 8, 9
range(6)     # 0, 1, 2, 3, 4, 5
range(0, 8, 2)  # 0, 2, 4, 6
range(15, 10, -5)  # 15
range(15, 10, -1)  # 15, 14, 13, 12, 11
```

Ejemplo de uso de for con listas

```python
numeros = [11, 24, 32, 4, 15, 6, 17, 38, 94, 110]
for numero in numeros:
    print(numero)
```

### 3.3. break y continue

Ambos funcionan de manera similar en ciclos while y for.

Ejemplo de break

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    if numero % 7 == 0:
        print("El primer número divisible por 7 es:", numero)
        break
```

Ejemplo de continue

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    if numero % 2 == 0:
        continue
    print(numero)
```

## 1. Ciclos Anidados

Los ciclos pueden estar anidados, es decir, un ciclo dentro de otro. El ciclo interno se completa antes de que el ciclo externo continúe.

Ejemplo de conteo de divisores

```python

num = int(input('Ingresá un número entero positivo: '))
while num <= 0:
    num = int(input('Ingresá un número entero positivo: '))
cant_divisores = 0
for d in range(2, num // 2 + 1):
    if num % d == 0:
        cant_divisores += 1
print(num, 'tiene', cant_divisores, 'divisores')
```

Ejemplo con múltiples bucles

```python
print('Ingresá 10 números y te contamos cuántos divisores tiene cada uno')
for n in range(10):
    num = int(input('Ingresá un número entero positivo: '))
    while num <= 0:
        num = int(input('Ingresá un número entero positivo: '))
    cant_divisores = 0
    for d in range(2, num // 2 + 1):
        if num % d == 0:
            cant_divisores += 1
    print(num, 'tiene', cant_divisores, 'divisores')
```