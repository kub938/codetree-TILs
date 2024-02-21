# 동시, a, b일경우 3경우
n,m = map(int,input().split())

a_arr = []
b_arr = []
fir = 0
cnt = 1
a_move = 0
b_move = 0

for i in range(n):
    v,t = map(int,input().split())
    for T in range(t):
        a_move+=v
        a_arr.append(a_move)

for i in range(m):
    v,t = map(int,input().split())
    for T in range(t):
        b_move+=v
        b_arr.append(b_move)

if a_arr[0]>b_arr[0]:
    fir = 1
elif a_arr[0]<b_arr[0]:
    fir = 2
else:
    fir = 0

for i in range(len(a_arr)):
    if fir!=0 and a_arr[i]==b_arr[i]:
        cnt+=1
        fir=0
    elif fir!=2 and a_arr[i]<b_arr[i]:
        cnt+=1
        fir=2
    elif fir!=1 and a_arr[i]>b_arr[i]:
        cnt+=1
        fir=1

print(cnt)