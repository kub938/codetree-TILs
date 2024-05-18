import sys

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

max_value = sys.maxsize
for i in range(n):
    max_value = min(max_value,arr[n+i]-arr[i])

print(max_value)