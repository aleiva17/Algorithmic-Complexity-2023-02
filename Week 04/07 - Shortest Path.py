# Considere el siguiente grafo (imagen: "Graph 07.png")
# e implemente una función que retorne el camino mínimo
# desde un NODO A hasta un NODO B. Si NO existe un camino,
# debe de retornar -1

# SOLAMENTE PODEMOS USAR BFS (Y TAMBIÉN SOLAMENTE CUANDO LAS
# TODAS LAS ARISTAS TENGAN EL MISMO PESO)
def get_shortest_path(graph, source, destination):
  visited = set() # Hash set -> Hast table en el que las keys == values

  queue = []
  queue.append( (source, 0) )
  visited.add(source)

  while len(queue):
    # Extraer el primer nodo de la cola
    node, distance = queue.pop(0)

    # Procesar el nodo (haz lo que quieras con él)
    if node == destination:
      return distance
    
    # Para cada nodo vecino NO visitado, lo agrego a la cola
    # con distancia = distancialActual + 1
    for neighbour in graph[node]:
      if neighbour not in visited:
        queue.append((neighbour, distance + 1))
        visited.add(neighbour)


# Interpretación:
#   graph[i]: Vecinos del nodo i
#   ej.
#       graph["A"]: El vecino del nodo A es B, C y G

graph = {
  "A": ["B", "C", "G"],
  "B": ["A", "I"],
  "C": ["A", "D"],
  "D": ["C", "E"],
  "E": ["D", "F"],
  "F": ["E", "H"],
  "G": ["A", "H"],
  "H": ["F", "G", "J"],
  "I": ["B", "J"],
  "J": ["H", "I"],
}

test_1 = get_shortest_path(graph, "A", "H")
print(f"El camino mínimo desde A hasta H es {test_1}")

test_2 = get_shortest_path(graph, "C", "J")
print(f"El camino mínimo desde C hasta J es {test_2}")