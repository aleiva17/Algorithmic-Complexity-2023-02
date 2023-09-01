"""
Utilizando la técnica de divide y vencerás:

Implementar una función para cada una de las siguientes operaciones
- Máximo elemento de un arreglo
- Mínimo elemento de un arreglo
- Suma de todos los elementos de un arreglo
- Multiplicación de todos los elementos de un arreglo
"""

def get_max_element(array):
  
  def divide_and_conquer(left, right):
    if left == right:
      return array[left]
    
    mid = (left + right) // 2
    left_sub_problem = divide_and_conquer(left, mid)
    right_sub_problem = divide_and_conquer(mid + 1, right)

    return max(left_sub_problem, right_sub_problem)

  return divide_and_conquer(0, len(array) - 1)


def get_min_element(array):
  
  def divide_and_conquer(left, right):
    if left == right:
      return array[left]
    
    mid = (left + right) // 2
    left_sub_problem = divide_and_conquer(left, mid)
    right_sub_problem = divide_and_conquer(mid + 1, right)

    return min(left_sub_problem, right_sub_problem)

  return divide_and_conquer(0, len(array) - 1)


def get_total_sum(array):
  
  def divide_and_conquer(left, right):
    if left == right:
      return array[left]
    
    mid = (left + right) // 2
    left_sub_problem = divide_and_conquer(left, mid)
    right_sub_problem = divide_and_conquer(mid + 1, right)

    return left_sub_problem + right_sub_problem

  return divide_and_conquer(0, len(array) - 1)


def get_total_mul(array):
  
  def divide_and_conquer(left, right):
    if left == right:
      return array[left]
    
    mid = (left + right) // 2
    left_sub_problem = divide_and_conquer(left, mid)
    right_sub_problem = divide_and_conquer(mid + 1, right)

    return left_sub_problem * right_sub_problem

  return divide_and_conquer(0, len(array) - 1)


nums = [2, 4, 6, 3, 1, 5, -99]

print(f"Max Element: {get_max_element(nums)}") 
# Output: 6

print(f"Min Element: {get_min_element(nums)}")
# Output: -99

print(f"Total Sum: {get_total_sum(nums)}")
# Output: -78

print(f"Total Mul: {get_total_mul(nums)}")
# Output: -71280