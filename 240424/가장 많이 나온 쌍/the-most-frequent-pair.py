n, m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in  range(m)]

for i in range(m):
    arr[i]=tuple(sorted(arr[i]))

ans = 0
arr= list(arr)

for i in range(m):
    cnt = arr.count(arr[i])
    ans = max(ans,cnt)

print(ans)