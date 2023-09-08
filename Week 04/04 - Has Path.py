# Considere el siguiente grafo (imagen: "Graph 04.png")
# e implemente una función que determine si existe un camino
# desde un nodo A hasta un nodo B

# Podemos usar BFS o DFS
def has_path(graph, source, destination):
  nodes = len(graph)
  visited = [False] * nodes

  queue = []
  # Agrego a la cola el 1er nodo (source)
  queue.append(source)
  visited[source] = True

  while len(queue):
    # Extraer el primer nodo de la cola
    node = queue.pop(0)

    # Procesar el nodo (haz lo que quiera con él)
    if node == destination:
      return True
    
    # Agrego a la cola los nodos vecinos sin visitar del nodo actual
    for neighbour in graph[node]:
      if not visited[neighbour]:
        queue.append(neighbour)
        visited[neighbour] = True

  return False

# Interpretación:
#   graph[i]: Vecinos del nodo i
#   ej.
#       graph[0]: Los vecinos del nodo 0 son 2, 4 y 5

graph = [
  [2, 4, 5],
  [4, 5],
  [3, 4],
  [],
  [5],
  [],
  [5],
  [4],
]

# Llamamos al DFS para que imprima el recorrido
test_cases = [(0, 7), (7, 5), (2, 5), (5, 2)]
for node_a, node_b in test_cases:
  result = "YES" if has_path(graph, node_a, node_b) else "NO"
  print(f"SOURCE: {node_a} - DESTINATION: {node_b} -> PATH: { result }")