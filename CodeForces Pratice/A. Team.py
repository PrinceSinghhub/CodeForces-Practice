n = int(input())
friends = []
count = 0
for i in range(n):

    inputs = list(map(int, input().split()))
    friends.append(inputs)

for i in friends:

    if i.count(1) > 1:
        count+=1

print(count)



