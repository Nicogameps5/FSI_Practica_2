# Práctica 2 – Fundamentos de los Sistemas Inteligentes

## Estrategias de Búsqueda:

## Introducción

Esta práctica parte del **código base proporcionado** para la asignatura *Fundamentos de los Sistemas Inteligentes*, el cual implementa algoritmos de búsqueda en grafos como BFS, DFS y Ramificación y Acotación aplicados al problema de navegación en el mapa de Rumanía (`GPSProblem`).

El objetivo de la práctica es ampliar dicho código para incorporar nuevas estrategias de búsqueda informada, manteniendo la funcionalidad original y respetando las interfaces existentes.

---

# Parte 1 – Ramificación y Acotación

## Descripción

En esta parte de la práctica se ha incorporado la estrategia de búsqueda **Ramificación y Acotación** al código base proporcionado.  

Para su implementación, no se ha modificado el algoritmo `graph_search`.
En su lugar, se ha creado una **cola de prioridad en el archivo `utils`**, que permite ordenar la lista abierta según un criterio de coste.
```python
import heapq
"""Cola de prioridad"""
class PriorityQueue:
    def __init__(self, f):
        self.f = f
        self.heap = []
        self.count = 0

    def append(self, item):
        heapq.heappush(self.heap, (self.f(item), self.count, item))
        self.count += 1

    def pop(self):
        return heapq.heappop(self.heap)[2]

    def extend(self, items):
        for item in items:
            self.append(item)

    def __len__(self):
        return len(self.heap)

```

---

## Implementación

La estrategia se implementa llamando directamente a `graph_search` y pasando como lista abierta una cola de prioridad que ordena los nodos por su coste acumulado (`path_cost`):

```python
def branch_and_bound_search(problem):
    return graph_search(
        problem,
        PriorityQueue(lambda node: node.path_cost)
    )
```

De esta forma, la diferencia entre BFS, DFS y Ramificación y Acotación se basa únicamente en el tipo de estructura utilizada para la lista abierta, manteniendo una implementación modular y reutilizable.

---

# Parte 2 – Ramificación y Acotación con Subestimación

## Descripción

En esta segunda parte se ha implementado una variante de Ramificación y Acotación que incorpora una **heurística subestimada**.

La heurística utilizada ya está incluida en el código base, dentro de la clase `GPSProblem`, y calcula la distancia euclídea en línea recta hasta el estado objetivo.  
Al ser una heurística admisible, se mantiene la garantía de optimalidad de la solución.

---

## Implementación

Al igual que en la versión anterior, no se modifica `graph_search`.  
La única diferencia consiste en cambiar el criterio de prioridad de la cola, utilizando ahora la función:

f(n) = g(n) + h(n)

La implementación es la siguiente:

```python
def branch_and_bound_with_underestimation(problem):
    return graph_search(
        problem,
        PriorityQueue(lambda node: node.path_cost + problem.h(node))
    )
```

Este enfoque permite reducir el número de nodos explorados, manteniendo siempre el coste total óptimo de la solución.

# Parte 3 – Contabilidad de nodos

### Implementación (cambios respecto al código base)

En esta última parte de la práctica se ha ampliado el algoritmo `graph_search` del código base para incorporar la **contabilidad de nodos generados y nodos visitados**, sin modificar el comportamiento lógico de la búsqueda.

A continuación se describen **únicamente los elementos añadidos o modificados** respecto a la versión original.

---

```python
generated = 0
visited = 0
```
Se introducen dos contadores:

- **`generated`**: contabiliza el número total de nodos generados durante la búsqueda.
- **`visited`**: contabiliza el número de nodos extraídos de la frontera y evaluados como posibles soluciones.

---

```python
fringe.append(Node(problem.initial))
generated += 1
```
Tras insertar el nodo inicial en la lista abierta, se incrementa el contador de nodos generados, ya que este nodo ha sido creado explícitamente.

---

```python
node = fringe.pop()
visited += 1
```
Cada vez que se extrae un nodo de la lista abierta, se incrementa el contador de nodos visitados.  
Esto refleja el número de nodos a los que se les comprueba si corresponden al estado objetivo.

---

```python
children = node.expand(problem)
generated += len(children)
```
Al expandir un nodo, se generan varios nodos hijos.  
El número de nodos generados se incrementa en función del número de sucesores creados.

---

```python
return node, generated, visited
```
La función devuelve ahora, además del nodo solución, los valores de **nodos generados** y **nodos visitados**, permitiendo analizar el rendimiento del algoritmo.

---

Esta incorporación permite **comparar de forma objetiva** el comportamiento de las distintas estrategias de búsqueda implementadas en la práctica, más allá del coste o la existencia de solución.



## Ejecución experimental

El archivo `run.py` ejecuta múltiples trayectos sobre el grafo de Rumanía y compara las siguientes estrategias:

- BFS  
- DFS  
- Ramificación y Acotación  
- Ramificación y Acotación con Subestimación  

Para cada caso se muestran:

- Ruta solución  
- Coste total  
- Nodos generados  
- Nodos visitados  
- Tiempo de ejecución  

---
Tabla con los resultados:

![Tabla final](Tabla final.jpg)

---
## Conclusiones

En los resultados se puede observar que, usando BFS y DFS, no siempre te devuelve el coste total óptimo. En cambio, usando
Ramificación y Acotación se observa que siempre devuelve el coste total óptimo, aunque teniendo que generar más nodos que los anteriores
algoritmos. Esto lo soluciona el algoritmo Ramificación y Acotación con subestimación haciendo uso de la heurística, generando
menor cantidad de nodos y encontrando el coste total óptimo.

Esto se consigue mediante el uso de colas de prioridad y heurísticas admisibles que reducen significativamente el espacio de búsqueda, manteniendo la optimalidad de las soluciones.

---

## Autores

- Nicolás Hernández Castro
- Adam Kardouchi Mhaifid
