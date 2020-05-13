# 시간 초과

# import sys

# def Select(a, k):
#     for i in range(k):
#         min_idx = i
#         for j in range(i+1, len(a)):
#             if a[min_idx] > a[j]:
#                 min_idx = j
#         a[i], a[min_idx] = a[min_idx], a[i]
#     return a[k-1]


# N, K= map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))

# print(Select(arr, K))

# 퀵 소트로 구현해볼까?
# 시간초과

# import sys

# def BOJ_11004():

#     def QuickSort(a, begin, end):
#         if begin < end:
#             p = Partition(a, begin, end) # R의 위치.
#             QuickSort(a, begin, p-1)
#             QuickSort(a, p+1, end)
#         return a

#     def Partition(a, begin, end):
#         pivot_idx = (begin + end) // 2
#         L = begin
#         R = end

#         while L < R:
#             while (a[L] < a[pivot_idx] and L < R):
#                 L += 1
#             while (a[R] >= a[pivot_idx] and L < R):
#                 R -= 1
#             if L < R :
#                 if L == pivot_idx:
#                     pivot_idx = R
#                 a[L], a[R] = a[R], a[L]

#         a[pivot_idx], a[R] = a[R], a[pivot_idx] 
#         return R
    
#     N, K= map(int, sys.stdin.readline().split())
#     arr = sorted(list(map(int, sys.stdin.readline().split())))

#     return QuickSort(arr, 0, len(arr)-1)[K-1]

# print(BOJ_11004())



import sys
N, K= map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
print(arr[K-1])