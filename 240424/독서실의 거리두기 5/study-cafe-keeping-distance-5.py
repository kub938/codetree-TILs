n = int(input())
arr = list(map(int,input()))

max_len = 0


for i in range(n):
    if arr[i]!=0:
        continue
    arr[i]=1
    min_len = 100
    cnt=0
    for j in range(1,n):
        if arr[j]==1:
            min_len = min(min_len,cnt+1)
            cnt=0
        else:
            cnt+=1                
    arr[i]=0
    max_len = max(max_len, min_len)

print(max_len)