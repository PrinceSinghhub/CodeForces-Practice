def findans(inp):
    a = set()
    ind = 1
    while ind * ind <= inp:
        a.add(ind * ind)
        ind += 1
    ind2 = 1
    while ind2 * ind2 * ind2 <= inp:
        a.add(ind2 * ind2 * ind2)
        ind2 += 1
    print(len(a))



t = int(input())
for _ in range(t):
    n = int(input())
    findans(n)


