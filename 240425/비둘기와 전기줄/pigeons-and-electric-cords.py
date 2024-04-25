n = int(input())
arr= [tuple(map(int,input().split())) for _ in range(n)]

line = [-1]*10
cnt=0


for n,l in arr:
    if line[n]==-1:
        line[n] = l
    elif line[n]==0 and l==1:
        cnt+=1
    elif line[n]==1 and l==0:
        cnt+=1

print(cnt)