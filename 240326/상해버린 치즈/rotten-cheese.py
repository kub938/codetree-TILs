n,m,d,s = tuple(map(int,input().split())) #사람, 치즈, 치즈기록, 아픈기록

e = [list(map(int,input().split())) for _ in range(d)] 
#몇번째 사람p, 몇번째 치즈m, 언제 먹었는지t
ep = [e[i][0] for i in range(d)]
ec = [e[i][1] for i in range(d)]
et = [e[i][2] for i in range(d)]

a = [list(map(int,input().split())) for _ in range(s)]
ap = [a[i][0] for i in range(s)]
at = [a[i][1] for i in range(s)]
#몇번째 사람이 p, 언제 아팠는지 t

pill=0
che = [0]*(m+1)
tmp=[0]*(m+1)

for i in range(s):
    cnt=0
    for j in range(d):
        if  ap[i] == ep[j] and at[i] > et[j]:
            tmp[ec[j]]+=1
            
        for k in range(m+1):
            if tmp[k]==s:
                che[k]=1

che_idx = []
for i in range(len(che)):
    if che[i]>0:
        che_idx.append(str(i))

result = []
for j in range(len(che_idx)):
    check = [0]*(n+1)
    cnt=0
    for i in range(d):
        if che[ec[i]]==1 and str(ec[i]) == che_idx[j]:
            cnt+=1
    result.append(cnt)

print(max(result))