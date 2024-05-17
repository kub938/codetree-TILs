n,b = map(int,input().split())
price = [list(map(int,input().split())) for _ in range(n)]

sale=[]
ans = 0
for i in range(n):
    sale = price[:]
    sale[i][0]//=2
    p_list = []
    for j in range(n):
        p_list.append(sale[j][0]+sale[j][1])
    p_list.sort()
    cnt = 0
    sum_p =0
    for j in range(n):
        sum_p+=p_list[j]
        if sum_p>=b:
            ans = max(cnt,ans)
            break
        else:
            cnt+=1

print(ans)