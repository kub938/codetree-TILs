n = int(input())

arr = [[0 for _ in range(n)]for _ in range(n)]
cnt=1
col = 0
row = 0

while 1:
    if row < n:
        arr[row][col] = cnt
        cnt+=1
        row+=1
    elif row == n:
        col+=1 
        row = 0
    if cnt>n*n:
        for i in arr:
            print(*i)
        break