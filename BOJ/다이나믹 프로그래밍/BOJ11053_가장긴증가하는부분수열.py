# 시행착오: 앞에서부터 옮기면서 큰 애 나오면 선택하는 방식. 그리디하다.

# N = int(input())
# seq = list(map(int, input().split()))
# i = 1 # 뒤로 옮겨 가면서 볼 애들
# # j = 0
# # while i < N: # i 수열 끝까지 옮기면서 검사
# #     dp[i] = dp[i-1] # 이전의 dp값 이용
# #     flag = seq[i]
# #     print(f"i: {i}, 검사: {flag}, 시작 위치: {j}")
# #     j = 0 # 검사할 요소가 뒤로 밀릴 때마다 j도 초기화.
# #     while j < i:
# #         if seq[j] < flag and dp[i-1] + 1 > dp[i]:
# #             dp[i] += 1
# #         j += 1
# #     i += 1
# #     print(f"{i}, {flag}완료. 현재 dp: {dp}")
# #     # print(dp)


# 테스트 케이스 생성
# import random
# N = random.randint(1, 100)
# seq = [random.randint(1, 1000) for _ in range(N)]
# print(N, seq)
# dp = [1] * N
# print(seq)
# # 뒤를 기준으로 옮겨야 한다.
# dp = [1] * N # 초기 dp 배열 : 어차피 처음에는 다 1개다.


N = int(input())
seq = list(map(int, input().split()))
dp = [1] * N
for i in range(len(seq)):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(dp)


