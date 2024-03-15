import sys

n = int(input())
arr = list(map(int,input().split()))
max_value = -sys.maxsize 

for i in range(n-2):
    for j in range(i+2,n):
        max_value = max(max_value, arr[i]+arr[j])

print(max_value)