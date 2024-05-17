n,m = map(int,input().split())
arr = list(map(int,input().split()))

ans = 0
for i in range(n):
    idx = arr[i]-1
    sum_value = 0
    for j in range(m):
        sum_value += arr[idx]
        idx = arr[idx]-1
    ans = max(ans, sum_value)
print(ans)