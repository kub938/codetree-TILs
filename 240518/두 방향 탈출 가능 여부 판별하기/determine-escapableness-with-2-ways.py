n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
stack = [[0,0]]
visited = [[0]*m for _ in range(n)]

def dfs():
    dx,dy = [0,1],[1,0]
    while stack:
        x,y = stack.pop()
        for i in range(2):
            nx,ny = x+dx[i],y+dy[i]
            if in_range(nx,ny) and board[nx][ny]==1 and visited[nx][ny]==0:
                stack.append([nx,ny])
                visited[nx][ny]=1

def in_range(x,y):
    return 0<=x<n and 0<=y<m

dfs()

print(visited[n-1][m-1])