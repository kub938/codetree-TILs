n,m = tuple(map(int,input().split()))
data = list(input().split())
target = list(input().split())

arr = {}

for a in data:
    if a in arr:
        arr[a] = arr[a]+1
    else:
        arr[a]=1

for t in target:
    if t in arr:
        print(arr[t],end=" ")
    else:
        print(0,end=" ")