n = int(input())
tmp = list(map(int,input().split()))
arr = []

print(tmp[0],end=" ")
for i in range(n):
    arr.append(tmp[i])
    if i%2!=0:
        arr.sort()
        print(arr[i//2+1],end=" ")