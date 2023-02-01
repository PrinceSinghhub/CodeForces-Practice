t = int(input())
for test in range(t):
    a,b,c,d = map(int, input().split())
    rs = (b > a) + (c > a) + (d > a)
    print(rs)