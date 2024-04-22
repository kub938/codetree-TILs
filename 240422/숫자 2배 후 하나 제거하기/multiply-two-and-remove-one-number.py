n = int(input())
arr = list(map(int,input().split()))

min_diff = 100000
for i in range(n):
    arr[i]*=2
    for j in range(n):
        tmp = []
        sum_diff = 0
        tmp.append(arr.pop(j))

        for k in range(n-2):
            sum_diff += abs(arr[k]-arr[k+1])
        min_diff = min(min_diff,sum_diff)
        arr.insert(j,*tmp)
    arr[i]//=2
    
print(min_diff)