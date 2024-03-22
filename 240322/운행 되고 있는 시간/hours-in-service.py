n = int(input())
arr = []

for i in range(n):
    a,b = map(int,input().split())
    arr.append(b-a)

ans = sum(arr)-max(arr)

print(ans)