n = int(input())
arr= [list(map(int,input().split())) for _ in range(n)]

arr.sort()
min_diff = arr[1][0]-arr[0][0]
arr.sort(key=lambda x:x[1])
max_diff = arr[-1][1]-arr[-2][1]

if min_diff<=max_diff:
    arr.pop()
else:
    arr.sort()
    del arr[0]

min_x = 200
max_x = 0
for i in arr:
    min_x = min(min_x,i[0])
    max_x = max(max_x,i[1])

print(max_x-min_x)