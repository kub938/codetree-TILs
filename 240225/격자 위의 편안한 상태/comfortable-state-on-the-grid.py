n, m = map(int, input().split())
arr = [[0] * n for _ in range(n)]

global x, y
global dxs, dxy
x, y = 0, 0
dxs, dxy = [-1, 1, 0, 0], [0, 0, -1, 1]


def check_state(r, c):
    cnt = 0
    for dx, dy in zip(dxs, dxy):
        x, y = dx + r, dy + c
        if 0 <= x < n and 0 <= y < n and arr[x][y] == 1:
            cnt += 1
    if cnt == 3:
        return 1
    else:
        return 0


for i in range(m):
    r, c = map(int, input().split())
    r, c = r - 1, c - 1
    arr[r][c] = 1
    answer = check_state(r, c)
    print(answer)