
with open("input.txt", "r") as file:
  line = file.readline().rstrip()

  nodes, edges = map(int, line.split())
  graph = [[] for _ in range(nodes + 1)]

  ind = [0] * (nodes + 1)

  for _ in range(edges):
    line = file.readline().rstrip()
    a, b = map(int, line.split())

    graph[a].append(b)
    ind[b] += 1
  
  queue = []
  toposort = []

  for node in range(1, nodes + 1):
    if ind[node] == 0:
      queue.append(node)
  
  while len(queue):
    node = queue.pop(0)

    toposort.append(node)

    for neighbour in graph[node]:
      ind[neighbour] -= 1
      if (ind[neighbour] == 0):
        queue.append(neighbour)

 
  print(toposort)