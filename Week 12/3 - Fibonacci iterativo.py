num = int(input("Ingrese el numero: "))

# fib[i] = fibonacci(i)
fib = [0] * (num + 1)

# Casos base
fib[0] = 0
fib[1] = 1

# Voy construyendo mi respuesta desde el valor más pequeño al más alto
for number in range(2, num + 1):
  fib[number] = fib[number - 1] + fib[number - 2]

print(fib[num])