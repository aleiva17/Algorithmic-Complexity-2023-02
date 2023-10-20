
class DSU:
  def __init__(self, quatity_of_elements) -> None:
    self.parent_of = [i for i in range(quatity_of_elements + 1)]
    self.rank_of = [1] * (quatity_of_elements + 1)
  
  def find(self, id):
    if self.parent_of[id] == id:
      return id
    
    parent_id = self.find(self.parent_of[id])
    self.parent_of[id] = parent_id

    return parent_id

  def union(self, set_a, set_b):
    set_a = self.find(set_a)
    set_b = self.find(set_b)

    if set_a == set_b:
      return False
    
    if self.rank_of[set_a] >= self.rank_of[set_b]:
      self.parent_of[set_b] = set_a
      self.rank_of[set_a] += self.rank_of[set_b]
    else:
      self.parent_of[set_a] = set_b
      self.rank_of[set_b] += self.rank_of[set_a]

    return True


quantity_of_nodes = int(input("Ingrese la cantidad de nodos: "))
quantity_of_edges = int(input("Ingrese la cantidad de aristas: "))

dsu = DSU(quantity_of_nodes)
edge_list = []

for i in range(quantity_of_edges):
  w, a, b = map(int, input(f"Ingrese el PESO y el nodo A y B de la arista #{i + 1}: ").split())
  edge_list.append((w, a, b))

edge_list.sort()

min_weight = 0
tree = []

for w, a, b in edge_list:
  if dsu.union(a, b):
    min_weight += w
    tree.append((a, b))

print(f"MST: {min_weight}")
print(f"Tree: {tree}")