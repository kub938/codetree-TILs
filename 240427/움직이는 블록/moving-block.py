n = int(input())
arr = [int(input()) for _ in range(n)]

avg = sum(arr)//n
ans = 0
for e in arr:
    if e>avg:
        ans+= e-avg

print(ans)