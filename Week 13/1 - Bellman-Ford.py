# Single Source Shortest-Path (SSSP)

# Objetivos:
# - Permite identificar si existen ciclos negativos en el grafo.
# - Hallar el camino mínimo desde un nodo origen al resto.


# Considerar:
# - Debemos utilizar una edge list (lista de aristas)
# - Realizar la relajación (La parte más importante del algoritmo)
# - Al inicio se asume que todas las distancias son infinito

# Complejidad
# Tiempo: O (V * E)
# Espacio: O(n) 
import math

def bellman_ford(edge_list, source, qty_nodes):
  # distaces[i] = el camino mínimo para llegar desde el origen hasta el nodo i
  distances = [math.inf] * qty_nodes
  # El camino mínimo para llegar del nodo origen al nodo origen es 0
  distances[source] = 0

  # Relajación (DP)
  for _ in range(1, qty_nodes):
    for a, b, w in edge_list:
      if distances[a] != math.inf and distances[a] + w < distances[b]:
        distances[b] = distances[a] + w
  
  # Verificar que no existan ciclos negativos
  for a, b, w in edge_list:
    if distances[a] != math.inf and distances[a] + w < distances[b]:
      print("Encontramos un ciclo negativo. Por ende, no hay respuesta.")
      return []

  return distances


# Lectura de datos
nodes, edges = map(int, input("Ingrese la cantidad de nodos y aristas: ").split())
edge_list = []

# Indexado en 1
for _ in range(edges):
  a, b, w = map(int, input("Ingrese el nodo origen, destino y el peso: ").split())
  # Convierto 1-based index a 0-based
  edge_list.append((a - 1, b - 1, w))


origin = int(input("Ingrese el nodo de origen: ")) 

# Bellman ford retorna un arreglo de distancias
# distaces[i] = el camino mínimo para llegar desde el origen hasta el nodo i
distances = bellman_ford(edge_list, origin - 1, nodes)

# Si NO existe un ciclo negativo:
if distances:
  print(f"El camino mínimo desde el nodo {origin} hasta:")
  for i in range(nodes):
    print(f"Hasta el nodo #{i + 1}: {distances[i]}")