n,k = tuple(map(int,input().split()))
arr = [0] * 101
k = 2*k+1
max_sum = 0

for _ in range(n):
    c,p = list(map(int,input().split()))
    arr[p]+= c

if k>len(arr):
    max_sum = sum(arr)
else:
    for i in range(len(arr)-k+1):
        max_sum = max(sum(arr[i:k+i]),max_sum)

print(max_sum)