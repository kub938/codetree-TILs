n = int(input())
arr = list(map(int, input().split()))

cnt = 0
ele_avg = 0

for i in range(n):
    for j in range(i, n):  # 순환 길이 조절
        sum_val = 0
        for k in range(i, j + 1):  # 순환
            sum_val += arr[k]
        ele_avg = sum_val //(j+1-i)
        if ele_avg in arr[i:j+1]:
            cnt += 1

print(cnt)