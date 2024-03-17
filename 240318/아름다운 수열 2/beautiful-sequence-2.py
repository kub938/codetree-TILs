n,m = map(int,input().split())
a = input().split()
b = input().split()
a = "".join(a)
bnum_arr = []
cnt = 0 

for i in range(m):
    for j in range(m):
        for k in range(m):
            if i!=j and j!=k and i!=k:
                bnum_arr.append(b[i]+b[j]+b[k])

for elem in bnum_arr:
    if elem in a:
        cnt+=1

print(cnt)