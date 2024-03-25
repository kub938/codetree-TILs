n,b = map(int,input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

cnt = 0
sum_p = 0

for i in range(n):
    sum_p+=arr[i]
    if sum_p>b:
        if i==0:
            cnt=0
            break
        elif sum_p-arr[i]+arr[i]//2<=b:
            cnt=i+1
            break
        else:
            cnt=i
            break

print(cnt)