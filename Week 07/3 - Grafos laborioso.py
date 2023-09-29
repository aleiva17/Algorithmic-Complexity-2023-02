"""

Considere el laberinto mostrado en la imagen "maze.png" como una matriz dónde 'X' sea las paredes (color negro)
y un espacio vacío ' ' como un camino libre (el resto de colores).

Además, considere que el cuadrado de color amarillo central superior es la coordenada inicial y la inferior es
la coordenada final.

Se le pide:
  A) Hallar la cantidad de recuadros que serían recorridos (sin considerar el inicial y final) al utilizar
     el algoritmo de BFS.
  
  B) Imprima la matriz dónde muestre con la letra 'O' las celdas que serían visitadas al realizar BFS. 

  C) [BONUS - TAREA] Imprima el camino mínimo que tendría que realizar para llegar de la coordenada inicial a la final.
      Hint: Puede considerar una matriz adicional que guarde para cada coordenada las coordenadas de las que proviene.
            Es decir, un matriz que guarde pares (tuplas)
"""

maze = [
  ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
  ['X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X'],
  ['X', ' ', 'X', ' ', 'X', 'X', 'X', ' ', 'X', ' ', 'X'],
  ['X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X'],
  ['X', ' ', 'X', 'X', 'X', 'X', 'X', ' ', 'X', 'X', 'X'],
  ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X'],
  ['X', ' ', 'X', ' ', 'X', 'X', 'X', ' ', 'X', 'X', 'X'],
  ['X', ' ', 'X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' '],
  ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
]

coord_inicial = (5, 3)
x_final = 10
y_final = 7

diferenciales = [(0, -1), (1, 0), (0, 1), (-1, 0)]
w = 11
h = 9

# Pregunta A y B
cantidad = 0

queue = [coord_inicial]
visited = [[False for _ in range(w)] for _ in range(h)]
visited[coord_inicial[1]][coord_inicial[0]] = True

while len(queue):
  x, y = queue.pop(0)

  maze[y][x] = 'O'
  cantidad += 1

  if (x == x_final and y == y_final):
    break

  for dx, dy in diferenciales:
    new_x = x + dx
    new_y = y + dy

    if new_x < 0 or new_y < 0: continue
    if new_x >= w or new_y >= h: continue
    if visited[new_y][new_x] or maze[new_y][new_x] == 'X': continue

    queue.append((new_x, new_y))
    visited[new_y][new_x] = True

print(f"La cantidad de recuadros que se recorriendo al hacer BFS es: {cantidad}")

for row in maze:
  print(row)