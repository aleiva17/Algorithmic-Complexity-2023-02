"""

Sirenoman se prometió a sí mismo que nunca jugaría a videojuegos durante la universidad. No obstante, recientemente 
Firestorm, una conocida empresa de desarrollo de juegos, ha publicado su último juego: Volar Ant, y se 
hizo muy popular. Por supuesto, Sirenoman no pudo resistir la tentación y empezó a jugar.

Ahora intenta resolver una misión. La tarea consiste en llegar a un asentamiento llamado Fondo de Bikini y difundir
un rumor en él sobre un reciente virus para alertar a la población y que tomen precauciones.

Sirenoman sabe que hay N personajes en Fondo de Bikini. Algunos personajes son amigos entre sí y comparten la información 
que obtienen. Además, Sirenoman sabe que puede sobornar a cada personaje para que empiece a difundir el rumor.

El i-ésimo personaje quiere Ci de oro a cambio de difundir el rumor. Cuando un personaje escucha el rumor, y se lo cuenta 
a todos sus amigos, ellos empiezan a difundir el rumor a sus amigos (gratis), y así sucesivamente.

La búsqueda termina cuando los N personajes conocen el rumor. 

¿Cuál es la cantidad mínima de oro que Sirenoman necesita gastar para terminar la misión?

Ejemplo de datos de entrada 1:
  5 2
  2 5 3 4 8
  1 4
  4 5

Ejemplo de datos de salida 1:
  10

  
Ejemplo de datos de entrada 2:
  10 0
  1 2 3 4 5 6 7 8 9 10

Ejemplo de datos de salida 2:
  55

  
Ejemplo de datos de entrada 3:
  10 5
  1 6 2 7 3 8 4 9 5 10
  1 2
  3 4
  5 6
  7 8
  9 10

Ejemplo de datos de salida 3:
  15


  
Explicación de datos de entrada:
  - La primera línea contiene 2 número N y M (El número de habitantes en Fondo de Bikini y el número de pares de amigos)
  - La segunda línea contiene contiene N números que indica el Ci (costo en oro para decirle al habitante i que esparza el rumor
  - Luego, siguen M líneas que tiene un par de número X e Y que representan que los habitantes X e Y son amigos.

Explicación de datos de salida:
  - Imprime un único número que indica la cantidad mínima de oro que tiene que gastar Sirenoman para completar la misión  

"""

def dfs_min_cost_node(character, graph, visited, cost):
  visited[character] = True

  mn_cost = cost[character]

  for friend in graph[character]:
    if not visited[friend]:
      mn_cost = min(mn_cost, dfs_min_cost_node(friend, graph, visited, cost))
  
  return mn_cost


with open("in2.txt", "r") as file:
  n, m = map(int, file.readline().rstrip().split())
  cost = list(map(int, file.readline().rstrip().split()))

  graph = [[] for _ in range(n)]
  visited = [False] * n

  for _ in range(m):
    a, b = map(int, file.readline().rstrip().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
  
  total = 0

  for character in range(n):
    if not visited[character]:
      total += dfs_min_cost_node(character, graph, visited, cost)

  print(total)