n = int(input())
arr = [list(input().split()) for _ in range(n)]

a_score = 0
b_score = 0
c_score = 0
g_status = 1 # 1:a==b==c 2:a>b,c 3:b>a,c 4:c>a,b 5:a==b 6:a==b 7:b==c 

ans=0
for c,s in arr:
    s = int(s)
    if c=='A':
        a_score+=s
    elif c=='B':
        b_score+=s
    else:
        c_score+=s

    if a_score==b_score==c_score and g_status!=1:
        ans+=1
        g_status=1
    elif a_score>b_score and a_score>c_score and g_status!=2:
        ans+=1
        g_status=2
    elif b_score>a_score and b_score>c_score and g_status!=3:
        ans+=1
        g_status=3
    elif c_score>a_score and c_score>b_score and g_status!=4:
        ans+=1
        g_status=4
    elif a_score==b_score and g_status!=5:
        ans+=1
        g_status=5
    elif a_score==c_score and g_status!=6:
        ans+=1
        g_status=6
    elif b_score==c_score and g_status!=7:
        ans+=1
        g_status=7

print(ans)