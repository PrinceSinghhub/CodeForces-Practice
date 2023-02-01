t = int(input())
count = 0
for i in range(t):

    n = input()

    if n[1] == '+':
        count+=1
    else:
        count-=1

print(count)