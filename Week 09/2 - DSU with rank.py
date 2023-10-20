
def find(parent_of, set_id):
  if parent_of[set_id] == set_id: 
    return set_id
  
  parent_id = find(parent_of, parent_of[set_id])
  parent_of[set_id] = parent_id
  return parent_id

def union(parent_of, rank_of, set_a, set_b):
  set_a = find(parent_of, set_a)
  set_b = find(parent_of, set_b)

  if set_a != set_b:
    if rank_of[set_a] >= rank_of[set_b]:
      parent_of[set_b] = set_a
      rank_of[set_a] += rank_of[set_b]
    else:
      parent_of[set_a] = set_b
      rank_of[set_b] += rank_of[set_a]


quantity = int(input("Ingrese la cantidad de elementos: "))
parent_of = [element for element in range(quantity + 1)]
rank_of = [1] * (quantity + 1)

# quantity = 6
# 1 2 3 4 5 6

union(parent_of, rank_of, 1, 4)
# 1-4 2 3 5 6

union(parent_of, rank_of, 2, 3)
# 1-4 2-3 5 6

union(parent_of, rank_of, 6, 5)
# 1-4 2-3 5-6

union(parent_of, rank_of, 5, 4)
# 1-4-5-6 2-3


for element in range(1, 7):
  print(f"Set ID del elemento {element}: {find(parent_of, element)}")