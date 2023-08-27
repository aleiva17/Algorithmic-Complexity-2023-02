from collections import deque
import heapq

vector = list()

# Podemos usar la lista como queue y stack
# Pero es bastante ineficiente
queue = []
stack = []

hash_set = set()
hash_table = dict()

deque_structure = deque()

# Podemos usar deque como queue y stack
# Es mucho más eficiente que utilizar una lista
better_queue = deque()
better_stack = deque()

# Usamos una lista para priority queue (heap)
heap = []
# Con heapq utilizamos los métodos del priorityqueue (heap)
heapq.heappush(heap, 3)
heapq.heappush(heap, 2)
heapq.heappush(heap, 99)
heapq.heappush(heap, -1)
heapq.heappush(heap, 0)

for element in heap:
    print(element, end=" > ")