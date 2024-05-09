from itertools import combinations

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
line = []
for i in range(1,n+1):
    for c in combinations(arr,i):
        line.append(list(c))


ans = 0
for i in line:
    check = True
    for j in range(len(i)):
        for k in range(len(line[j])):
            if len(line[k])>1:
                if line[k][1]>=line[k+1][0]:
                    check = False
    if check:
        ans = max(ans, len(i))

print(ans)