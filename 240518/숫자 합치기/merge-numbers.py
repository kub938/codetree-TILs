n = int(input())
arr = list(map(int,input().split()))

price = 0
while n!=1:
    arr.sort()
    arr[0]=arr[0]+arr[1]
    price += arr[0]
    del arr[1]
    n-=1

print(price)