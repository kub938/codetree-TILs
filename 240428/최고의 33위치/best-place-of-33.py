n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

max_coin = 0




for i in range(n-(n-1)):
    for j in range(i,n-(n-1)):
        coins = 0
        for k in range(3):
            coins += sum(arr[i+k][j:j+3])
        max_coin = max(coins,max_coin)
    
print(max_coin)