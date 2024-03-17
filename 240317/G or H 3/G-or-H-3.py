MAX_RANGE = 10000

n,k = map(int,input().split())
arr = [0] * (MAX_RANGE+1)
max_score = 0

for _ in range(n):
    x,c = input().split()
    x = int(x)
    arr[x] = 1 if c=='G' else 2

for i in range(MAX_RANGE-k+1):
    sum_score = 0
    for j in range(i,i+k+1):
        sum_score += arr[j]
    
    max_score = max(sum_score,max_score)

print(max_score)