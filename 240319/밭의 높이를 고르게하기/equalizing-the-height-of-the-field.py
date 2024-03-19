import sys

n,h,t = tuple(map(int,input().split()))
arr = list(map(int,input().split()))
h_diff = []

min_value = sys.maxsize

for i in range(n):
    h_diff.append(abs(arr[i]-h))

for i in range(n-t+1):
    sum_h = 0
    for j in range(i,i+t):
        sum_h += h_diff[j]
    min_value = min(sum_h,min_value)

print(min_value)