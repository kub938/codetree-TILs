n = int(input())
arr = list(map(int,input().split()))

sum_value = 0
max_value = 0
for i in range(n):
    sum_value += arr[i]
    if sum_value<0:
        sum_value = 0
        continue
    max_value = max(max_value,sum_value)
    
print(max_value)