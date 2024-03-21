import sys

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
min_area = sys.maxsize

for i in range(n):
    min_x,min_y = 40000,40000
    max_x,max_y = 0,0

    for j in range(n):
        if i==j:
            continue
        x,y = arr[j]
        min_x,min_y = min(min_x,x),min(min_y,y)
        max_x,max_y = max(max_x,x),max(max_y,y)
    min_area = min(min_area,(max_x-min_x)*(max_y-min_y))

print(min_area)