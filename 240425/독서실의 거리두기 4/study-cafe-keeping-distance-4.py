n = int(input())
arr = list(map(int,input()))

def min_diff():
    diff = 100
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]==1 and arr[j]==1:
                diff=min(diff,j-i)
    return diff

ans = 0

for i in range(n):
    if arr[i]==0:
        arr[i]=1
    else:
        continue
    for j in range(i+1,n):
        
        if arr[j]==0:
            arr[j]=1
        else:
            continue
        ans = max(ans,min_diff())
        arr[j]=0
    arr[i]=0

print(ans)