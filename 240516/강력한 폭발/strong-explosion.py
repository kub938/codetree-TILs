def solved(m):
    global ans

    if m==0:
        ans = max(boom(bombs),ans)
        return
    
    for i in range(3):
        bombs.append(i)
        solved(m-1)
        bombs.pop()

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def boom(bombs):
    bomb_shapes = [
          [[2,0],[1,0],[0,0],[-1,0],[-2,0]],
        [[1,0],[0,1],[0,0],[-1,0],[-1,-1]],
          [[-1,-1],[-1,1],[0,0],[1,1],[1,-1]]
    ]

    max_cnt = 0
    for i in bombs:
        dis = [[0]*n for _ in range(n)]
        cnt=0
        for x,y in target:
            for j in range(5):
                nx,ny = x+bomb_shapes[i][j][0],y+bomb_shapes[i][j][1]
                if in_range(nx,ny) and dis[nx][ny]==0:
                    dis[nx][ny]=1
                    cnt+=1
        max_cnt = max(max_cnt,cnt)
    return max_cnt
        

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
target = []
bombs = []
ans = 0

t_cnt = 0
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            target.append([i,j])
            t_cnt+=1

solved(t_cnt)

print(ans)