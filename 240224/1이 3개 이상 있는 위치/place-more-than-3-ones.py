n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

dxs,dys = [-1,0,1,0],[0,1,0,-1]
x,y = 0,0
cnt = 0
result = 0
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n


for i in range(n):
    for j in range(n):
        for dx,dy in zip(dxs,dys):  
            nx, ny = i+dx,j+dy
            if in_range(nx,ny) and arr[nx][ny] ==1:
                cnt+=1
        if cnt>=3:
            result+=1
        cnt=0
    
print(result)