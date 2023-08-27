# [BRUTEFORCE] PROBLEM LINK: https://codeforces.com/problemset/problem/122/A

lucky_numbers = []
n = int(input())
answer = False

def recursive(mx, actual):
    if actual > mx: return

    if actual != 0:
        lucky_numbers.append(actual)

    # Opción A: Agrego el dígito 4, al final del número
    recursive(mx, actual * 10 + 4)
    # Opción B: Agrego el dígito 7, al final del número
    recursive(mx, actual * 10 + 7)

recursive(n, 0)

for lucky_num in lucky_numbers:
    if n % lucky_num == 0:
        answer = True
        break

print("YES" if answer else "NO")