import sys

n,s = map(int,input().split())
arr = list(map(int,input().split()))
near_s = sys.maxsize

for i in range(n-1):
    for j in range(i+1,n):
        a,b = arr[i],arr[j]
        arr[i],arr[j] = 0,0
        near_s = min(near_s,abs(sum(arr)-s))
        arr[i],arr[j] = a,b

print(near_s)