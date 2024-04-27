import sys

n = int(input())
arr = list(map(int,input().split()))

max_value= -sys.maxsize
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            max_value = max(max_value,arr[i]*arr[j]*arr[k])
    

print(max_value)