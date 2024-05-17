n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

def check(x1,y1,x2,y2):
    size = 0
    if  0<=x1<n and 0<=x2<n and 0<=y1<m and 0<=y2<m:
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if board[i][j]<=0:
                    return
        return abs(x2-x1+1)*abs(y2-y1+1)
                

ans =0 
for i in range(n):
    for j in range(m):
        for k in range(n):
            for l in range(m):
                ans = max(check(i,j,k,l),ans)

print(ans)