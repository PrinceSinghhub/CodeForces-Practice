t = int(input())
for _ in range(t):
    n = int(input())

    a = 0
    b = 0
    for i in range(3):
        lst = n%10
        a+=lst
        n = n // 10

    for i in range(3):
        lst = n%10
        b+=lst
        n = n // 10

    if a == b:
        print("YES")
    else:
        print("NO")
