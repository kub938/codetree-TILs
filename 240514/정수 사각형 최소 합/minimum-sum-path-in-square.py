n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
sum_b = [[0]*n for _ in range(n)]
sum_b[0][n-1] = board[0][n-1]

for i in range(n-2,-1,-1):
    sum_b[0][i] = board[0][i]+sum_b[0][i+1]
for i in range(1,n):
    sum_b[i][n-1]= board[i][n-1]+sum_b[i-1][n-1]


for i in range(1,n):
    for j in range(n-2,-1,-1):
        sum_b[i][j]= min(board[i][j]+sum_b[i-1][j],board[i][j]+sum_b[i][j+1])

print(sum_b[n-1][0])