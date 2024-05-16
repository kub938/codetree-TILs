n,h,t = map(int,input().split())
arr = list(map(int,input().split()))

diff_list = []
cnt=0
for i in range(n):
    diff_list.append(abs(arr[i]-h))
    if arr[i]==h:
        cnt+=1

ans = 0
diff_list.sort()
for i in range(t):
    ans+=diff_list[i]

print(ans)