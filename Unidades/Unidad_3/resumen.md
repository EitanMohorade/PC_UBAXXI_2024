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

# Sentencias Condicionales

Los programas deben adaptarse a distintos casos o patrones de entrada y aplicar tratamientos diferenciados según la situación. Para lograr esto, los programas necesitan identificar casos específicos y tomar decisiones basadas en esos casos.

**Esencialmente:**

- **Identificación**: Reconocer los casos o patrones que pueden surgir.
- **Decisión**: Elegir el camino adecuado para cada caso.

No podemos realizar tratamientos diferenciados si no somos capaces de reconocer las diferencias entre los casos. Por lo tanto, necesitamos programas que no solo transformen datos y obtengan resultados, sino que también decidan cómo tratar cada situación específica utilizando flujos de control alternativos.

## 1.1 Introducción a Lógica

La lógica bivalente o lógica simbólica es útil para formular preguntas y tomar decisiones en programación. Todos los lenguajes de programación, como Python, utilizan expresiones y operadores lógicos para estos fines.

### Expresiones Booleanas

En lógica, una **proposición** o **expresión lógica** puede evaluarse como Verdadera o Falsa. En programación, estas se llaman expresiones booleanas. Ejemplos de expresiones booleanas incluyen:

- "Hoy llueve"
- "Estoy en Sudamérica"
- "Las zanahorias son celestes"
- "4 es un número par"

Cada una de estas expresiones puede ser evaluada como Verdadera o Falsa, dependiendo del contexto. En programación, todas las preguntas y decisiones deben formularse como expresiones booleanas, es decir, condiciones que resultan en un valor de verdad.

### Operadores Lógicos

Para construir condiciones, se utilizan operadores lógicos que operan sobre expresiones booleanas. Los operadores lógicos más comunes son:

- **Negación ( ~ )**: Invierte el valor de verdad de una expresión. En Python, se usa `not`.
  - Ejemplo: `not True` resulta en `False`.

- **Conjunción ( ^ )**: También conocido como "y". La condición completa es Verdadera solo si todas las expresiones evaluadas son verdaderas. En Python, se usa `and`.
  - Ejemplo: `True and False` resulta en `False`.

- **Disyunción ( v )**: También conocido como "o". La condición completa es Verdadera si al menos una de las expresiones evaluadas es verdadera. En Python, se usa `or`.
  - Ejemplo: `True or False` resulta en `True`.

Cada operador lógico tiene una **Tabla de Verdad** que muestra los resultados posibles al combinar diferentes valores de verdad.

## Nota sobre Expresiones Lógicas

Las expresiones lógicas complejas (que incluyen más de un operador) se resuelven respetando precedencias y de izquierda a derecha. Se pueden usar paréntesis `()` para alterar las precedencias. Sin embargo, si no se usan paréntesis, los operadores `AND` tienen mayor precedencia que los operadores `OR` en Python.

**Ejemplos:**

- `V or F and F` se resuelve como `V or (F and F)` = `V or F` = `V` (precedencia de `AND` sobre `OR`).
- `V or F or F` se resuelve como `(V or F) or F` = `V or F` = `V`.
- `V and V and F` se resuelve como `(V and V) and F` = `V and F` = `F`.

Con paréntesis alterando las precedencias, podemos obtener resultados diferentes:

- `(V or F) and F` = `V and F` = `F` (sin paréntesis, el resultado era `V`).
- `V or (F or F)` = `V or F` = `V` (no cambia).
- `V and (V and F)` = `V and F` = `F` (no cambia).

**Conclusión:**

- El operador lógico `OR` (or) es asociativo. Esto significa que la evaluación se realiza de izquierda a derecha y se detiene tan pronto como se encuentra un valor `True`. Si ninguno de los valores es `True`, el resultado es `False`.
- El operador lógico `AND` (and) también es asociativo. La evaluación se realiza de izquierda a derecha y se detiene tan pronto como se encuentra un valor `False`. Si todos los valores son `True`, el resultado es `True`.

En expresiones combinadas, en Python `AND` tiene precedencia sobre `OR`. La expresión se evalúa de izquierda a derecha respetando estas precedencias.

## 1.2. Sentencia `if`

En los lenguajes de programación procedural, las sentencias condicionales permiten alterar el flujo de control de un programa. En Python, la sentencia `if` es una herramienta común para tomar decisiones y bifurcar el flujo de control.

### Sintaxis de `if` en Python

```python
if condición1:
    instrucción1
    instrucción2
elif condición2:
    instrucciónA
    instrucciónB
else:
    instrucciónX
    instrucciónY
```

- elif es una combinación de else y if, y se usa para evaluar una nueva condición si la condición del if inicial no se cumple.
- El cuerpo de cada sentencia if, elif, o else debe estar indentado de manera consistente. La indentación es crucial en Python para definir qué instrucciones pertenecen a cada bloque.

Traducción coloquial:

"Si la condición 1 es Verdadera, ejecuta las instrucciones 1 y 2. Si la condición 2 es Verdadera, ejecuta las instrucciones A y B. Si ninguna de las condiciones anteriores es Verdadera, ejecuta las instrucciones X e Y."

Notas:

- Los elementos entre corchetes [ ] son opcionales.
- Python ignora los elif y else si el if previo ya ha ejecutado su bloque de código. El flujo de control continúa después del if.

## 1.3. Operadores en Python

Además de los operadores aritméticos, Python incluye operadores de comparación, pertenencia y lógicos.

### 1.3.1. Operadores de Comparación

| Símbolo | Definición             | Ejemplo           | Comentario                                           |
|---------|------------------------|-------------------|-----------------------------------------------------|
| `==`    | igual a                | `4 == 4`          | La expresión va a valer True si ‘a’ vale 4         |
| `!=`    | distinto               | `b != 4`          | La expresión va a valer True si ‘b’ NO vale 4      |
| `<`     | menor                  | `2 < 4`           | Devuelve True                                       |
|         |                        | `3 < 1`           | Devuelve False                                      |
| `<=`    | menor o igual          | `2 <= 4`          | Devuelve True                                       |
|         |                        | `3 <= 1`          | Devuelve False                                      |
|         |                        | `3 <= 3`          | Devuelve True                                       |
| `>`     | mayor                  | `2 > 4`           | Devuelve False                                      |
|         |                        | `3 > 1`           | Devuelve True                                       |
| `>=`    | mayor o igual          | `2 >= 4`          | Devuelve False                                      |
|         |                        | `3 >= 1`          | Devuelve True                                       |
|         |                        | `3 >= 3`          | Devuelve True                                       |

### Operadores de Pertenencia

| Símbolo  | Definición | Ejemplo                          | Comentario                                           |
|----------|------------|----------------------------------|-----------------------------------------------------|
| `in`     | Pertenece  | `"razón" in "corazón"`           | Devuelve True                                       |
|          |            | `"tazón" in "corazón"`            | Devuelve False                                      |
| `not in` | NO pertenece| `"razón" not in "corazón"`       | Devuelve False                                      |
|          |            | `"tazón" not in "corazón"`        | Devuelve True                                       |

1.4. Ejemplo de Aplicación
Para calcular el pago a un trabajador considerando horas trabajadas, valor de la hora y otros factores:

```python
# Ejemplo de cálculo de pago por horas
cant_horas = int(input('Ingrese la cantidad de horas trabajadas: '))
valor_hora = float(input('Ingrese valor de la hora de trabajo: '))
hijos = input('Tiene hijos? (si/no): ')
total = cant_horas * valor_hora

if hijos == 'si':
    plus_fijo = float(input('Ingrese adicional guardería: '))
    total = total + plus_fijo
else:
    if cant_horas >= 30:
        total = total * 1.1

print('Debe cobrar', total)
```

Casos de prueba:

- No tiene hijos y no trabaja 30 horas o más: Calcula cant_horas * valor_hora.
- No tiene hijos y trabaja 30 horas o más: Calcula cant_horas * valor_hora * 1.1.
- Tiene hijos y no trabaja 30 horas o más: Calcula cant_horas * valor_hora + plus_fijo.
Tiene hijos y trabaja 30 horas o más: Calcula cant_horas* - valor_hora + plus_fijo.
Ejemplo de Código:

```python
if clima_hoy == "lluvia":
    llevar_paraguas()
    llevar_campera()

if nivel_sueño == "mucho":
    apagar_alarma()
    seguir_durmiendo()
else:
    apagar_alarma()
    levantarse()

if necesidad == "hambre":
    comer_algo()
elif necesidad == "sed":
    tomar_agua()
else:
    relajarme_en_el_sillon()

if clima == "lluvia":
    if transporte == "colectivo":
        llevar_paraguas()
    elif transporte == "auto":
        llevar_llaves()
    salir_de_casa()
```

Estos ejemplos muestran cómo se utilizan las sentencias if, elif, y else para tomar decisiones y controlar el flujo del programa.
