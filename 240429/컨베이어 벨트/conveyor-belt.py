n,t = map(int,input().split())

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

for i in range(t):
    tmp1,tmp2 = arr1[-1],arr2[-1]
    for j in range(n-1,0,-1):
        arr1[j]=arr1[j-1]
        arr2[j]=arr2[j-1]
    arr1[0] = tmp2
    arr2[0] = tmp1



print(*arr1)
print(*arr2)