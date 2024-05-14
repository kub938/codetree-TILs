n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
sum_line = [[0]*n for _ in range(n)]
sum_line[0][0] = board[0][0]

for i in range(1,n):
    sum_line[0][i]=sum_line[0][i-1]+board[0][i]
    sum_line[i][0]=sum_line[i-1][0]+board[i][0]


for i in range(1,n):
    for j in range(1,n):
        sum_line[i][j] = max(sum_line[i][j-1]+board[i][j],sum_line[i-1][j]+board[i][j],sum_line[i][j])

print(sum_line[n-1][n-1])