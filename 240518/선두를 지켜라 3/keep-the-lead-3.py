n,m = map(int,input().split())

a_move = [0]
b_move = [0]


now_pos = 0
for i in range(n):
    v,t = map(int,input().split())
    for j in range(t):
        now_pos+=v
        a_move.append(now_pos)

now_pos = 0
for i in range(m):
    v,t = map(int,input().split())
    for j in range(t):
        now_pos+=v
        b_move.append(now_pos)


# if a_move[0]>b_move[0]:
#     learder = 1
# elif a_move[0]<b_move[0]:
#     leader = 2
# else:
#     leader = 3

leader = 0
ans = 0
for i in range(len(a_move)):
    if leader!= 1 and a_move[i]>b_move[i]:
        leader = 1
        ans+=1
    elif leader!=2 and a_move[i]<b_move[i]:
        leader = 2
        ans+=1
    elif leader!=3 and a_move[i]==b_move[i]:
        leader = 3
        ans+=1

print(ans-1)