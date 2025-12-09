# Search methods

import search
import time

casos = [('A', 'B'), ('O', 'E'), ('G', 'Z'), ('N', 'D'), ('M', 'F')]

def ejecutar(inicio, fin):
    print(f"\n==============================")
    print(f"   Inicio: {inicio}  →  Fin: {fin}")
    print(f"==============================")

    problema = search.GPSProblem(inicio, fin, search.romania)

    # BFS
    inicio_t = time.perf_counter()
    solucion_bfs, generados_bfs, visitados_bfs = search.breadth_first_graph_search(problema)
    fin_t = time.perf_counter()

    print("BFS nodos generados:", generados_bfs)
    print("BFS nodos visitados:", visitados_bfs)
    print("BFS path: ", solucion_bfs.path())
    print("BFS coste total: ", solucion_bfs.path_cost)
    print(f"BFS tiempo de ejecución: {fin_t - inicio_t:.6f} segundos")

    print()

    # DFS
    inicio_t = time.perf_counter()
    solucion_dfs, generados_dfs, visitados_dfs = search.depth_first_graph_search(problema)
    fin_t = time.perf_counter()

    print("DFS nodos generados:", generados_dfs)
    print("DFS nodos visitados:", visitados_dfs)
    print("DFS path:", solucion_dfs.path())
    print("DFS coste total: ", solucion_dfs.path_cost)
    print(f"DFS tiempo de ejecución: {fin_t - inicio_t:.6f} segundos")

    print()

    # Ramificación y acotación
    inicio_t = time.perf_counter()
    solucion_bnb, generados_bnb, visitados_bnb = search.branch_and_bound_search(problema)
    fin_t = time.perf_counter()

    print("Branch&Bound nodos generados:", generados_bnb)
    print("Branch&Bound nodos visitados:", visitados_bnb)
    print("Branch&Bound path:", solucion_bnb.path())
    print("Branch&Bound coste total:", solucion_bnb.path_cost)
    print(f"Branch&Bound tiempo de ejecución: {fin_t - inicio_t:.6f} segundos")

    print()

    # Ramificación y acotación con subestimación
    inicio_t = time.perf_counter()
    solucion_bnbu, generados_bnbu, visitados_bnbu = search.branch_and_bound_with_underestimation(problema)
    fin_t = time.perf_counter()

    print("Branch&Bound con subestimación nodos generados:", generados_bnbu)
    print("Branch&Bound con subestimación nodos visitados:", visitados_bnbu)
    print("Branch&Bound con subestimación path:", solucion_bnbu.path())
    print("Branch&Bound con subestimación coste total:", solucion_bnbu.path_cost)
    print(f"Branch&Bound con subestimación tiempo de ejecución: {fin_t - inicio_t:.6f} segundos")


for inicio, fin in casos:
    ejecutar(inicio, fin)

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
