target, init = map(int, input("Ingrese el número objetivo y el número inicial: ").split())

if init >= target:
  print(f"La cantidad mínima de botones a presiona es: {init - target}")
  exit(0)

# DP con BFS
seen = set() # hash set -> hash table (key = value) [Amortizado O(1) lectura y escritura]
queue = [(init, 0)] # (init, 0) He llegado al nodo init con 0 botones presionados
seen.add(init)

while len(queue):
  current_value, distance = queue.pop(0)

  if current_value == target:
    print(f"La cantidad mínima de botones a presiona es: {distance}")
    exit(0)

  # Presiono el botón para restarle 1 al valor actual
  if current_value - 1 > 0:
    new_num = current_value - 1
    
    if new_num not in seen:
      queue.append( (new_num, distance + 1) )
      seen.add(new_num)

  # Presiono el botón para multiplicar por 2 el valor actual
  if current_value < target:
    new_num = 2 * current_value

    if new_num not in seen:
      queue.append((new_num, distance + 1))
      seen.add(new_num)
