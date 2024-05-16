def move(x,y):
    global ans
    dxs,dys = [-1,1,0,0],[0,0,-1,1]
    max_pos = []
    for i in range(4):
        max_value=board[x][y]
        nx,ny = x+dxs[i],y+dys[i]
        if in_range(nx,ny) and board[nx][ny]>max_value:
            ans.append(board[nx][ny])
            move(nx,ny)
            return

def in_range(x,y):
    return 0<=x<n and 0<=y<n
n,x,y = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
ans = [board[x-1][y-1]]
move(x-1,y-1)

print(*ans)