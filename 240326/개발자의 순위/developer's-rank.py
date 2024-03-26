k,n = map(int,input().split())
cnt = [[1]*n]*n

for i in range(k):
    arr = list(map(int,input().split()))
    arr.reverse()
    for j in range(i+1,n):
        main = arr[i]-1
        elem = arr[j]-1
        cnt[main][elem]=0

ans = 0
for i in range(n):
    ans += cnt[i].count(1)

print(ans)