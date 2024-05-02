n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
r,c = map(int,input().split())
r,c = r-1,c-1
tmp = [[] for _ in range(n)]

def boom():
    b_n = arr[r][c]
    arr[r][c]=0
    for i in range(1,b_n):
        arr[r+i][c] = 0
        arr[r-i][c] = 0
        arr[r][c+i] = 0
        arr[r][c-i] = 0

def boom_sort():
    for i in range(n):
        for j in range(n):
            if arr[j][i]!=0:
                tmp[i].append(arr[j][i])
    for i in range(n):
        for j in range(n-len(tmp[i])):
            tmp[i].insert(0,0)
    
    
boom()
boom_sort()

for c in range(n):
    for r in range(n):
        print(tmp[r][c],end=" ")
    print()