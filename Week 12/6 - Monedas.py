# Dado un arreglo de N monedas con valores X1, X2, ..., Xn
coins = [7, 1, 5]
# Y un monto X, determine la mínima cantidad de monedas que puedes
# utilizar para cambiar el valor. Si no se puede, imprima -1
monto = 11

# 7 1 1 1 1 (5 monedas)
# 1 1 1 ... 1 (11 monedas)
# 5 5 1 (3 monedas)

queue = [ (monto, 0) ]
visited = [False] * (monto + 1)

while len(queue):
  balance, steps = queue[0]
  queue.pop(0)

  if balance == 0:
    print(f"La minima cantida de monedas es: {steps}")
    exit(0)

  for coin in coins:
    if balance - coin >= 0 and not visited[balance - coin]:
      queue.append((balance - coin, steps + 1))
      visited[balance - coin] = True


print("No puede realizar el cambio con las monedas seleccionadas")