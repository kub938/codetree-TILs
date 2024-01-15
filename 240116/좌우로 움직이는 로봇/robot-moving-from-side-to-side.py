n, m = map(int, input().split())

# 같이 움직임, 각각 움직이는 횟수는 다름,
# 바로 직전에는 다른 위치, 다음번에 같은 위치인 경우 +1
# 만약 a가  움직임을 끝내고 b가 움직여서 같은 위치가 될시 이것도

mode=1 #같은거였으면 1, 다른거면 0, mode가 0 이고 각각배열이 같으면 cnt 증가
# 배열 길이가 다르기 때문에 똑같은거 더 큰 배열을 자른다. 배열의 길이가 똑같을 시 그냥 진행

pos_a = []
pos_b = []
ans = 0
now_pos = 0

for i in range(n):
    t, d = input().split()
    t = int(t)
    for j in range(t):
        if d == 'L':
            now_pos -= 1
            pos_a.append(now_pos)
        elif d == 'R':
            now_pos += 1
            pos_a.append(now_pos)

now_pos = 0

for i in range(m):
    t, d = input().split()
    t = int(t)
    for j in range(t):
        if d=='L':
            now_pos-=1
            pos_b.append(now_pos)
        elif d=='R':
            now_pos+=1
            pos_b.append(now_pos)


#긴걸로 채택 한뒤에 if len(pos_b)== i 랑 같아지면 last_pos 설정하고, pos_a만 돌림 + last_pos랑 값이 같아지면 ans+=1
if len(pos_a)>len(pos_b):
    for i in range(len(pos_a)):
        if len(pos_b)<=i+1:
            last_pos = pos_b[-1]
            if pos_a[i]==last_pos and mode==0:
                ans+=1
                mode=1
            else:
                mode=0
        elif len(pos_b)!=i+1 and pos_a[i] == pos_b[i] and mode == 0:
            ans+=1
            mode = 1

else:
    for i in range(len(pos_b)):
        if len(pos_a)<=i+1:
            last_pos = pos_a[-1]
            if pos_b[i]==last_pos and mode==0:
                ans+=1
                mode=1
        elif len(pos_a)!=i+1 and pos_b[i] == pos_a[i] and mode == 0:
            ans+=1
            mode = 1
        else:
            mode = 0

print(ans)