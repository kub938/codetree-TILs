n,b = map(int,input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

cnt = 0
sum_p = 0

for i in range(n):
    if (sum_p+arr[i])>b:
        if sum_p+(arr[i]//2)-arr[i-1]>b:
            break
        else:
            cnt=i+1
            break
    else:
        sum_p = sum_p+arr[i]
        cnt=i+1

print(cnt)