n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

price=0
cost = 0
for i in range(1,n//2+1):
    s = arr[i-1]
    e = arr[-i]
    if e-s<18:
        break
    if (e-s-17)%2==0:
        cost+=2*(((e-s-17)//2)**2)
    else:
        cost+=((e-s-17)//2)**2+((e-s-17)//2-1)**2

print(cost)