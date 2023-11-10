# All Pair Shortest-Path (APSP)

# Objetivos:
# - Hallar el camino mínimo para todos los posibles pares de vértices
# - Puede deterctar ciclos negativos (pero con un paso extra)
# - DP based algorithm

# Consideraciones
# - Debemos utilizar una matriz de adyacencia
# - Sí sirve para pesos negativos
# - No deben haber ciclos negativos
# - Al inicio se asume que todas las distancias son infinito

# Complejidad
# Tiempo: O(V^3)
# Espacio: O(V^2)
import math

def floyd_warshall(matrix):
  max_range = range(len(matrix)) # La cantidad de nodos
  distaces = [row.copy() for row in matrix.copy()]

  for k in max_range:
    for j in max_range:
      for i in max_range:
        if distaces[i][j] > distaces[i][k] + distaces[k][j]:
          distaces[i][j] = distaces[i][k] + distaces[k][j]

  return distaces


nodes, edges = map(int, input("Ingrese la cantidad de nodos y aristas: ").split())
graph = [[math.inf] * nodes for _ in range(nodes)]
# graph[i][j] = el peso de la arista que conecta el nodo i con j

# Para cada nodo, el peso mínimo para llegar del nodo i al nodo i es 0
for i in range(nodes):
  graph[i][i] = 0

# Lectura de las aristas
for _ in range(edges):
  a, b, w = map(int, input("Ingrese el nodo origen, destino y el peso: ").split())
  graph[a - 1][b - 1] = w

distances = floyd_warshall(graph)
# distances[i][j] = el camino mínimo para llegar al nodo j partiendo desde el nodo i

for index, row in enumerate(distances):
  print(f"Shortest Path from Node #{index + 1}", end=": ")

  for d in row:
    print(d, end=" ")

  print()