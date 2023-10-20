import heapq

def prim_mst(graph, quantity_of_nodes):
  priority_queue = []
  visited = [False] * (quantity_of_nodes + 1)

  min_weight = 0

  # Order: (Weight - Node)
  heapq.heappush(priority_queue, (0, 1))

  while len(priority_queue) > 0:
    weight, to = heapq.heappop(priority_queue)

    if visited[to]:
      continue

    min_weight += weight
    visited[to] = True

    for neighbour in graph[to]:
      if visited[neighbour[0]]: continue
      heapq.heappush(priority_queue, (neighbour[1], neighbour[0]))


  return min_weight


quantity_of_nodes = int(input("Ingrese la cantidad de nodos: "))
quantity_of_edges = int(input("Ingrese la cantidad de aristas: "))

graph = [[] for _ in range(quantity_of_nodes + 1)]

for i in range(quantity_of_edges):
  w, a, b = map(int, input(f"Ingrese el PESO y el nodo A y B de la arista #{i + 1}: ").split())
  graph[a].append((b, w))
  graph[b].append((a, w))

print(prim_mst(graph, quantity_of_nodes))