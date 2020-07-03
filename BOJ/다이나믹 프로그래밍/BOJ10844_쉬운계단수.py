# 정답
dp = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0][:] for _ in range(101)]  # 초기값 설정
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

N = int(input())

for i in range(2, N + 1):
    # print(f"{i-1}th dp: {dp[i-1]}") # check
    dp[i][0] = dp[i - 1][1] % 1000000000
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 1000000000
    dp[i][2] = (dp[i - 1][1] + dp[i - 1][3]) % 1000000000
    dp[i][3] = (dp[i - 1][2] + dp[i - 1][4]) % 1000000000
    dp[i][4] = (dp[i - 1][3] + dp[i - 1][5]) % 1000000000
    dp[i][5] = (dp[i - 1][4] + dp[i - 1][6]) % 1000000000
    dp[i][6] = (dp[i - 1][5] + dp[i - 1][7]) % 1000000000
    dp[i][7] = (dp[i - 1][6] + dp[i - 1][8]) % 1000000000
    dp[i][8] = (dp[i - 1][7] + dp[i - 1][9]) % 1000000000
    dp[i][9] = dp[i - 1][8] % 1000000000

print(sum(dp[N]) % 1000000000)

############# copy 여부 주의합시다 #############################
from copy import deepcopy

dp = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]*10 # 초기값 설정
dp[1] = [100, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print("==================== copy 안 했을 때 ====================")
print(dp)
for d in dp:
    print(id(d), id(d[0]))

dp_copy = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0][:] for _ in range(10)] # 초기값 설정
dp_copy[1] = [200, 100, 1, 1, 1, 1, 1, 1, 1, 1]
print("==================== copy 했을 때 ====================")
print(dp_copy)
for d in dp_copy:
    print(id(d), id(d[0]))

dp_deepcopy = [deepcopy([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) for _ in range(10)] # 초기값 설정
dp_deepcopy[1] = [100, 400, 1, 1, 1, 1, 1, 1, 1, 1]
print("==================== deepcopy 했을 때 ====================")
print(dp_deepcopy)
for d in dp_deepcopy:
    print(id(d), id(d[0]))