n = input()
sml = 0
larg = 0

for i in n:
    if i.islower():
        sml+=1
    else:
        larg+=1

if larg > sml:
    print(n.upper())
else:
    print(n.lower())
