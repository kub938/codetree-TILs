n = int(input())
arr = [[0]*201 for _ in range(201)]
for i in range(1,n+1):
    x1,y1,x2,y2 = map(int,input().split())
    if i%2!=0: #빨간색
        for j in range(x1,x2):
            for k in range(y1,y2):
                arr[j][k]=-1
    else:
        for j in range(x1,x2):
            for k in range(y1,y2):
                arr[j][k]=1

ans=0
for a in arr:
    for e in a:
        if e==1:
            ans+=1

print(ans)