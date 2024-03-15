n = int(input())
arr = [int(input()) for _ in range(n)]
sum_dis = 0
arr_dist = [i for i in range(n)]
dists = []

for i in range(1,n):
    for j in range(1,n):
        sum_dis+=arr[(i+j)%n]*arr_dist[j]
    dists.append(sum_dis)
    sum_dis=0

print(min(dists))