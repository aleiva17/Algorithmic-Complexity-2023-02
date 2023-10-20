
# Retorna el id del conjunto
def find(parent_of, set_id):
  # Si el padre del nodo X es X, significa que ese es el id del conjunto
  if parent_of[set_id] == set_id: 
    return set_id

  # El conjunto actual, tiene un padre. Tenemos que hallar el id del conjunto
  # del padre.
  parent_id = find(parent_of, parent_of[set_id])
  # Actualizo el padre del conjunto actual para que apunte directamente al id
  # del conjunto terminal
  parent_of[set_id] = parent_id

  # Y lo retorno
  return parent_id


def union(parent_of, set_a, set_b):
  set_a = find(parent_of, set_a)
  set_b = find(parent_of, set_b)

  # Significa, que el set_a no pertenece al set_b
  if set_a != set_b:
    parent_of[set_a] = set_b


quantity = int(input("Ingrese la cantidad de elementos: "))
parent_of = [element for element in range(quantity + 1)]

# quantity = 6
# 1 2 3 4 5 6

union(parent_of, 1, 4)
# 1-4 2 3 5 6

union(parent_of, 2, 3)
# 1-4 2-3 5 6

union(parent_of, 6, 5)
# 1-4 2-3 5-6

union(parent_of, 5, 4)
# 1-4-5-6 2-3


for element in range(1, 7):
  print(f"Set ID del elemento {element}: {find(parent_of, element)}")