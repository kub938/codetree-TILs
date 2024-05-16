def check(x,y):
    for i in range(y,y+m+1):
        if board[x][i]==1:
            return True
    return False

n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
x,y = 0,k-1

while 1:
    if check(x,y):
        for i in range(y,y+m):
                board[x][i]=1
        for e in board:
            print(*e)  
        break
    else:
        x+=1