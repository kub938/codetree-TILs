n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

# def rect_size(x1, y1, x2, y2):
#     size = 0
#     if check(x1, y1, x2, y2): # 음수가 없다면
#         rect = [
#             board[i][j]
#             for i in range(x1, x2+1)
#             for j in range(y1, y2+1)
#         ]
#         size = len(rect)
#     return size

def check(x1,y1,x2,y2):
    size = 0
    if x1>x2:
        x1,x2=x2,x1
    elif y1>y2:
        y1,y2 = y2,y1
    cnt=0
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            if board[x][y]<=0:
                return False
            cnt+=1
    return cnt

ans = -1
s = 0
for i in range(n):
    for j in range(m):
        for k in range(n):
            for l in range(m):
                s = check(i,j,k,l)
                if s:
                    ans = max(s,ans)

print(ans)