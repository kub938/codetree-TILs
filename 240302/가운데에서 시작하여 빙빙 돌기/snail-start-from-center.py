n = int(input())
arr = [[0]*n for _ in range(n)]

dxs,dys = [0,-1,0,1],[-1,0,1,0]
nx,ny,x,y,dir_num, = 0,0,n-1,n-1,0
arr[n-1][n-1] = n*n

def in_range(x,y):
    return 0<=x<n and 0<=y<n

for i in range(n*n-1,0,-1):
    nx,ny = x+dxs[dir_num],y+dys[dir_num]
    if not in_range(nx,ny) or arr[nx][ny]!=0:
        dir_num=(dir_num+1)%4
    x,y = x+dxs[dir_num], y+dys[dir_num]
    arr[x][y] = i

for elem in arr:
    print(*elem)