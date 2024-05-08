from collections import deque

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
que = deque()
que.append([0,0])

dis = [[0]*m for _ in range(n)]
dx,dy = [0,1,0,-1],[1,0,-1,0]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs():
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if nx==n-1 and ny==m-1:
                return True
            if in_range(nx,ny) and board[nx][ny]==1 and dis[nx][ny]==0:
                que.append([nx,ny])
                dis[nx][ny]= dis[x][y]+1
    return False

if bfs():
    print(1)
else:
    print(0)