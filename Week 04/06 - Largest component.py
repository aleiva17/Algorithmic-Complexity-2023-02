# Considere el siguiente grafo (imagen: "Graph 05 - 06.png")
# e implemente una función que retorn el mayor tamaño de
# todos los componentes

def get_max_component_size(graph):
  nodes = len(graph)
  visited = [False] * nodes
  ans = 0

  def dfs(node):
    visited[node] = True
    size = 1

    for neighbour in graph[node]:
      if not visited[neighbour]:
        size += dfs(neighbour)

    return size
  

  for node in range(1, nodes):
    if not visited[node]:
      current_component_size = dfs(node)
      ans = max(ans, current_component_size)
  
  return ans


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

print(f"El componente de mayor tamaño tiene {get_max_component_size(graph)} nodos.")