# 조건1 범위 밖이거나 칸이 0이 아니면 꺾음
# 조건2 A:65, Z:90  = 90 이상일시 (n%91+65)

n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
nx, ny = 0, 0
x, y = 0, 0
dir_num = 0
chr_num = 66
arr[0][0] = 'A'

def in_range(x,y):
    return 0<=x<n and 0<=y<m

for _ in range(n * m-1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    x, y = x + dxs[dir_num], y + dys[dir_num]
    if chr_num>90:
        chr_num=chr_num % 91 + 65
    arr[x][y] = chr(chr_num)
    chr_num += 1

for elem in arr:
    print(*elem)