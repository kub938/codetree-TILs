a,b,c = map(int,input().split())

sum_max = 0
for i in range(1000):
    for j in range(1000):
        if a*i+b*j>c:
            break
        else:
            sum_max=max(sum_max,a*i+b*j)

print(sum_max)