a, b = map(int, input().split())
a_pos = []
b_pos = []
now_pos = 0

for i in range(a):
    d, t = input().split()
    t = int(t)
    if d == 'R':
        for j in range(t):
            now_pos += 1
            a_pos.append(now_pos)
    elif d == "L":
        for j in range(t):
            now_pos -= 1
            a_pos.append(now_pos)

now_pos = 0

for i in range(b):
    d, t = input().split()
    t = int(t)
    if d == 'R':
        for j in range(t):
            now_pos += 1
            b_pos.append(now_pos)
    elif d == "L":
        for j in range(t):
            now_pos -= 1
            b_pos.append(now_pos)


answer = -1
for i in range(1,len(a_pos)):
    if a_pos[i]==b_pos[i]:
        answer=i+1
        break

print(answer)