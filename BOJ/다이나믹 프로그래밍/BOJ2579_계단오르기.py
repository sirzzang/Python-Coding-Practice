# # n = int(input())
# # stairs = [0] + [int(input()) for _ in range(n)]
# #
# # if n == 1 or n == 2:
# #     print(sum(stairs))
# # else:
# #     max_score = [0] * (n + 1)
# #     max_score[1] = stairs[1]
# #     max_score[2] = stairs[1] + stairs[2]
# #     # 2번째 칸의 최댓값은 1칸씩 오를 때.
# #
# #     for i in range(3, n + 1):
# #         max_score[i] = max(max_score[i - 2] + stairs[i], max_score[i - 3] + stairs[i - 1] + stairs[i])
# #
# #     print(max_score[-1])
# #
import sys
s = sys.stdin.readline

n = int(s())

stairs = [0] + [int(s()) for _ in range(n)]

if n == 1:
    print(stairs[1])
elif n == 2:
    print(stairs[1]+stairs[2])
else:

    max_score = [0] * (n+1) # 시작 : 0번째 인덱스
    max_score[1] = stairs[1] # 1번 칸 최대 값
    max_score[2] = stairs[1] + stairs[2] # 2번째 칸은 반드시 한 칸씩 올라야 최대

    if n >= 3:
        max_score[3] = max(stairs[1]+stairs[3], stairs[2]+stairs[3])
        # 1번째 칸 -> 3번째 칸이거나, 2번째 칸 -> 3번째 칸.

        for i in range(4, n+1):
            max_score[i] = max(max_score[i-2] + stairs[i], max_score[i-3] + stairs[i-1] + stairs[i])
            # 전전 칸에서 두 칸을 올라오거나, 전전전 칸에서 한 칸 올라오고 두 칸 올라오거나.

        print(max_score[-1])
#
# #
# import sys
# read = lambda: sys.stdin.readline().rstrip()
# s1, s2 = 0, 0
# a,b,c,d = 0,0,0,0
# for _ in range(int(read())):
#     k = int(read())
#     print(f"계단 점수: {k}")
#     s1, s2 = s2, k
#     print(s1, s2) # 전 계단 점수, 지금 계단 점수.
#     a,b,c,d = b,c,d,max(c,b+s1)+s2
#     print(a, b, c, d) # b : 직전 계단 최대 점수 --> 이후에 전 계단 점수와 더함 : 3계단 전 + 직전 + 현재,
# # print(d)


