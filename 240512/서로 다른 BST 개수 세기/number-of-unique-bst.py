dp = [1,2]
n = int(input())


for i in range(2,n):
    dp.append(dp[i-1]*dp[i-2]+i+1)

print(dp[n-1])