n = int(input())
arr = [2,7,22]

for i in range(3,n):
    arr.append((arr[i-1]*3+arr[i-2]-arr[i-3])%1000000007)

print(arr[n-1])