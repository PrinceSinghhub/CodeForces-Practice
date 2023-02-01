def findans(n,arr):

    ans = set()

    for i in range(n - 1, -1, -1):
        if arr[i] in ans:
            return i+1
        ans.add(arr[i])

    return 0

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(findans(n,arr))

