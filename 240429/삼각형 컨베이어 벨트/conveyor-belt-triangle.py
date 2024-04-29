n,t = map(int,input().split())
c = [list(map(int,input().split())) for _ in range(3)]

for i in range(t):
    tmp = [c[2][-1],c[0][-1],c[1][-1]]
    for j in range(n-1,-1,-1):
        for k in range(3):
            c[k][j]=c[k][j-1]
    for k in range(3):
        c[k][0] = tmp[k]
        
for i in c:
    print(*i)