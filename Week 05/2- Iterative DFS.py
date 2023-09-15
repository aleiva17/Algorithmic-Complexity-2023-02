def has_path(source, destination, graph):
  stack = [source] # deque() -> from collections import deque
  visited = [False] * len(graph)

  while len(stack):
    # Extraigo el nodo del stack
    node = stack.pop()
    
    # Proceso el nodo
    print(node)
    if node == destination:
      return True
    
    # Por cada vecino del nodo actual, lo visito si no ha sido visitado
    for neighbour in graph[node]:
      if not visited[neighbour]:
        visited[neighbour] = True
        stack.append(neighbour)

  return False


with open("input.txt", "r") as file:
  nodes = int(file.readline().rstrip())
  edges = int(file.readline().rstrip())

  graph = [[] for _ in range(nodes)]

  for _ in range(edges):
    line = file.readline().rstrip()
    a, b = map(int, line.split())

    graph[a].append(b)
    graph[b].append(a)
  
  source = int(file.readline().rstrip())
  destination = int(file.readline().rstrip())

  print(has_path(source, destination, graph))
  