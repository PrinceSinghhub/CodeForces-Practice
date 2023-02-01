s = input()

arr = []
for i in s:
    if i.isdigit():
        arr.append(int(i))

arr.sort()
ans = ''
for i in arr:
    ans+=str(i)
    ans+='+'
print(ans[0:len(ans)-1])