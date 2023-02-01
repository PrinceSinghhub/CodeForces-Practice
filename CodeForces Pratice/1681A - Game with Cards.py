t = int(input())
for i in range(t):
    n = int(input())
    alicia = list(map(int, input().split()))
    m = int(input())
    bob = list(map(int, input().split()))

    if max(alicia) >= max(bob):
        print('Alice')
    else:
        print('Bob')

    if max(alicia) > max(bob):
        print('Alice')
    else:
        print('Bob')