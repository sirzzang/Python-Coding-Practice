# 시간 초과
# import sys

# T = int(sys.stdin.readline())

# for _ in range(T):

#     N = int(sys.stdin.readline())

#     candidates = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)], key=lambda x: -x[0])

#     front_idx = 0
#     cnt = N

#     while front_idx < N :
#         if any(candidates[front_idx][1] > candidate[1] for candidate in candidates[front_idx+1:]):
#             front_idx += 1
#             cnt -= 1
#         else:
#             front_idx += 1
#     print(cnt)

# T = int(sys.stdin.readline())

# for _ in range(T):

#     N = int(sys.stdin.readline())

#     candidates = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)], key=lambda x: -x[0])

#     front_idx = 0
#     cnt = N

#     while front_idx < N :
#         if any(candidates[front_idx][1] > candidate[1] for candidate in candidates[front_idx+1:]):
#             front_idx += 1
#             cnt -= 1
#         else:
#             front_idx += 1
#     print(cnt)


# candidates = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)], key=lambda x: -x[0])
# print(candidates)




# front_idx = 0
# cnt = N
# fail = 0
# while front_idx < N :
#     if candidates[front_idx][1] - fail <= front_idx :

#     if candidates[front_idx][1] <= front_idx + 1:        
#         front_idx +=1
#     else:
#         cnt -= 1
#         front_idx +=1
# print(cnt)


# O(nlogn) 시간복잡도 위해 퀵 소트 함수 정의.

# def QuickSort(a, begin, end):
#     if begin < end:
#         p = Partition(a, begin, end)
#         QuickSort(a, begin, p-1)
#         QuickSort(a, p+1, end)
#     return a

# def Partition(a, begin, end):
#     pivot_idx = (begin + end)//2
#     L = begin
#     R = end
#     while L < R:
#         while (a[L][0] < a[pivot_idx][0] and L < R):
#             L += 1
#         while (a[R][0] >= a[pivot_idx][0] and L < R):
#             R -= 1
#         if L < R:
#             if L == pivot_idx:
#                 pivot_idx = R
#             a[L], a[R] = a[R], a[L]
#     a[pivot_idx], a[R] = a[R], a[pivot_idx]
#     return R


# import sys

# T = int(sys.stdin.readline())

# for _ in range(T):

#     N = int(sys.stdin.readline())
#     candidates = QuickSort([list(map(int, sys.stdin.readline().split())) for _ in range(N)], 0, N-1)

#     front_idx = 0
#     highest_rank = N+1
#     cnt = 0

#     for candidate in candidates:
#         if candidate[1] < highest_rank:
#             cnt += 1
#             highest_rank = candidate[1]
#     print(cnt)


import sys

T = int(sys.stdin.readline())

for _ in range(T):

    N = int(sys.stdin.readline())
    candidates = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)], key=lambda x: x[0])

    front_idx = 0
    highest_rank = N+1
    cnt = 0

    for candidate in candidates:
        if candidate[1] < highest_rank:
            cnt += 1
            highest_rank = candidate[1]
    print(cnt)
