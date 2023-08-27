# [BRUTEFORCE]PROBLEM LINK: https://codeforces.com/problemset/problem/1228/A

# 121 130
# input().split() -> ['121', '130']
# map() -> itera sobre un iterable y para cada elemento ejecuta una
# función que retorna un valor
l, r = map(int, input().split())
answer = None

# range(a, b) -> a, a + 1, ..., b - 1
# range(a) -> 0, 1, 2, ..., a - 1
for number in range(l, r + 1):
    if len(set(digit for digit in str(number))) == len(str(number)):
        answer = number
        break

# if not answer:
#     print(-1)
# else:
#     print(answer)
# Equivale al ternary operator
print(-1 if not answer else answer)