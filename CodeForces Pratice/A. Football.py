n = input()
flag = 0
for i in range(len(n)):
    count = 1

    for j in range(i+1,len(n)):

        if n[i] == n[j]:
            count+=1

        else:
            break
    if count >= 7:
        print("YES")
        flag = 1
        break
if flag == 0:
    print("NO")

