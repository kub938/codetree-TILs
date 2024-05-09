from collections import deque
from itertools import combinations
import copy

n,k,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

dx,dy = [0,1,0,-1],[1,0,-1,0]
cnt=0
que = deque()

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def bfs(board,x,y):
    cnt=0
    dis[x][y]=1
    que.append([x,y])
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if in_range(nx,ny) and dis[nx][ny]==0 and board[nx][ny]==0:
                que.append([nx,ny])
                dis[nx][ny]= 1


stone_pos = []
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            stone_pos.append([i,j])

max_value = 0
start_point = [list(map(int,input().split())) for _ in range(k)]

if m>0:
    for comb in combinations(stone_pos,m):
        copy_board = copy.deepcopy(board)
        for i in comb:
            x,y = i
            copy_board[x][y]=0

        dis = [[0] * n for _ in range(n)]
        cnt=0
        for j in start_point:
            r,c = j
            r,c = r-1,c-1
            bfs(copy_board,r,c)
        for i in range(n):
            for j in range(n):
                if dis[i][j] == 1:
                    cnt += 1

        max_value = max(cnt,max_value)
else:
    dis = [[0] * n for _ in range(n)]
    for j in start_point:
        r, c = j
        r, c = r - 1, c - 1
        bfs(board,r,c)
    for i in range(n):
        for j in range(n):
            if dis[i][j] == 1:
                max_value += 1

print(max_value)