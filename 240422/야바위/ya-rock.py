n = int(input())
tc = [list(map(int,input().split())) for _ in range(n)]

ans = []
for t in range(n):
    score = 0
    arr = [0]*3
    arr[t] = 1
    for i in range(n):
        a,b,c = tc[i][0]-1,tc[i][1]-1,tc[i][2]-1
        arr[a],arr[b] =arr[b],arr[a]
        score += arr[c]
    ans.append(score)

print(max(ans))