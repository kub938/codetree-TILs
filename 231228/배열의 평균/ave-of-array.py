arr = [list(map(int,input().split()))for _ in range(2)]
n = len(arr[0])


row_sum1 = sum(arr[0])
row_sum2 = sum(arr[1])

avg_sum1 = row_sum1/4
avg_sum2 = row_sum2/4

print(avg_sum1, avg_sum2)


for row in range(n):
    sum_col = 0
    for col in range(2):
        sum_col += arr[col][row]
    avg_col = sum_col/2
    print(avg_col,end=" ")
print()

print(round((row_sum1+row_sum2)/8,1))