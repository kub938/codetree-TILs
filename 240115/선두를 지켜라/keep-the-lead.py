n,m = map(int,input().split())

a_pos = []
b_pos = []

now_pos = 0

for i in range(n):
    v,t = map(int,input().split())
    for j in range(t):
        now_pos+=v
        a_pos.append(now_pos)


now_pos = 0
for i in range(m):
    v,t = map(int,input().split())
    for j in range(t):
        now_pos+=v
        b_pos.append(now_pos)


leader,ans = 0,0
for i in range(1,len(a_pos)):
    if a_pos[i] > b_pos[i]:
        if leader ==2:
            ans+=1
        
        leader = 1
    elif a_pos[i] < b_pos[i]:
        if leader ==1:
            ans+=1

        leader = 2

print(ans)