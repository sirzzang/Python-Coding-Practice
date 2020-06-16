import sys
s = sys.stdin.readline

n = int(s())
wines = [0] + [int(s()) for _ in range(n)]

# print(wines) #check

dp = [0] * (n+1)

dp[1] = wines[1]
dp[2] = wines[1] + wines[2]

for i in range(3, n+1):
	dp[i] = max(dp[i-1], dp[i-2]+wines[i], wines[i-3]+wines[i-1]+wines[i])

print(dp)