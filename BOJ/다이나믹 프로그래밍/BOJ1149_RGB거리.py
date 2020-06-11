# 테스트 케이스 생성
# import random
# N = random.randint(1, 14)
# print(N)
# for _ in range(N):
#     print([random.randint(1, 1000) for _ in range(3)])

# N = int(input()) # 칠해야 할 집의 개수
# # min_cost = [0] * N # 각 단계에서 칠하는 최소 비용
# costs = [list(map(int, input().split())) for _ in range(N)]
# # print(costs)
# for i in range(1, N):
#     # print(costs[i])
#     costs[i][0] += min(costs[i-1][1], costs[i-1][2])
#     costs[i][1] += min(costs[i-1][0], costs[i-1][2])
#     costs[i][2] += min(costs[i-1][0], costs[i-1][1])
# print(min(costs[-1]))

import sys

s = sys.stdin.readline

N = int(s())

costs = [list(map(int, s().split())) for _ in range(N)]

for i in range(1, N):
    costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
    costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
    costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])

print(costs)
print(min(costs[-1]))

# N = int(input())

# # 초기 설정
# costs = list(map(int, input().split()))
# min_c = min(costs)
# idx, money = costs.index(min_c), min_c
# print(f"초기 색칠할 집 순서: {idx+1}, 돈: {min_c}, 누적 필요한 돈: {money}")
#
# # 이후 집들 색칠
# for _ in range(N-1):
#     costs = list(map(int, input().split()))
#     print(costs)
#     costs[idx] = 1001 # 이전에 사용한 색 사용 불가
#     print(f"사용 불가 후: {costs}")
#     min_c = min(costs)
#     idx = costs.index(min_c)
#     money += min_c # 누적
#     print(f"색칠할 색 순서: {idx + 1}, 돈: {min_c}, 누적 필요한 돈: {money}")
#
# print(money)