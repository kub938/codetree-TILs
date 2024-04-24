n,k = map(int,input().split())
arr = [int(input()) for _ in range(n)]

ans = 0
for i in range(10001):
    cnt=0
    for j in range(n):
        if i<=arr[j]<=i+k:
            cnt+=1
    ans = max(ans,cnt)

print(ans)