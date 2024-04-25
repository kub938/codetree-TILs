n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
min_x,max_x = 101,0



check = True

x1,x2 = arr[0][0],arr[0][1]
for i in range(1,n):
    x3,x4 = arr[i][0],arr[i][1]
    if x2<x3 or x4<x1:
        check = False
        break
    x1,x2 = min(x1,x3),min(x2,x4)

if check:
    print('Yes')
else:
    print('No')