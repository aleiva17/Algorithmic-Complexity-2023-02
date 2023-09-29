"""
En un país muy lejano, existe una ciudad llamada LOS AMISTOSOS con N residentes. Se sabe que varios pares
de estos residentes son amigos, así que, acorde a la frase que reza: 

  "Los amigos de mis amigos son mis amigos también"

Significa que si A es amigo de B y B es amigo de C, entonces A y C son amigos.

La tarea que se le encomienda como experto programador, es el de escribir un programa que contabilice cuántos
residentes existen en la ciudad de LOS AMISTOSOS a partir de un grupo de amigos.

Como dato de entrada, el programa recibe un archivo de texto.

  Ejemplo de entrada:
    2
    3 2
    1 2
    2 3
    10 12
    1 2
    3 1
    3 4
    5 4
    3 5
    4 6
    5 2
    2 1
    7 1
    1 2
    9 10
    8 9
  
  Dónde:
    - Dónde, la primera línea identifica los casos a evaluar (variable C)
    - Cada línea de caso a evaluar se distingue por una línea conteniendo 2 números enteros separados por
      un espacio en blanco.

      N (dónde N >= 1 y N <= 30000) es el número de residentes en el pueblo
      M (dónde M >= 0 y < <= 500000) es el número de pares de persona consideradas amigas
    
    - Las siguientes M líneas contienen 2 números enteros cada una, separados por un espacio en blanco:
      A y B, que describe que son amigos (dónde A >= 1 y A <= N, B >= 1 y B <= N, A != B). Considere que
      podría haber repeticiones entre los pares dados.

  Para cada caso que procese, deberá mostrar como salida (en una sola línea) un número que indique cuántas personas
  hay en el grupo más grande de amigos en una línea por sí mismo. El resultado de cada caso evaluado debe contener
  (en una sóla línea) un número que indique cuántas personas hay en el grupo más grande de amigos.

  Ejemplo de salida:
    Caso #1 - Tot. Residentes: 3
    Caso #2 - Tot. Residentes: 7

    
  Se le solicita:
    A) Desarrollar un código en Python que lea el archivo de texto y determine la salida de datos deseada (7pts)
    B) Indicar el algoritmo que tomó de base para solucionar este ejercicio y porqué (1pto)
  
  Se tendrá en cuenta para la calificación el orden y la explicación (documentación) de su solución. Puede adjuntar
  su solución en formato "py" o "ipynb"
"""

def calcular_componente_mayor(file):
  n, m = map(int, file.readline().rstrip().split())
  graph = [[] for _ in range(n + 1)]

  for _ in range(m):
    a, b = map(int, file.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

  # BFS, pero se puede hacer con DFS perfectamente
  visited = [False] * (n + 1)
  ans = 0

  for residente in range(1, n + 1):
    if visited[residente]: continue

    longitud_del_grupo_de_amigos = 0

    queue = [residente] # deque()
    visited[residente] = True

    while len(queue):
      persona = queue.pop(0)
      
      longitud_del_grupo_de_amigos += 1

      for amigo in graph[persona]:
        if not visited[amigo]:
          visited[amigo] = True
          queue.append(amigo)
    
    ans = max(ans, longitud_del_grupo_de_amigos)

  return ans


with open("in1.txt", "r") as file:
  test_cases = int(file.readline().rstrip())

  for test_case in range(test_cases):
    print(f"Caso #{test_case + 1} - Tot. Residentes: { calcular_componente_mayor(file) }")