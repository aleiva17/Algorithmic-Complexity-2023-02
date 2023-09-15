from random import shuffle

def rdfs(node, graph, visited):
  # Marcar como visitado
  visited[node] = True
  
  # Procesar el nodo actual
  print(f"{node}", end=" -> ")

  # Visito todos los vecinos que no han sido visitados
  # DE MANERA ALEATORIA
  shuffle(graph[node])

  for neighbour in graph[node]:
    if not visited[neighbour]:
      rdfs(neighbour, graph, visited)


for _ in range(3):
  with open("input.txt", "r") as file:
    nodes = int(file.readline().rstrip())
    edges = int(file.readline().rstrip())

    graph = [[] for _ in range(nodes + 1)]
    visited = [False] * (nodes + 1)

    for _ in range(edges):
      a, b = map(int, file.readline().rstrip().split())
      graph[a].append(b)
      graph[b].append(a)

    source = int(file.readline().rstrip())
    rdfs(source, graph, visited)

  print()