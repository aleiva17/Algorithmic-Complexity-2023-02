numeros = [7, 10, 8, -1, 4]
qty = 2
memo = [ [None for _ in range(qty + 1)] for _ in range(len(numeros)) ]

# Matriz
# memo[i][j] = Estando en el índice i con j números como máximo que puedo todavía 
#              seleccionar, cuál es la máxima suma que puedo tener

# index: indice en el cuál me encuentro y debo tomar la decisión de si lo sumo o no
# k: la cantidad de números como máximo que todavía puedo seleccionar.

def dp(index, k):
  if index >= len(numeros) or k == 0: return 0

  if memo[index][k] != None:
    return memo[index][k]

  # Decido seleccionar el número en el índice actual
  first_subproblem = numeros[index] + dp(index + 1, k - 1)
  # Decido NO seleccionar el número en el índice actual
  second_subproblem = dp(index + 1, k)

  memo[index][k] = max(first_subproblem, second_subproblem)
  return memo[index][k]


print(f"La mayor suma con {qty} numeros de {numeros} es: {dp(0, qty)}")