# 초기 dp 리스트 설정 제대로 안하면 런타임 에러.
# 경우 복잡하게 나눌 필요가 없었다.

N = int(input())
dp = [0]*1000001

dp[1], dp[2], dp[3] = 0, 1, 1 # 초기값

for i in range(4, N+1):
    if i % 6 == 0:
        dp[i] = min(dp[i-1], dp[i//2], dp[i//3]) + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i-1], dp[i//2]) + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i-1], dp[i//3]) + 1
    else:
        dp[i] = dp[i-1]+1

print(dp[N])


for i in range(4, N+1):
    if i % 6 == 0: # 6, 12, 18, ...
        dp[i] = min(dp[i//2]+1, dp[i//3]+1)
    elif i % 2 == 0:
        if (i-1) % 3 == 0: # 4, 16, 64, 10, 28, 82, ...
            dp[i] = min(dp[i//2]+1, dp[(i-1)//3]+2, dp[i-1]+1)
        else: # 2, 4, 8, 14, 88, ...
            dp[i] = min(dp[i//2]+1, dp[i-1]+1)
    elif i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[(i-1)//2]+1, dp[i-1]+1)

    else: # 5, 7, 11, 13, 571, 1793, ... 어쨌든 1을 빼야 한다.
        dp[i] = dp[i-1]+ 1

print(dp[N])





############### 밑에는 망한 방법들..
# # 1) 2, 3으로 나눌 수 있을 때까지 나눠 보자. 여기서 나눠지는 애들은 그냥 1로 만들어 버리면 된다.
#
# # N = int(input())
# #
# # for n in range(1, N+1):
# #     print(n, end=" => ")
# #     while n % 3 == 0 or n % 2 == 0:
# #         if n % 3 == 0:
# #             n //= 3
# #         elif n % 2 == 0:
# #             n //= 2
# #     print(n)
#
# # 2) 1로 안 되는 애들 1씩 빼서 2, 3으로 나눠서 1로 만들어지게 하자.
# # N = int(input())
# # for n in range(1, N+1):
# #     while n > 1:
# #         print(n, end=" => ")
# #         while n % 3 == 0 or n % 2 == 0:
# #             if n % 3 == 0:
# #                 n //= 3
# #             elif n % 2 == 0:
# #                 n //= 2
# #         else:
# #             if n == 1:
# #                 break
# #             n -= 1
# #     print(n)

# 3) 1로 만들어지는 과정을 보자.
# - 문제1: 10, 28의 경우 1로 빼고 3으로 다 나누는 게 빠르다.
# - 문제2: 문제 1을 해결하고 나니, 이제 16이 1을 빼 버린다.
# - 오????????????
# N = int(input())
# for n in range(1, N+1):
#     while n > 1:
#         print(n, end=" => ")
#         while n % 3 == 0 or n % 2 == 0:
#             if n % 3 == 0:
#                 n //= 3
#                 print(n, end=" => ")
#             elif n % 2 == 0:
#                 if (n-1) % 3 == 0 and (n-1) % 2 != 1:
#                     n -= 1
#                 else:
#                     n //= 2
#                 print(n, end=" => ")
#         else:
#             if n == 1:
#                 break
#             n -= 1
#     print(n)
#
# # 4) 연산횟수
#
#
# # for i in range(1, N+1):
# #     n = i
# #     cnt = 0
# #     # cnt = dp[i]
# #     # print(f"dp {i}번째, 이전 연산 횟수: {cnt}")
# #
# #     while n > 1:
# #
# #         while n % 3 == 0 or n % 2 == 0:
# #             if n % 3 == 0:
# #                 n //= 3
# #                 cnt += 1
# #                 # cnt = dp[n]
# #             elif n % 2 == 0:
# #                 n //= 2
# #                 cnt += 1
# #                 # cnt = dp[n]
# #
# #         else:
# #             if n == 1:
# #                 break
# #             n -= 1
# #             cnt += 1
# #
# #     print(f"{i}번째 연산 횟수 {cnt}, {i-1}번째 dp {dp[i-1]}")
# #
# #     dp[i] = min(dp[i-1]+1, cnt)
#
#     # if n == 1: # 검사 후 1이 만들어진다면
#     #     dp[i] = min(dp[i-1]+1, cnt)
#     # else: # 1이 안 만들어 진다면
#     #     dp[i] = min(dp[i-1]+1, dp[n]+1)
#
# N = int(input())
# dp = [0] * (N+1)
#
# for i in range(1, N+1):
#     n = i
#     cnt = 0
#     # cnt = dp[i]
#     # print(f"dp {i}번째, 이전 연산 횟수: {cnt}")
#
#     while n % 3 == 0 or n % 2 == 0:
#         if n % 3 == 0:
#             n //= 3
#             cnt += 1
#         elif n % 2 == 0:
#             n //= 2
#             cnt += 1
#
#     print(f"{i}번째 수: 검사 후 {n}, 연산 횟수 {cnt}")
#
#     if n == 1:
#         dp[i] = min(cnt, dp[i-1]+1)
#     else:
#         if n == i: # 아예 나누기조차 안 됨.
#             dp[i] = min(dp[i-1]+1, dp[i-2]+2)
#         else: # 나눠지니까 거기서 연산 한 번만 더 하면 됨(2를 곱하든 3을 곱하든) -- 1을 더하는 경우는 어떻게 되려나? 일단 해보자.
#             dp[i] = min(dp[n]+1, dp[i-1]+1, dp[i-2]+2)
#
#     print(f"{i}번째 dp: {dp[i]}")
#
# print(dp)

# # 재귀 : 근데 어차피 이것도 재귀호출을 해야 하니까..
# def div(n, cnt):
#     while n % 3 == 0 or n % 2 == 0:
#         if n % 3 == 0:
#             n //= 3
#             cnt += 1
#         elif n % 2 == 0:
#             n //= 2
#             cnt += 1
#     if n == 1:
#         return cnt
#     else:
#         n -= 1
#         cnt += 1
#         return div(n, cnt) # 재귀
#
# N = int(input())
# dp = [0] * (N+1)
# for i in range(1, N+1):
#     dp[i] = min(div(i, 0), dp[i-1]+1, dp[i-2]+2)
# print(dp)




# N = int(input())
# dp = [0] * (N + 1)
#
# for i in range(1, N + 1):
#     n = i
#     cnt = 0
#
#     # 2, 3으로 나눌 수 있을 때까지 검사
#     while n % 3 == 0 or n % 2 == 0:
#         if n % 3 == 0:
#             n //= 3
#             cnt += 1
#         elif n % 2 == 0:
#             n //= 2
#             cnt += 1
#
#     print(f"{i}번째 수: 검사 후 {n}, 연산 횟수 {cnt}")
#
#     if n == 1:
#         dp[i] = min(cnt, dp[i-1] + 1)
#     else:
#         if n == i:  # 아예 나누기조차 안 됨.
#             dp[i] = min(dp[i-1] + 1, dp[i-2] + 2)
#         else:
#             dp[i] = min(dp[n] + cnt, dp[i-1]+1)
#
#     print(f"{i}번째 dp: {dp[i]}")
#
# print(dp)