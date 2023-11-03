num = int(input("Ingrese el numero: "))

# memo[i] = fibonacci(i) 
#     -> Opcion A (memo[i] == None): No ha sido calculado previamente fibonacci(i)
#     -> Opcion B (memo[i] != None): Si he calculado previamente fibonacci(i)
memo = [None] * (num + 1)

def fibonacci(num):
  if num <= 1: return num

  # Opcion B: Si he calculado previamente fibonacci(num)
  if memo[num] != None:
    return memo[num]
  
  # Opcion A: No he calculado previamente fibonacci(num)
  # Por lo tanto, lo debo calcular y debo guardar ese valor en memo[num]

  # Resuelvo mi 1er subproblema
  first_subproblem = fibonacci(num - 1)
  second_subproblem = fibonacci(num - 2)

  memo[num] = first_subproblem + second_subproblem
  return memo[num]


print(fibonacci(num))