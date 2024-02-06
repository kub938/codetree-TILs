n,m = map(int,input().split())

a = []
b = []
same_cnt=0
now_pos = 0

for i in range(n):
    t,d = input().split()
    t = int(t)
    if d=='L':
        for j in range(t):
            now_pos-=1  
            a.append(now_pos)
    else:
        for j in range(t):
            now_pos+=1
            a.append(now_pos)

now_pos = 0

for i in range(m):
    t,d = input().split()
    t = int(t)
    if d=='L':
        for j in range(t):
            now_pos-=1  
            b.append(now_pos)
    else:
        for j in range(t):
            now_pos+=1
            b.append(now_pos)


min_ab = min(len(a),len(b))
max_ab = max(len(a),len(b))

for i in range(1,min_ab):
    if a[i-1] == b[i-1]:
        continue
    else:
        if a[i] == b[i]:
            same_cnt+=1

for i in range(min_ab,max_ab):
    if min_ab == len(a):
        if a[-1] == b[i-1]:
            continue
        else:
            if a[-1] == b[i]:
                same_cnt+=1
    else:
        if a[i-1] == b[-1]:
            continue
        else:
            if a[i] == b[-1]:
                same_cnt+=1



print(same_cnt)

# 해설은 더 짧은 길이를 내가 사용한 now_pos를 각각 pos_a, pos_b 로 사용하여 0 으로 초기화 하지 않고 서로 비교해서 구함
# 그후 나는 새롭게 만나는 횟수를 구하고 더 긴 배열을 한번 더 돌리는 형식으로 구현했지만
# 해설은 먼저 더 짧은 구간을 구해서 그 구간의 마지막 인덱스를 더 긴 배열과의 길이 차이만큼 추가하는 형식으로 길이를 맞춘후
# 새롭게 만나는 횟수를 구하는 형식으로 구현함