n = int(input())

dir = {'E': 0,'W':1,'S':2,'N':3}
dx,dy = [0,0,1,-1],[1,-1,0,0]
nx,ny = 0,0
x,y = 0,0
cnt=0
check=0

for i in range(n):
    d,t = input().split()
    t = int(t)
    for j in range(t):
        nx,ny = dx[dir[d]],dy[dir[d]]
        x,y = x+nx,y+ny
        cnt+=1
        if x==0 and y==0:
            print(cnt)
            check=-1
            break
    if x==0 and y==0:
        break

if check!=-1:
    print(-1)