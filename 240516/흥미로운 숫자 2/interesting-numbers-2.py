from collections import Counter
x,y = map(int,input().split())

ans = 0
for i in range(x,y+1):
    i = str(i)
    count_n = Counter(i)
    if len(count_n)==2:
        ans+=1

print(ans)