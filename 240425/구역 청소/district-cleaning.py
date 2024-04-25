a,b = map(int,input().split())
c,d = map(int,input().split())
arr = [0]*101

for i in range(a,b+1):
    arr[i]=1

for i in range(c,d+1):
    arr[i]=1

print(arr.count(1)-1)