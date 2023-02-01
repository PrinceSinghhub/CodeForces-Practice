n = int(input())

for i in range(n):
    s = input()

    if len(s) <= 10:
        print(s)

    else:
        ans = ''
        ans+=s[0]
        L = len(s)-2
        ans+=str(L)
        ans+=s[-1]
        print(ans)