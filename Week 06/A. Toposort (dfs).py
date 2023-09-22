
def dfs(node, graph, visited, toposort):
  visited[node] = True

  for neighbour in graph[node]:
    if not visited[neighbour]:
      dfs(neighbour, graph, visited, toposort)
  
  toposort.append(node)


with open("input.txt", "r") as file:
  line = file.readline().rstrip()

  nodes, edges = map(int, line.split())
  graph = [[] for _ in range(nodes + 1)]

  for _ in range(edges):
    line = file.readline().rstrip()
    a, b = map(int, line.split())
    graph[a].append(b)
  
  toposort = []
  visited = [False] * (nodes + 1)

  for node in range(1, nodes + 1):
    if not visited[node]:
      dfs(node, graph, visited, toposort)

  print(toposort[::-1])
