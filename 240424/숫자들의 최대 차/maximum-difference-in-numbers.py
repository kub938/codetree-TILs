n,k = map(int,input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
ans = 0

for i in range(n):
    cnt=0
    for j in range(i,n):
        if abs(arr[i]-arr[j])<=k:
            cnt+=1

    ans = max(ans,cnt)

print(ans)