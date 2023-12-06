n,m = map(int,input().split())

arr1 = [list(map(int,input().split()))for _ in range(n)]
arr2 = [list(map(int,input().split()))for _ in range(n)]
result = [[1 for _ in range(m)] for _ in range(n)]

for row in range(n):
    for col in range(m):
        if arr1[row][col] == arr2[row][col]:
            result[row][col] = 0
        print(result[row][col],end=" ")
    print()