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

Estos ejemplos muestran cómo se utilizan las sentencias if, elif, y else para tomar decisiones y controlar el flujo del programa