n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

line = [0]*101
check = False

for a in arr:
    for j in range(a[0],a[1]+1):
        line[j]+=1


for a in arr:
    for j in range(a[0],a[1]+1):
        line[j]-=1
        if n-1 in line:
            check = True
            break
    for j in range(a[0],a[1]+1):
        line[j]+=1


if check:
    print('Yes')
else:
    print('No')