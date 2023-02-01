t = int(input())
for _ in range(t):
    n = int(input())
    cnt1 = 0
    cnt2 = 0

    while n % 2 == 0:
        cnt1 += 1
        n = n // 2

    while n % 3 == 0:
        cnt2 += 1
        n = n // 3

    if cnt2 >= cnt1 and n == 1:
        print(2 * cnt2 - cnt1)

    else:
        print(-1)


