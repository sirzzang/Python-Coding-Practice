# N = int(input())
#
# dp = [[int(input())]]
# print(dp)
#
# for i in range(1, N):
#     print(f"{i-1}층: {dp[i - 1]}")
#     tri = list(map(int, input().split()))
#     print(f"{i}층: {tri}")
#     for j in range(len(tri)):
#         print(f"{i}층 {j}번째")
#         if j == 0:
#             tri[j] += dp[i-1][0]
#         elif j == len(tri) - 1:
#             tri[j] += dp[i-1][j-1]
#         else:
#             tri[j] += max(dp[i-1][j-1], dp[i-1][j])
#     print(tri)
#     dp.append(tri)
#
# print(max(dp[-1]))

def solution():
    import sys
    n = int(input())
    triangle = []
    for _ in range(n):
        triangle.append(list(map(int, sys.stdin.readline().rstrip().split())))

    accum = []
    for i in range(n):
        for a, b, c in zip([0] + accum, accum + [0], triangle[i]):
            print(a+c, b+c)
        accum = [max(a + c, b + c) for a, b, c in zip([0] + accum, accum + [0], triangle[i])] # a+c, b+c가 int가 된다. 아 그렇지.
        print(accum)
    print(max(accum))



solution()

