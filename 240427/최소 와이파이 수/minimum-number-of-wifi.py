n,m = map(int,input().split())
arr = list(map(int,input().split()))

cnt = 0
i = 0
while i<=n-1:
    if arr[i]==1:
        cnt+=1
        i = i+m*2
    i+=1

print(cnt)