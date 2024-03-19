n,h,t = tuple(map(int,input().split()))
arr = list(map(int,input().split()))
tmp = []
sum_h = 0

for i in range(n):
    tmp.append(abs(arr[i]-h))

tmp = sorted(tmp)
sum_h = sum(tmp[:t])

print(sum_h)