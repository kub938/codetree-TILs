n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0

if a[0]<b[0]:
    a,b = b,a

for i in range(n-1):
    a[i+1] += a[i]-b[i]
    ans += a[i]-b[i]

print(ans)