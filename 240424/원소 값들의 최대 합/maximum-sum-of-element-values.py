n, m =map(int,input().split())

arr = list(map(int,input().split()))
ans = 0
max_ans = 0
for i in range(n):
    next_idx = arr[i]-1
    for j in range(m):
        ans+=next_idx+1
        next_idx = arr[next_idx]-1
    max_ans = max(max_ans,ans)
    ans=0
print(max_ans)