n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]



def sum_area_gold():
    golds = sum(arr[i][j] for i in range(n) for j in range(n) if abs(r-i)+abs(c-j)<=k)
    return golds

max_gold = 0
for r in range(n):
    for c in range(n):
        for k in range(2*(n-1)+1):
            sum_gold = sum_area_gold()
            if sum_gold*m>=k*k+(k+1)*(k+1):
                max_gold= max(max_gold,sum_gold)
    
print(max_gold)