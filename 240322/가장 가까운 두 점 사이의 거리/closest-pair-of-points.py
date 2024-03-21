import sys

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
min_dis = sys.maxsize

for i in range(n-1):
    for j in range(i+1,n):
        x,y = arr[i]
        x2,y2 = arr[j]
        dis = (x-x2)*(x-x2)+(y-y2)*(y-y2)
        min_dis = min(min_dis,dis)

print(min_dis)