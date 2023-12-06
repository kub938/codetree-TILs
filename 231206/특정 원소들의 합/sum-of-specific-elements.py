arr = [list(map(int,input().split()))for _ in range(4)]

area = 1
sum_arr = 0
for i in arr:
    for j in range(area):
        sum_arr+=i[j]
    area+=1

print(sum_arr)