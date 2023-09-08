# Considere el siguiente grafo (imagen: "Graph 01 - 03.png")
# e implemente el algoritmo de BFS para imprimir el recorrido 
# DESDE el nodo 4.

def bfs(graph, source):
  nodes = len(graph)
  visited = [False] * nodes

  # deque() -> from collections import deque
  queue = []

  # Inserto en la cola el nodo inicial y lo marco como visitado
  queue.append(source)
  visited[source] = True

  while len(queue):
    # 1er paso: Extraer el primer nodo de la cola
    node = queue.pop(0)

    # 2do paso: Procesar el nodo (haz lo que quieras con él)
    print(node)

    # Para cada nodo vecino del nodo actual, si no ha sido visitado
    # lo debo de agregar a la cola
    for neighbour in graph[node]:
      if not visited[neighbour]:
        queue.append(neighbour)
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

# Llamamos al BFS para que imprima el recorrido
bfs(graph, 4)