"""
Utilizando la técnica de recursión:

Dado un número entero N, retorna el valor de la suma del doble de cada número desde N hasta 1.

ej.
  N = 4
  Respuesta: (4 * 2) + (3 * 2) + (2 * 2) + (1 * 2) = 20
"""

def double_sum(n):
  if n == 0: 
    return 0
  return n * 2 + double_sum(n - 1)

print(double_sum(4))
# Output: 20

print(double_sum(5))
# Output: 30