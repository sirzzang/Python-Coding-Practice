# n=1, n=2 런타임에러 주의
# 처음 오답: dp[i] = max(dp[i-1], dp[i-2]+wines[i], wines[i-3]+wines[i-1]+wines[i]) # 미친건가

import sys
s = sys.stdin.readline

n = int(s())
wines = [0] + [int(s()) for _ in range(n)]
# print(wines) #check

dp = [0] * (n+1) # 초기 배열 설정

if n == 1:
    print(wines[1])
elif n == 2:
    print(wines[1] + wines[2])
else:
    dp[1] = wines[1] # 초기값
    dp[2] = wines[1] + wines[2] # 초기값
    for i in range(3, n+1):
	    dp[i] = max(dp[i-1], dp[i-2]+wines[i], dp[i-3]+wines[i-1]+wines[i])
    print(dp[n])