def dfs(node, destination, graph, visited):
  visited[node] = True
  state = False

  if node == destination:
    state = True

  for neighbour in graph[node]:
    if not visited[neighbour]:
      state = state or dfs(neighbour, destination, graph, visited)
  
  return state


nodes = int(input("Ingrese la cantidad de nodos del grafo: "))
edges = int(input("Ingrese la cantidad de aristas a registrar: "))

graph = [[] for _ in range(nodes)]

for i in range(edges):
  a, b = map(int, input("Ingrese la conexión de nodos: ").split())
  graph[a].append(b)
  graph[b].append(a)

source = int(input("Ingrese el nodo de origen: "))
destination = int(input("Ingrese el nodo de destino: "))

visited = [False] * len(graph)

found = dfs(source, destination, graph, visited)
print(found)