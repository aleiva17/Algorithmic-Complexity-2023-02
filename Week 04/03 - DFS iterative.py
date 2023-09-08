# Considere el siguiente grafo (imagen: "Graph 01 - 03.png")
# e implemente el algoritmo de DFS ITERATIVO para imprimir
# el recorrido DESDE el nodo 4.

def dfs(graph, source):
  nodes = len(graph)
  visited = [False] * nodes

  # deque() -> from collections import deque
  stack = []

  # Inserto en el stack el nodo inicial y lo marco como visitado
  stack.append(source)
  visited[source] = True

  while len(stack):
    # 1er paso: Extraer el primer nodo del stack
    node = stack.pop()

    # 2do paso: Procesar el nodo (haz lo que quieras con él)
    print(node)

    # Para cada nodo vecino del nodo actual, si no ha sido visitado
    # lo debo de agregar al stack
    for neighbour in graph[node]:
      if not visited[neighbour]:
        stack.append(neighbour)
        visited[neighbour] = True


# Interpretación:
#   graph[i]: Vecinos del nodo i
#   ej.
#       graph[0]: Los vecinos del nodo 0 son 2, 4 y 5

graph = [
  [2, 4, 5],
  [4, 5],
  [0, 3, 4],
  [2],
  [0, 1, 2, 5, 7],
  [0, 1, 4, 6],
  [5],
  [4],
]

# Llamamos al DFS para que imprima el recorrido
dfs(graph, 4)