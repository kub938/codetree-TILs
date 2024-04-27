n,t = map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(n)]

best = [[0,0,0] for _ in range(n)]
for i in range(n):
    k,s = arr[i]
    best[i] = [s/k,i,k,s] #1시간에 얻을 수 있는 효율


best.sort(key =lambda x:(-x[0],x[2]))
ans = 0
time = 0

for i in range(n):
    if time+best[i][2]>t:
        continue
    else:
        ans += best[i][3]
        time += best[i][2]


print(ans)