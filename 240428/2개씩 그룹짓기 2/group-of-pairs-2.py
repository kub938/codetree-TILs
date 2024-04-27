import sys

n = int(input())
arr = list(map(int,input().split()))
min_diff = sys.maxsize

arr.sort()
for i in range(n):
    min_diff = min(abs(arr[i]-arr[i+n]),min_diff)

print(min_diff)