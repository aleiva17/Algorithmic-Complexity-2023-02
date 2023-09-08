# Considere el siguiente grafo (imagen: "Graph 05 - 06.png")
# e implemente una función que cuente la cantidad de
# componentes que existe en el grafo

# Podemos usar DFS o BFS
def count_components(graph):
  nodes = len(graph)
  visited = [False] * nodes
  count = 0

  def dfs(node):
    visited[node] = True

    for neighbour in graph[node]:
      if not visited[neighbour]:
        dfs(neighbour)


  for node in range(1, nodes):
    if not visited[node]:
      count += 1
      dfs(node)

  return count


# Interpretación:
#   graph[i]: Vecinos del nodo i
#   ej.
#       graph[1]: El vecino del nodo 1 es 2

graph = [
  [],
  [2],
  [1, 9],
  [4, 5, 7, 8],
  [3],
  [3],
  [],
  [3],
  [3],
  [2]
]

print(f"En el grafo existen {count_components(graph)} componentes")