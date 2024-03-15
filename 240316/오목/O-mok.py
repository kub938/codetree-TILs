board = [list(map(int,input().split())) for _ in range(19)]

cnt = 0
num = 0
winner = 0
winpos = []
for i in range(19):
    for j in range(14):
        if board[i][j]!=0:
            num = board[i][j]
            for k in range(5):
                if num==board[i][j+k]:
                    cnt+=1
                else:
                    cnt=0 
                if cnt==5:
                    winner=num
                    winpos.append(i+1)
                    winpos.append(j+k-1)
                    break
            cnt=0
for i in range(14):
    for j in range(19):
            for k in range(5):
                if num==board[i+k][j]:
                    cnt+=1 
                else:
                    cnt=0 
                if cnt==5:
                    winner=num
                    winpos.append(i+k-1)
                    winpos.append(j+1)
                    break
            cnt=0
for i in range(14):
    for j in range(14):
            for k in range(5):
                if num==board[i+k][j+k]:
                    cnt+=1 
                else:
                    cnt=0 
                if cnt==5:
                    winner=num
                    winpos.append(i+k-1)
                    winpos.append(j+k-1)
                    break
            cnt=0
for i in range(14):
    for j in range(14):
            for k in range(5):
                if j>4 and num==board[i+k][j-k]:
                    cnt+=1 
                else:
                    cnt=0 
                if cnt==5:
                    winner=num
                    winpos.append(i+3)
                    winpos.append(j-1)
                    break

print(winner)
print(*winpos)