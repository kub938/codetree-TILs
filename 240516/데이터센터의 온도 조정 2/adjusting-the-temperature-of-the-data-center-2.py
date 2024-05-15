n,c,g,h = map(int,input().split())

t = [list(map(int,input().split())) for _ in range(n)] 
arr = [0]*2001
max_idx = 0
for ta,tb in t:
    for i in range(ta,tb+1):
        arr[i]+=1

target = arr.index(max(arr))

ans = 0
for ta,tb in t:
    if ta<=target<=tb:
        ans+=g
    elif target<ta:
        ans+=c
    elif target>tb:
        ans+=h

print(ans)