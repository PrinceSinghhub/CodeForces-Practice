Limak,Bob = map(int,input().split())

count = 0
Limak*=3
Bob*=2
count+=1

while Limak <= Bob:
    Limak*=3
    Bob*=2
    count+=1
print(count)