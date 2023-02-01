n = int(input())
for _ in range(n):
    inp = int(input())

    if inp & (inp-1):
        print('YES')
    else:
        print('NO')