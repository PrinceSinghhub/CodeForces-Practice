t = int(input())
for _ in range(t):

    s = input()
    if (s[0] != 'y' and s[0] != 'Y'):
        print("NO")

    elif (s[1] != 'e' and s[1] != 'E'):
        print("NO")

    elif (s[2] != 's' and s[2] != 'S'):
        print("NO")

    else:
        print("YES")

