a,b = map(int,input().split())

arr_a = []
arr_b = []
leader = 0
pos = 0
change_cnt = 0
for i in range(a):
    v,t = map(int,input().split())
    for j in range(t):
        pos+=v
        arr_a.append(pos)

pos=0
for i in range(b):
    v,t = map(int,input().split())
    for j in range(t):
        pos+=v
        arr_b.append(pos)

if arr_a[0]<arr_b[0]:
    leader=2
else:
    leader=1

for i in range(len(arr_a)):
    if leader==1 and arr_b[i]>arr_a[i]:
        leader=2
        change_cnt+=1
    elif leader ==2 and arr_b[i]<arr_a[i]:
        leader=1
        change_cnt+=1

print(change_cnt)