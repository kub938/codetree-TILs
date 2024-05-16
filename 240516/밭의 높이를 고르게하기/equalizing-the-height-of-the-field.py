n,h,t = map(int,input().split())
arr = list(map(int,input().split()))

diff_list = []
cnt=0
for i in range(n):
    diff_list.append(abs(arr[i]-h))

ans = 200
for i in range(n-t+1):
    sum_value = 0
    for j in range(i,t+i):
        sum_value+=diff_list[j]
    ans = min(ans,sum_value)

if n==1:
    ans = diff_list[0]
print(ans)