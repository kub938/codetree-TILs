from collections import deque

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dis = [[0]*m for _ in range(n)]
que = deque()
que.append([0,0])

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs():
    dx,dy = [0,1,0,-1],[1,0,-1,0]
    for i in range(n):
        while que:
            x,y = que.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if in_range(nx,ny) and board[nx][ny]==1 and dis[nx][ny]==0:
                    dis[nx][ny] = dis[x][y]+1
                    que.append([nx,ny])

bfs()

if dis[n-1][m-1]==0:
    print(-1)
else:
    print(dis[n-1][m-1])