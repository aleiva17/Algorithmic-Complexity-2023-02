"""
Utilizando la técnica de fuerza bruta:

Dado un arreglo de números, imprime todos los posibles pares de números cuya suma sea igual a X.
  ej: 
    Arreglo: [1, 2, 3, 4, 5, 6, 8]
    X: 9

    Respuestas:
      1 8
      3 6
      4 5
"""

def all_pairs_that_sum(array, target):
  answers = []

  # for (int i = 0; i < n - 1; ++i)
  for i in range(len(array) - 1):
    first_number = array[i]

    # for (int j = i + 1; j < n; ++j)
    for j in range(i + 1, len(array)):
      second_number = array[j]

      if first_number + second_number == target:
        answers.append([first_number, second_number])

  return answers


print(all_pairs_that_sum([1, 2, 3, 4, 5, 6, 8], 9))
# Output: [[1, 8], [3, 6], [4, 5]]

print(all_pairs_that_sum([5, 5, 10, 0, 14, 15, 20, -5], 10))
# Output: [[5, 5], [10, 0], [15, -5]]