n,m = map(int,input().split())

a = []
b = []
same_cnt=0
now_pos = 0

for i in range(n):
    t,d = input().split()
    t = int(t)
    if d=='L':
        for j in range(t):
            now_pos-=1  
            a.append(now_pos)
    else:
        for j in range(t):
            now_pos+=1
            a.append(now_pos)

now_pos = 0

for i in range(m):
    t,d = input().split()
    t = int(t)
    if d=='L':
        for j in range(t):
            now_pos-=1  
            b.append(now_pos)
    else:
        for j in range(t):
            now_pos+=1
            b.append(now_pos)


min_ab = min(len(a),len(b))
max_ab = max(len(a),len(b))

for i in range(1,min_ab):
    if a[i-1] == b[i-1]:
        continue
    else:
        if a[i] == b[i]:
            same_cnt+=1

for i in range(min_ab,max_ab):
    if min_ab == len(a):
        if a[-1] == b[i-1]:
            continue
        else:
            if a[-1] == b[i]:
                same_cnt+=1
    else:
        if a[i-1] == b[-1]:
            continue
        else:
            if a[i] == b[-1]:
                same_cnt+=1



print(same_cnt)