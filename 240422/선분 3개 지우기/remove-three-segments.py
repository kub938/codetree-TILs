n = int(input())

arr =[list(map(int,input().split())) for _ in range(n)]
cross = []

cnt=1
for i in range(len(arr)-1):
    a,b = arr[i+1][0],arr[i][1]
    if a<=b:
        cnt+=1
    else:
        cross.append(cnt)
        cnt=1

cross.append(cnt)

ans = 1
for e in cross:
    ans*=e

print(ans)