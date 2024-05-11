from collections import deque
import copy

n,m=map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

que = deque()

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs():
    global board
    dis = [[0]*m for _ in range(n)]
    dx,dy = [0,1,0,-1],[1,0,-1,0]
    que.append([0,0])
    tmp = copy.deepcopy(board)
    melt = 0
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if in_range(nx,ny):
                if board[nx][ny]==1:
                    tmp[nx][ny]=0
                    melt+=1
                elif board[nx][ny]==0 and dis[nx][ny]==0:
                    dis[nx][ny]=1
                    que.append([nx,ny])
        board = copy.deepcopy(tmp)
    return melt



time = 0
for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            time+=1
            melt_cnt = bfs()

print(time,melt_cnt)