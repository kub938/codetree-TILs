x,y = map(int,input().split())

ans = 0
for i in range(x,y+1):
    i = list(map(int,list(str(i))))
    sum_value = 0
    for j in i:
        sum_value+=j
    ans = max(ans,sum_value)

print(ans)