n = int(input())
hint = [list(map(int,input().split())) for _ in range(n)]
check = False
ans = 10001

for i in range(hint[0][0],hint[0][1]+1):
    j = 1
    x=i
    for a,b in hint:
        x*=2
          
        if a<=x<=b:
            check=True
        else:
            check=False
            break
        j+=1
    if check:
        ans = min(i,ans)
    
print(ans)