import sys 


arr = list(map(int,input().split()))
n = len(arr)
sum_arr = sum(arr)
min_value = sys.maxsize

for i in range(n):
    for j in range(i,n):
        for k in range(j,n):
            sum1 = arr[i]+arr[j]+arr[k]
            sum2 = sum_arr-(arr[i]+arr[j]+arr[k])
            min_value = min(min_value,abs(sum1-sum2))

print(min_value)