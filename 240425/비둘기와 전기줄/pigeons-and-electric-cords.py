n = int(input())
arr= [tuple(map(int,input().split())) for _ in range(n)]

line = [-1]*11
cnt=0


for p,l in arr:
    if line[p]==0 and l==1:
        cnt+=1
    elif line[p]==1 and l==0:
        cnt+=1
    line[p] = l

print(cnt)