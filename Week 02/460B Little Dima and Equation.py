# [BRUTEFORCE] PROBLEM LINK: https://codeforces.com/contest/460/problem/B
# x = b · s(x)^a  +  c, 
a, b, c = map(int, input().split())
ans = []

def sum_of_digits(x):
    ans = 0
    for digit in str(x):
        ans += int(digit)
    return ans

for sx in range(1, 82):
    x = b * pow(sx, a) + c

    if x < 0:
        continue

    if x >= 1000000000:
        break
    
    if sum_of_digits(x) == sx:
        ans.append(x)
    
print(len(ans))
for valid_answer in ans:
    print(valid_answer, end=" ")