n = int(input())
arr = list(map(int,input().split()))
arr.append(0)
result = []
for i in range(1,n+1):
    if len(result)==n:
        break
    result = []
    next_num = i
    for j in range(n):
        if next_num in result or next_num>n:
            break
        result.append(next_num)
        next_num=abs(arr[j]-next_num)


print(*result)