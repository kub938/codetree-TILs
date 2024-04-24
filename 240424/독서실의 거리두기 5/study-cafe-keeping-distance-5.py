n = int(input())
arr = list(map(int,input()))

max_len = 0

for i in range(n):
    if arr[i]!=0:
        continue
    arr[i]=1
    min_len = 100
    cnt=0
    check = False
    for j in range(n):
        if arr[j]==1 and check :
            min_len = min(min_len,cnt+1)

            cnt=0
        if arr[j]==1 :
            check = True
        elif not check:
            continue
        else:
            cnt+=1                
    arr[i]=0
    max_len = max(max_len, min_len)

print(max_len)