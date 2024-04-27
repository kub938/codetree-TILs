n = int(input())
arr = list(map(int,input().split()))

even, odd = 0,0
ans = 0

for i in arr:
    if i%2 == 0:
        even+=1
    else:
        odd+=1

if odd==even:
    ans = even+odd
elif odd<even:
    ans = even+odd-(even-odd)+1
else:
    ans+=even*2
    ans+=(odd-even)//3*2
    if (odd-even)%3==2:
        ans+=1
    elif (odd-even)%3==1:
        ans-=1
    
print(ans)