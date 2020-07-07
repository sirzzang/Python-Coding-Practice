# 04_최대중량구하기_BOJ2217.py
# - 어차피 여러 개의 로프를 사용하면, 가장 적은 무게를 들 수 있는 로프 * 로프 개수가 최대 중량이지 않을까?
# - 로프 리스트로 받고, 최대 중량 갱신하는 방식으로.

# 어차피 여러 개 사용하면, 최소 무게 * k개 밖에 안 된다.
# 10, 15 -> 10kg 2개
# 10, 15, 17 -> 3개 사용하면 30, 2개 사용하면 30
# 10, 13, 17, 22 -> 4개 다 사용하면 40, 3개 사용하면

n = int(input())
ropes = sorted([int(input()) for _ in range(n)])

maximum_weight = 0
for i in range(len(ropes)):
    check_weight = ropes[i]*(n-i)
    if check_weight > maximum_weight:
        maximum_weight = check_weight

print(maximum_weight)

# - sys.stdin.readline() : 시간 빨라진다

import sys

def greedy_rope(ropes):
    maximum_weight = 0
    for i in range(len(ropes)):
       check_weight = ropes[i]*(n-i)
        if check_weight > maximum_weight:
            maximum_weight = check_weight

    return maximum_weight

n = int(sys.stdin.readline())
rope_list = sorted([int(sys.stdin.readline()) for _ in range(n)])

print(greedy_rope(rope_list))