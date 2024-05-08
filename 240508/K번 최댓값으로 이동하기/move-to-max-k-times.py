from collections import deque

n,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
x,y = map(int,input().split())
x,y = x-1,y-1
que = deque()
cnt = 0
dx,dy = [0,1,0,-1],[1,0,-1,0]


def in_range(x,y):
    return 0<=x<n and 0<=y<n

def bfs(x,y,cnt):
    if cnt==k:
        return x+1,y+1
    que.append([x,y])
    cnt+=1
    max_value = -1
    value = [[0]*n for _ in range(n)]
    max_num = board[x][y]
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if in_range(nx,ny) and board[nx][ny]<max_num and value[nx][ny]==0:
                que.append([nx,ny])
                value[nx][ny] = board[nx][ny]
                max_value = max(max_value,value[nx][ny])
    for i in range(n):
        for j in range(n):
            if value[i][j]==max_value:
                x,y = i,j
                return bfs(x,y,cnt)
    return x,y
                    

x,y = bfs(x,y,cnt)

print(x+1,y+1)