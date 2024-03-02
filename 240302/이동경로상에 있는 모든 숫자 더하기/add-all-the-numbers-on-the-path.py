n,t = map(int,input().split())
com = input()
arr = [list(map(int,input().split())) for _ in range(n)]

x,y,nx,ny = n//2,n//2,0,0
dxs,dys = [-1,0,1,0],[0,1,0,-1] #URDL
dir_num = 0
ans = arr[x][y]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

for c in com:
    if c=='L':
        dir_num=(dir_num+3)%4
    elif c=='R':
        dir_num=(dir_num+1)%4
    else:
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        if in_range(nx, ny):
            x,y = x+dxs[dir_num],y+dys[dir_num]
            ans=ans+arr[x][y]

print(ans)