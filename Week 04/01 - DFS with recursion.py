# Considere el siguiente grafo (imagen: "Graph 01 - 03.png")
# e implemente el algoritmo de DFS con RECURSIÓN para imprimir
# el recorrido DESDE el nodo 4.

def dfs(graph, source):
  nodes = len(graph)
  visited = [False] * nodes

  def recursion(node):
    # 1er paso: Marcar como visitado
    visited[node] = True

    # Procesar el nodo (haz la operación que quieras)
    print(node)

    # Llamo a que la recursión visite los vecinos NO visitados
    for neighbour in graph[node]:
      if not visited[neighbour]:
        recursion(neighbour)


  recursion(source)
  


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