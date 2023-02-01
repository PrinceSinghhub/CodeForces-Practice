n = int(input())
count = 0

while n > 0:
    if n >= 5:
        n-=5
        count+=1
    if n >= 4 and n < 5:
        n-=4
        count+=1
    if n >= 3 and n < 4:
        n-=3
        count+=1
    if n >= 2 and n < 3:
        n-=2
        count+=1
    if n == 1:
        n-=1
        count+=1
print(count)
