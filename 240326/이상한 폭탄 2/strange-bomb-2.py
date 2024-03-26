n,k = tuple(map(int,input().split()))
arr = [int(input()) for _ in range(n)]

tmp = []
max_n = -1

for i in range(n-k+1):
    for j in range(i+1,n):
        target = arr[i]
        if target==arr[j]:
            max_n = max(max_n,arr[j])

print(max_n)