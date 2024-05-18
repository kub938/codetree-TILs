n = int(input())
arr = list(map(int,input().split()))

max_value = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            max_value = max(max_value,arr[i]*arr[j]*arr[k])

print(max_value)