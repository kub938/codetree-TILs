n,k= map(int,input().split())
price = [int(input()) for _ in range(n)]

ans = 0
for i in range(n-1,-1,-1):
    if k==0:
        break
    ans += k//price[i]
    k%=price[i]

print(ans)