dp = [1,2,5]
n = int(input())

for i in range(4,n):
    dp.append(dp[i-3]+dp[i-2]+dp[i-1])

print(dp[n-1])