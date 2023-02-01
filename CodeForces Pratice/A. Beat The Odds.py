t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    old = 0
    for j in arr:
        if j & 1:
            old += 1
    print(min(old, n - old))
