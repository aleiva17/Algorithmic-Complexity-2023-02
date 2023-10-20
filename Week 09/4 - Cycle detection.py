
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



nodes = int(input("Ingrese la cantidad de nodos: "))
dsu = DSU(nodes)

edges = int(input("Ingrese la cantidad de aristas: "))

for _ in range(edges):
  a, b = map(int, input("Ingrese el conjunto A y B: ").split())

  if not dsu.union(a, b):
    print("SE DETECTÓ UN CICLO")