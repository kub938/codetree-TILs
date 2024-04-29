n,m,Q = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

q = [list(input().split()) for _ in range(Q)]



def r_shift(i):  # <-  왼쪽으로 밀기
    tmp = arr[i][0]
    for j in range(m-1):
        arr[i][j] = arr[i][j+1]
    arr[i][-1] = tmp
    
def l_shift(i):
    tmp = arr[i][-1]
    for j in range(m-1,0,-1):
        arr[i][j] = arr[i][j-1]
    arr[i][0] = tmp

def u_check(floor,u_dir_num):
    check = False
    for i in range(floor,0,-1):
        for j in range(m):
            if arr[i][j]==arr[i-1][j]:
                check = True
                if u_dir_num==1:
                    r_shift(i-1)
                    u_dir_num = 2
                else:
                    l_shift(i-1)
                    u_dir_num = 1
                break
        if not check:
            break
def d_check(floor,d_dir_num):
    check = False
    for i in range(floor,n-1):
        for j in range(m):
            if arr[i][j]==arr[i+1][j]:
                check = True
                if d_dir_num==1:
                    r_shift(i+1)
                    d_dir_num = 2
                else:
                    l_shift(i+1)
                    d_dir_num = 1
                break
        if not check:
            break

for c in range(Q): #case
    floor = int(q[c][0])-1
    if q[c][1]=='L':
        u_dir_num = 1 #왼쪽 1, 오른쪽 2
        d_dir_num = 1
        l_shift(floor)
    else:
        u_dir_num = 2
        d_dir_num = 2
        r_shift(floor)
        
    u_check(floor,u_dir_num)
    d_check(floor,d_dir_num)

for e in arr:
    print(*e)