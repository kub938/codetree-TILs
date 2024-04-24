n = int(input())
arr = list(map(int,input()))

def dist():
    min_dist = n
    for j in range(n):
        for k in range(j+1,n):
            if arr[j]==1 and arr[k]==1:
                dist = k-j
                min_dist = min(dist,min_dist)
    
    return min_dist

ans = 0

for i in range(n):
    if arr[i]==0:
        arr[i]=1
        ans = max(ans, dist())
        arr[i]=0

print(ans)