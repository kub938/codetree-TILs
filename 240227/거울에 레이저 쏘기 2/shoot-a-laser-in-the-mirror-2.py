n = int(input())
arr = [input().split() for _ in range(n)]
k = int(input())

# Initial position and direction setup
init_pos_dir = [(0, k % n - 1, 'D'), (k % n - 1, n - 1, 'L'), (n - 1, k % n - 1, 'U'), (k % n - 1, 0, 'R'), (0, 0, 'R')]
x, y, now_dir = init_pos_dir[k // n] if k % n != 0 else init_pos_dir[k // n - 1]

dir_xy = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
change_dir1 = {'U': 'L', 'D': 'R', 'L': 'U', 'R': 'D'}
change_dir2 = {'U': 'R', 'D': 'L', 'L': 'U', 'R': 'D'}

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

visit = [[[0]*n for _ in range(n)] for _ in range(4)]  # 3D list for memoization
dir_num = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
cnt = 0

while in_range(x, y):
    if visit[dir_num[now_dir]][x][y] > 0:  # if this position and direction is visited before
        cnt = -1  # means it is in infinite loop
        break
    visit[dir_num[now_dir]][x][y] = 1  # mark as visited
    if arr[x][0][y] == '\\':
        now_dir = change_dir1[now_dir]  # 다시 반사
    elif arr[x][0][y] == '/':
        now_dir = change_dir2[now_dir]
    dx, dy = dir_xy[now_dir]  # 방향에 따른 x,y값 설정
    x, y = x + dx, y + dy  # 반사된 방향으로 전진
    cnt += 1

print(cnt)