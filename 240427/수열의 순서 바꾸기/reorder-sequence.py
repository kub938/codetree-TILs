n = int(input())
arr = list(map(int,input().split()))


i = n-2

while 1:
    if arr[i-1]>arr[i]:
        break
    i-=1

print(n-(n-i))