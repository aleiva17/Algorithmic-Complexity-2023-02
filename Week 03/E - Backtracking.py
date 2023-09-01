"""
Utilizando la técnica de backtracking:

Implemente una función que imprima para un arreglo de tamaño N todos los posibles
arreglo con valores del 1 al 9 en cada celda.

ej:
  N = 2
  Respuestas:
    [1, 1]
    [1, 2]
    [1, 3]
    [1, 4]
    [1, 5]
    [1, 6]
    [1, 7]
    [1, 8]
    [1, 9]
    [2, 1]
    [2, 2]
    [2, 3]
    [2, 4]
    [2, 5]
    [2, 6]
    [2, 7]
    [2, 8]
    [2, 9]
    ...
    [9, 9]
"""

def solve(n):
  initial_state = [0] * n
  digits = range(1, 10) # 1, 2, 3, 4, 5, 6, 7, 8, 9

  def backtracking(index, array):
    if index == n:
      print(array)
      return
    
    # Colocar un número en la celda actual (index) del 1 al 9
    for digit in digits:
      array[index] = digit
      backtracking(index + 1, array)


  backtracking(0, initial_state)


solve(3)