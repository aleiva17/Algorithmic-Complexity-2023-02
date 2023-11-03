
# 2 ^ n
def fibonacci(num):
  if num <= 1: return num
  return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(50))