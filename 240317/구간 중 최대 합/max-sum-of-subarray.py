import sys

n,k = map(int,input().split())
arr= list(map(int,input().split()))
max_sum = -sys.maxsize
sum_arr = 0 

for i in range(n-k+1):
    for j in range(k):
        sum_arr += arr[i+j]
    max_sum = max(max_sum,sum_arr)
    sum_arr = 0

print(max_sum)