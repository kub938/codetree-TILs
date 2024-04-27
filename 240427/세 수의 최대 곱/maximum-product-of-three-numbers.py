import sys

n = int(input())
arr = list(map(int,input().split()))
cnt = [0,0,0] #0 = 0, 1 = 음수, 2=양수 갯수
    
arr.sort()
for e in arr:
    if e<0:
        cnt[1]+=1
    elif e==0:
        cnt[0]+=1
    else:
        cnt[2]+=1


for i in range(3):
    if n in cnt:
        c = cnt.index(n)        
        if c==0:
            ans = 0
        else:
            ans = arr[-1]*arr[-2]*arr[-3]
        break
    elif cnt[1]>=2 and cnt[2]>=1:
        ans = max(arr[0]*arr[1]*arr[-1], arr[-1]*arr[-2]*arr[-3])
    else:
        ans = arr[0]*arr[1]*arr[2]


print(ans)