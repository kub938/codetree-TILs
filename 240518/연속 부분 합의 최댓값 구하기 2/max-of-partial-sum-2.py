n = int(input())
arr = list(map(int,input().split()))

sum_value = 0
max_value = -1000
for i in range(n):
    sum_value += arr[i]
    max_value = max(max_value,sum_value)
    if sum_value<0:
        sum_value = 0
        continue

    
print(max_value)