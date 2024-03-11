import sys

min_value = sys.maxsize

n = int(input())
arr = map(int,input().split())
cnt=0

for elem in arr:
    if elem<min_value:
        min_value = elem
        cnt=0
        cnt+=1
    elif elem==min_value:
        cnt+=1

print(min_value,cnt)