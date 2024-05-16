n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

def col_search(x,y):
    for c in range(y,m):
        if board[x][c]<0:
            return c-1    #음수 만나면 그 col값 반환
    return c

def row_search(x,y):
    for r in range(x,n):
        if board[r][y]<0:
            return r-1
    return r

ans = 0
for x in range(n):
    for y in range(m):
        if board[x][y]>0:
            ny,nx = col_search(x,y),row_search(x,y)
            result=0
            for i in range(x,nx+1):
                cnt=0
                for j in range(y,ny+1):
                    if board[i][j]<0:
                        break
                    cnt+=1
                if board[i][j]<0:    
                    break
                else:
                    result+=cnt
            ans = max(result,ans)
    if ans==n*m:
        break
print(ans)