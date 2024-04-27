n = int(input())
arr = list(map(int,input().split()))


i = n-2
while arr[i]<arr[i+1] and i>=0:
    i-=1

print(i+1)