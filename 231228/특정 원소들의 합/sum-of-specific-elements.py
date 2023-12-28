arr = [list(map(int,input().split()))for _ in range(4)]

row,col = 0,0
tmp = 0
while 1:
    for i in range(col+1):
        tmp+=arr[row][i]
    row+=1
    col+=1

    if col==4:
        print(tmp)
        break