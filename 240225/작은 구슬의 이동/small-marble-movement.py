n, t = map(int, input().split())
r, c, d = input().split()
x, y = int(r) - 1, int(c) - 1

area = [[0] * n for _ in range(n)]
area[x][y] = 1

dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]

dict = {'U': 0, 'R': 1, 'L': 2, 'D': 3}

dir = dict[d]

dx, dy = dxs[dir], dys[dir]  # 방향 설정


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


for i in range(t):
    if (not in_range(x+dx, y+dy)):
        dx, dy = dxs[abs(dir - 3)], dys[abs(dir - 3)]
    else:
        x += dx
        y += dy


print(x+1, y+1)

# 조건 : 부딪히면 방향을 뒤집음 , 이동시 이동한곳 = 1, 이전 자리 = 0