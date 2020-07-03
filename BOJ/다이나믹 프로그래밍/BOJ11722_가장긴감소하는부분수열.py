import sys

s = sys.stdin.readline

n = int(s())
seq = list(map(int, s().split()))

dp = [1] * n
for i in range(len(seq)):
    for j in range(i):
        if seq[j] > seq[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(dp)