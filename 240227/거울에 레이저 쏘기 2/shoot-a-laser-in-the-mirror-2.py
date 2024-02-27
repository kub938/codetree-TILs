n = int(input())
arr = [input().split() for _ in range(n)]
k = int(input())
dx, dy = 0, 0
x, y = 0, 0
now_dir = 0
dir = 0
cnt = 0

if k // n == 0:
    x, y = 0, k % n - 1
    now_dir = 'D'
elif k // n == 1:
    if k%n==0:
        x, y = 0, n-1
        now_dir = 'D'
    else:
        x, y = k % n - 1, n - 1
        now_dir = 'L'
elif k // n == 2:
    if k%n==0:
        x, y = n-1, n - 1
        now_dir = 'L'
    else:
        x, y = n - 1, k % n - 1
        now_dir = 'U'
elif k // n == 3:
    if k%n==0:
        x, y = n - 1, 0
        now_dir = 'U'
    else:
        x, y =  n-1, 0
        now_dir = 'R'
elif k// n ==4:
    x,y = 0,0
    now_dir ='R'

mirx1, miry1 = [-1, 1, 0, 0], [0, 0, -1, 1]  # \\\\
mirx2, miry2 = [1, -1, 0, 0], [0, 0, -1, 1]  # ////
change_dir1 = {'U': 'L', 'D': 'R', 'L': 'U', 'R': 'D'}
change_dir2 = {'U': 'R', 'D': 'L', 'L': 'U', 'R': 'D'}
dir_num = {'U': 0, 'D': 1, 'L': 2, 'R': 3}


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

while 1:
    if not in_range(x, y):
        break
    if arr[x][0][y] == '\\':
        now_dir = change_dir1[now_dir]  # 다시 반사
        dir = dir_num[now_dir]
        dx, dy = mirx1[dir], miry1[dir]  # 방향에 따른 x,y값 설정
    elif arr[x][0][y] == '/':
        now_dir = change_dir2[now_dir]
        dir = dir_num[now_dir]
        dx, dy = mirx2[dir], miry2[dir]  # 방향에 따른 x,y값 설정
    x, y = x + dx, y + dy  # 반사된 방향으로 전진
    cnt += 1



print(cnt)

# cross_x=['L','R','U','D']
# cross_y=['R','L','U','D']