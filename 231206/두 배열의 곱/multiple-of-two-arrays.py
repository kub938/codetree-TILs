arr1 = [list(map(int,input().split()))for _ in range(3)]
input()
arr2 = [list(map(int,input().split()))for _ in range(3)]

result = [[0 for _ in range(3)] for _ in range(3)]

for row in range(3):
    for col in range(3):
        result[row][col] = arr1[row][col] * arr2[row][col]
    print(*result[row])