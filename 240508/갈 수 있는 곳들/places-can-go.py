from collections import deque

n,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
k=[list(map(int,input().split())) for _ in range(K)]
dis = [[0]*n for _ in range(n)]

que = deque()
dx,dy = [0,1,0,-1],[1,0,-1,0]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def bfs(x,y):
    que.append([x-1,y-1])
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if in_range(nx,ny) and board[nx][ny]==0 :
                que.append([nx,ny])
                dis[nx][ny]=1

for x,y in k:
    bfs(x-1,y-1)

ans = 0

if n==1:
    print(1)
else:
    for i in range(n):
        for j in range(n):
            if dis[i][j]==1:
                ans+=1
    print(ans)