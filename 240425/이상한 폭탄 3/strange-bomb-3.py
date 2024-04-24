n,k = map(int,input().split())
arr = [int(input()) for _ in range(n)]

booms = []
for i in range(n):
    target = arr[i]
    boom = arr[i+1:i+1+k].count(target)
    if boom>0:
        booms.append([boom,target])

ans = 0
max_value = 0
for i in range(len(booms)):
    if booms[i][0]>max_value:
        max_value=booms[i][0]
        ans=booms[i][1]
    if booms[i][0]==max_value:
        max(ans,booms[i][1])

print(ans)