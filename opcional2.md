# Parte 2 - Opcional: Ejemplo de Heurística que Sobreestima

## ¿Qué es una heurística que sobreestima?

Una heurística **admisible** nunca sobreestima el coste real para llegar a la meta: h(n) ≤ coste_real

Una heurística que **sobreestima** da valores mayores que el coste real: h(n) > coste_real

Cuando la heurística sobreestima, el algoritmo A* pierde la garantía de encontrar el camino óptimo.

---

## Ejemplo donde FALLA

### Grafo:

```
        5          1
    A -----> B -------> D (META)
    |                  ^
    |1                 |
    |                  |10
    +------> C --------+
```

**Aristas:**
- A → B: coste 5
- B → D: coste 1
- A → C: coste 1
- C → D: coste 10

**Caminos posibles:**
- A → B → D = 5 + 1 = **6** (ÓPTIMO)
- A → C → D = 1 + 10 = **11**

---

### Heurística que sobreestima:

| Nodo | h(n) | Coste real a D |
|------|------|----------------|
| A    | 8    | 6              |
| B    | 50   | 1              |
| C    | 9    | 10             |
| D    | 0    | 0              |

La heurística sobreestima especialmente en B: dice que faltan 50 cuando realmente solo falta 1.

---

### Ejecución manual (A* con esta heurística):

**Recordatorio:** f(n) = g(n) + h(n)

| Iteración | Nodo Actual | Lista Abierta (ordenada por f) | Acción |
|-----------|-------------|--------------------------------|--------|
| 0 | - | A(g=0, h=8, f=8) | Inicio |
| 1 | A | B(g=5, h=50, f=**55**)<br>C(g=1, h=9, f=**10**) | Se expande A |
| 2 | C | D(g=11, h=0, f=**11**)<br>B(g=5, h=50, f=**55**) | Se elige C porque f=10 es menor |
| 3 | D | B(g=5, h=50, f=55) | **META ENCONTRADA** |

**Solución:** A → C → D con **coste total = 11**

---

## ¿Qué ha pasado?

El algoritmo encontró el camino A → C → D con coste 11, pero **el óptimo era A → B → D con coste 6**.

**El problema:** El nodo B nunca se expandió porque su f = 55 lo hacía parecer malísimo. La heurística h(B) = 50 sobreestimaba tanto que el algoritmo lo descartó, cuando en realidad B llevaba al mejor camino.

---

## Conclusión

Cuando una heurística **sobreestima**, puede hacer que el algoritmo:
- Descarte nodos buenos pensando que son malos
- Encuentre soluciones **subóptimas**
- No explore caminos que realmente son mejores

Por eso es fundamental usar **heurísticas admisibles** (que no sobreestimen) si queremos garantizar encontrar el camino óptimo con A*.