n,m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
cnt = 0
ans = 0

def in_range(x,y):
    return 0<=x<n and 0<=y<m

dxs,dys = [-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1] #북쪽부터
nx,ny = 0,0

for x in range(n):
    for y in range(m):
        if arr[x][y] =='L':
            for k in range(8):
                for l in range(1,3):
                    nx,ny = x+dxs[k]*l,y+dys[k]*l
                    if in_range(nx,ny) and arr[nx][ny]=='E':
                        
                        cnt+=1
                    if cnt==2:
                        ans+=1
                cnt=0

print(ans)