n = int(input())
arr= [list(map(int,input().split())) for _ in range(n)]


arr.sort(key=lambda x:x[1])

cnt=0
last_e = -1
for s,e in arr:
    if last_e<=s:
        last_e = e
        cnt+=1
        

print(n-cnt)