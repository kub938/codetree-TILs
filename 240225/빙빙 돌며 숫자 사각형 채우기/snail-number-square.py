n, m = map(int, input().split())
sqr = [[0] * m for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
dx, dy = 0, 0
nx, ny = 0, 0

for i in range(1, n * m + 1):
    sqr[nx][ny] = i
    if not (in_range(nx + dxs[dx], ny + dys[dy])) or sqr[nx + dxs[dx]][ny + dys[dy]] != 0:
        dx, dy = (dx + 1) % 4, (dy + 1) % 4

    nx, ny = nx + dxs[dx], ny + dys[dy]

for elem in sqr:
    print(*elem)