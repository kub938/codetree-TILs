n,t = map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(n)]

best = [[0,0] for _ in range(n)]
for i in range(n):
    k,s = arr[i]
    best[i] = s/k,i #1시간에 얻을 수 있는 효율


best.sort(key =lambda x:(x[0],x[1]),reverse = True)
ans = 0
time = 0

for i in range(n):
    time += arr[best[i][1]][0]
    if time>=t:
        break
    ans += arr[best[i][1]][1]

print(ans)