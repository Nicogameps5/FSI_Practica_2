# Ejercicio Manual: Ramificación y Acotación en Rumanía

## Enunciado
Realizar búsqueda manual desde **Arad** hasta **Bucharest** usando **Ramificación y Acotación**.

---

## Mapa de Rumanía (Conexiones del código)

```
Arad (A)           → Zerind: 75,  Sibiu: 140,  Timisoara: 118
Bucharest (B)      → Urziceni: 85, Pitesti: 101, Giurgiu: 90, Fagaras: 211
Craiova (C)        → Drobeta: 120, Rimnicu Vilcea: 146, Pitesti: 138
Fagaras (F)        → Sibiu: 99, Bucharest: 211
Lugoj (L)          → Timisoara: 111, Mehadia: 70
Oradea (O)         → Zerind: 71, Sibiu: 151
Pitesti (P)        → Rimnicu Vilcea: 97, Bucharest: 101, Craiova: 138
Rimnicu Vilcea (R) → Sibiu: 80, Pitesti: 97, Craiova: 146
Sibiu (S)          → Arad: 140, Fagaras: 99, Oradea: 151, Rimnicu Vilcea: 80
Timisoara (T)      → Arad: 118, Lugoj: 111
Zerind (Z)         → Arad: 75, Oradea: 71
```

---

## ¿Cómo funciona Ramificación y Acotación?

**Regla simple:** Siempre expando el nodo que tenga el **coste más bajo** desde el origen.

---

## ITERACIÓN 1

**Expando:** Arad (coste: 0)

**Genero:**
- Zerind con coste 75
- Timisoara con coste 118  
- Sibiu con coste 140

**Lista ABIERTA (ordenada por coste):**
1. Zerind (75)
2. Timisoara (118)
3. Sibiu (140)

**Lista CERRADA:** {Arad}

---

## ITERACIÓN 2

**Expando:** Zerind (coste: 75) ← El de menor coste

**Genero desde Zerind:**
- Oradea con coste 75+71 = 146
- Arad ya visitado, lo descarto

**Lista ordenada por coste:**
1. Timisoara (118)
2. Sibiu (140)
3. Oradea (146)

**Visitados:** {Arad, Zerind}

---

## ITERACIÓN 3

**Expando:** Timisoara (coste: 118) ← El de menor coste

**Genero desde Timisoara:**
- Lugoj con coste 118+111 = 229
- Arad ya visitado, lo descarto

**Lista ordenada por coste:**
1. Sibiu (140)
2. Oradea (146)
3. Lugoj (229)

**Visitados:** {Arad, Zerind, Timisoara}

---

## ITERACIÓN 4

**Expando:** Sibiu (coste: 140) ← El de menor coste

**Genero desde Sibiu:**
- Fagaras con coste 140+99 = 239
- Rimnicu Vilcea con coste 140+80 = 220
- Oradea con coste 140+151 = 291 (ya existe con 146, mantengo el mejor)
- Arad ya visitado, lo descarto

**Lista ordenada por coste:**
1. Oradea (146)
2. Rimnicu Vilcea (220)
3. Lugoj (229)
4. Fagaras (239)

**Visitados:** {Arad, Zerind, Timisoara, Sibiu}

---

## ITERACIÓN 5

**Expando:** Oradea (coste: 146) ← El de menor coste

**Genero desde Oradea:**
- Zerind ya visitado, lo descarto
- Sibiu ya visitado, lo descarto

**Lista ordenada por coste:**
1. Rimnicu Vilcea (220)
2. Lugoj (229)
3. Fagaras (239)

**Visitados:** {Arad, Zerind, Timisoara, Sibiu, Oradea}

---

## Resultado

**Nodos visitados:** Arad, Zerind, Timisoara, Sibiu, Oradea

**Siguiente nodo a expandir:** Rimnicu Vilcea (coste 220)

**Estado:** Todavía no hemos llegado a Bucharest. Para encontrar la solución habría que continuar expandiendo nodos en orden de coste.