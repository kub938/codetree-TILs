a,b = map(int,input().split())
c,d = map(int,input().split())
arr = [0]*101

if c<a:
    a,b,c,d = c,d,a,b

if b<c or d<a:
    ans = b-a+d-c
elif b>c:
    ans = d-a
elif d>a:
    ans = d-a

print(ans)