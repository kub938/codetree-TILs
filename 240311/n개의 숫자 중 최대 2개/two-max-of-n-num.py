n = int(input())
arr=list(map(int,input().split()))
result=[]
for i in range(n):
    result.append(max(arr))
    arr.pop(arr.index(max(arr)))

print(result[0], result[1])