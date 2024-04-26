n = int(input())
arr = [list(input().split()) for _ in range(n)]

a_score = 0
b_score = 0
g_state = 1  # 1==a,b 같이 올라감 2==a, 3==b
cnt = 0

for c,s in arr:
    s = int(s)
    if c=='A':
        a_score+=s
    else:
        b_score+=s

    if a_score>b_score and g_state!=2:
        cnt+=1
        g_state=2
    elif a_score<b_score and g_state!=3:
        cnt+=1
        g_state=3
    elif a_score==b_score and g_state!=1:
        cnt+=1
        g_state=1
    

print(cnt)