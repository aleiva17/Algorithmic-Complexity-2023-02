""" [MISMO ENUNCIADO QUE ANTES SÓLO QUE AHORA SON COMBINACIONES]
Utilizando la técnica de recursión:

Implementa una función (recursiva) que reciba como parámetro un entero positivo N
e imprima todas las combinaciones (en cualquier orden) de números entre 1 y N cuya suma sea N

ej:
  N: 5

  Respuestas:
    { 5 },
    { 1, 4 },
    { 2, 3 },
    { 1, 1, 3 },
    { 1, 2, 2 },
    { 1, 1, 1, 2 },
    { 1, 1, 1, 1, 1 }

  N: 4

  Respuestas:
    { 4 },
    { 1, 3 },
    { 2, 2 },
    { 1, 1, 2 },
    { 1, 1, 1, 1 }
"""

def print_all_combinations_that_sum(n):
  combinations = set()

  def recursion(pending, numbers_prev_used):
    if not pending:
      sorted_path = sorted(numbers_prev_used)
      combinations.add("".join(sorted_path))
      return
    
    for digit in range(1, min(pending, n) + 1):
      recursion(pending - digit, numbers_prev_used + str(digit))

  recursion(n, "")

  for comb in combinations:
    print(comb)
  

print("N = 5")
print_all_combinations_that_sum(5)

print("\nN = 4")
print_all_combinations_that_sum(4)