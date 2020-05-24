import heapq

scoville = list(map(int, input().split()))
K = int(input())

# '모든 음식의 스코빌 지수가 K 이상'이다. 점수를 K로 만드는 게 아니라.
h = []
for s in scoville:
    heapq.heappush(h, (-1, s))
print(h)
cnt = 0

try:
    while h[0][1] < K :
        score = heapq.heappop(h)[1] + 2*heapq.heappop(h)[1]
        print(score)
        cnt += 1
        heapq.heappush(h, (-1, score))
        print(h, cnt)
except IndexError:
    cnt = -1

print(cnt)
# 정확성 : 6/15, 효율성 : 0/4
# import heapq
#
# h = []
# for s in scoville:
#     heapq.heappush(h, (-1, s))
#
# cnt = 0
#
# # 스코빌 지수 만들어서 넣어야 함.
# while len(h) > 1:
#     score = heapq.heappop(h)[1] + 2*heapq.heappop(h)[1]
#     cnt += 1
#     print(f"점수는 {score}이고, 섞은 횟수는 {cnt}입니다.")
#     if score >= K:
#         break
#     heapq.heappush(h, (-1, score))
# else:
#     cnt = -1
#
# print(h)
# print(cnt)