n,s = map(int,input().split())
arr = list(map(int,input().split()))

sum_value = sum(arr)
min_value = 10000
for i in range(n-1):
    for j in range(i+1,n):
        min_value = min(abs(s-(sum_value - arr[i]-arr[j])),min_value)

print(min_value)