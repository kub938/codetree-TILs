n = int(input())
t_case = [list(input().split()) for _ in range(n)]
arr= [0]*2001
#검은색 = 1 흰색 = -1
now_pos = 20
for m,d in t_case:
    m = int(m)
    if d=='L':
        for i in range(m):
            arr[now_pos]=-1
            now_pos-=1 
        now_pos+=1
    else:
        for i in range(m):
            arr[now_pos]=1
            now_pos+=1
        now_pos-=1
print(arr.count(-1),arr.count(1))