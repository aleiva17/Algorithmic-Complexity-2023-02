# [BRUTEFORCE] PROBLEM LINK: https://codeforces.com/contest/271/problem/A

# 2000
base_year = int(input())
# 2001
answer = base_year + 1

def distinct(year):
    # st = set()

    # for digit in str(year):
    #     st.add(digit)
    return len(set(digit for digit in str(year))) == 4

while not distinct(answer):
    answer += 1

print(answer)