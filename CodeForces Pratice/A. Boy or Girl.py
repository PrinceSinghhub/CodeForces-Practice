def solve(n):
    arr = set(n)
    if len(arr) % 2 != 0:
        print("IGNORE HIM!")
    else:
        print("CHAT WITH HER!")
n = input()
solve(n)
