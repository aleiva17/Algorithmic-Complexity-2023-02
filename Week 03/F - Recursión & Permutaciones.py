"""
Utilizando la técnica de recursión:

Implementa una función (recursiva) que reciba como parámetro un entero positivo N
e imprima todas las PERMUTACIONES (en cualquier orden) de números entre 1 y N cuya suma sea N

ej:
  N: 4

  Respuestas:
    { 1, 1, 1, 1 },
    { 1, 1, 2 },
    { 1, 2, 1 },
    { 2, 1, 1 }
    { 1, 3 },
    { 3, 1 }
    { 2, 2 }
    { 4 }
"""

def print_all_permutations_that_sum(n):
  
  def recursion(pending, numbers_prev_used):
    if not pending:
      print(numbers_prev_used)
      return
    
    for digit in range(1, min(pending, n) + 1):
      recursion(pending - digit, numbers_prev_used + str(digit))

  
  recursion(n, "")


print("N = 5")
print_all_permutations_that_sum(5)

print("\nN = 4")
print_all_permutations_that_sum(4)