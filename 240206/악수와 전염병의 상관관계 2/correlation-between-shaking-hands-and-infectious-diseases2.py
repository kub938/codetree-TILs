N, K, P, T = map(int, input().split())
t_arr = []

dev = [[0, 0] for _ in range(N+1)]
dev[P][0] = 1
dev[P][1] = K

for i in range(T):
    t, x, y = map(int, input().split())
    t_arr.append([t, x, y])

t_arr.sort()

for i in t_arr:
    x=i[1]
    y=i[2]
    if dev[x][0] == 1 or dev[y][0] == 1 and dev[x][1] > 0 or dev[y][1] > 0:
        if dev[x][1]==0 and dev[y][1]==0:
            break
        elif dev[x][0] == dev[y][0]:
            dev[x][1] -= 1
            dev[y][1] -= 1
        elif dev[x][0] == 1:
            dev[x][1] -= 1
            dev[y][0] = 1
            dev[y][1] = K
        elif dev[y][0] == 1:
            dev[y][1] -= 1
            dev[x][0] = 1
            dev[x][1] = K

for i in range(N):
    print(dev[i+1][0],end="")