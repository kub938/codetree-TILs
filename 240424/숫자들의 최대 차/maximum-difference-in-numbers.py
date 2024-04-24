n,k = map(int,input().split())
arr = [int(input()) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(i+1,n):
        if abs(arr[i]-arr[j])<=k:
            cnt+=1
    

print(cnt)