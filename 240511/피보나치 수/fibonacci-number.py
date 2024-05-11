# n-2 + n-1 = n
fibo = [1,1]
n = int(input())

for i in range(2,n):
    fibo.append(fibo[i-2]+fibo[i-1])

print(fibo[n-1])