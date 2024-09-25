# Diccionarios

Las listas permiten acceder a elementos por posición, lo que puede ser ineficiente si se desconoce la ubicación del dato. En estos casos, se recurre a métodos de búsqueda secuencial.

Para acelerar este proceso, Python provee **diccionarios** (tipo `dict`), estructuras de datos hashables que mapean **claves** a valores. En lugar de buscar por posición, se accede directamente al valor mediante su clave. Esta estructura optimiza la búsqueda, manteniendo tiempos de acceso constantes, independientemente del tamaño del diccionario.

Un diccionario en Python se representa como una colección de pares `clave: valor` entre llaves `{}`.

## Ejemplos

```python
    a = {1: 1, 2: 4, 3: 6, 4: 8, 5: 10}
    b = {}
    c = {'ana': 27, 'juan': 15, 'elena': 1}
    d = {345: ('clavos', 1), 346: ('tuercas', 1), 202: ('manguera', 2)}

    print(a[3])      # 6
    print(c['elena']) # 1
    print(d[202])     # ('manguera', 2)
```

## Métodos de Diccionarios en Python

- `d.clear()` → Elimina todos los elementos de `d`.
- `d.pop(clave)` → Remueve el par clave/valor y devuelve el valor. Da error si la clave no existe.
- `d.popitem()` → Remueve y devuelve un par clave/valor aleatorio. Da error si el diccionario está vacío.
- `d.copy()` → Devuelve una copia de `d` en otra región de memoria.
- `d.fromkeys(secuencia)` → Crea un diccionario usando una secuencia de claves.
- `d.get(clave)` → Devuelve el valor asociado a la clave, o `None` si la clave no existe.
- `d.items()` → Devuelve una lista de tuplas, cada una con clave (índice 0) y valor (índice 1).
- `d.keys()` → Devuelve una lista con las claves de `d`.
- `d.update(b)` → Agrega o actualiza los pares clave/valor de `b` en `d`.

Los diccionarios son útiles para almacenar y acceder a información de manera eficiente, como listas de productos o estudiantes. El siguiente ejemplo muestra cómo se puede usar un diccionario para gestionar productos de una tienda:

```python
    Copy code
    productos = {}
    cgo = int(input('Ingrese código, 0 para terminar '))

    while cgo != 0:
        if cgo not in productos:
            desc = input(f'Descripción de {cgo} ')
            unidad = input(f'Unidad de Medida de {desc} ')
            precio = float(input(f'Precio unitario de {desc} '))
            productos[cgo] = (desc, unidad, precio)
        cgo = int(input('Ingrese código, 0 para terminar '))

    for cgo in productos:
        print(cgo, *productos[cgo])

    total = 0
    cgo = int(input('Qué lleva? 0 para salir '))
    while cgo != 0:
        cant = float(input(f'Cantidad de {productos[cgo][0]} '))
        total += cant * productos[cgo][2]
        cgo = int(input('Qué lleva? 0 para salir '))

    print(f'Debe abonar: ${total:.2f}')
```

### Características

- **Claves**: Deben ser inmutables (números, strings, tuplas, etc.).
- **Valores**: Pueden ser de cualquier tipo (incluyendo listas o diccionarios).
- **Acceso**: Es directo mediante la clave.
- **Mutabilidad**: Los diccionarios son mutables; se pueden agregar o eliminar elementos.
