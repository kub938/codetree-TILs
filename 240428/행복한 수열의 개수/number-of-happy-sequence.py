n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

def happy_arr():
    cnt = 0
    for r in range(n):
        if w_check(r):
            cnt+=1

    for c in range(n):
        if h_check(c):
            cnt+=1
    return cnt

def w_check(r):
    cnt = 1
    for c in range(n-1):
        if arr[r][c]==arr[r][c+1]:
            cnt+=1
        else:
            cnt=1
        if cnt==m:
            return True

def h_check(c):
    cnt = 1
    for r in range(n-1):
        if arr[r][c]==arr[r+1][c]:
            cnt+=1
        else:
            cnt=1
        if cnt==m:
            return True


print(happy_arr())