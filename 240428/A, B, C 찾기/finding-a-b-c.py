arr = list(map(int,input().split()))
arr.sort()
n = len(arr)
a,b,c = arr[0],0,0

for i in range(1,n-1):
    for j in range(i,n-1):
        if a+arr[i]+arr[j]==arr[-1]:
            b,c=arr[i],arr[j]

print(a,b,c)