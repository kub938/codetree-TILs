arr = [list(map(int,input().split())) for _ in range(2)]
total_sum = []
avg1=0
avg2=0
for i in range(2):
    avg1 = sum(arr[i])/4
    total_sum.append(avg1)
    print(avg1,end=" ")
print()

for j in range(4):
    for k in range(2):
        avg2+=arr[k][j]
    avg2/=2
    total_sum.append(avg2)
    print(avg2,end=" ")
    avg2=0
print()
print(f'{sum(total_sum)/6:.1f}')