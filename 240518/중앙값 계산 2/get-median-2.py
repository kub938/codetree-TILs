n = int(input())
tmp = [0]+list(map(int,input().split()))
arr = []

for i in range(1,n+1):
    arr.append(tmp[i])

    if i%2!=0:
        arr.sort()
        print(arr[i//2],end=" ")