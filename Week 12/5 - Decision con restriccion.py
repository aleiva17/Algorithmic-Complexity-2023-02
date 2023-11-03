numeros = [9, 100, -4, 1, 5]
qty = 2
memo = [ [None for _ in range(qty + 1)] for _ in range(len(numeros)) ]

# Matriz
# memo[i][j] = Estando en el índice i con j números como máximo que puedo todavía 
#              seleccionar, cuál es la máxima suma que puedo tener

# RESTRICCIÓN: Si selecciono un número en la coordenada X, no puedo seleccionar el
# número en la coordenada siguiente.

# index: indice en el cuál me encuentro y debo tomar la decisión de si lo sumo o no
# k: la cantidad de números como máximo que todavía puedo seleccionar.

def dp(index, k):
  if index >= len(numeros) or k == 0: return 0

  if memo[index][k] != None:
    return memo[index][k]

  # Opción A: Selecciono el número actual
  first_subproblem = numeros[index] + dp(index + 2, k - 1)
  # Opción B: Ignoro el número actual
  second_subproblem = dp(index + 1, k)

  memo[index][k] = max(first_subproblem, second_subproblem)
  return memo[index][k]


print(f"La mayor suma con {qty} numeros con la restricción de {numeros} es: {dp(0, qty)}")