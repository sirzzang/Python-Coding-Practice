# 메모리 초과
# 수의 범위가 10000이다.

# def CountingSort(A):

#     counts = [0] * (max(A)+1)
#     temp = [0] * len(A)

#     for a in A:
#         counts[a] += 1
    
#     for i in range(len(counts)-1):
#         counts[i+1] += counts[i]
    
#     for i in range(len(temp)-1, -1, -1):
#         temp[counts[A[i]]-1] = A[i]
#         counts[A[i]] -= 1
    
#     return temp

# 퀵 정렬 사용하기
# 메모리 초과

# def QuickSort(a, begin, end):
#     if begin < end :
#         p = Partition(a, begin, end) # 분할 기준 인덱스
#         QuickSort(a, begin, p-1) # 왼쪽 배열에 대해 재귀 호출
#         QuickSort(a, p+1, end) # 오른쪽 배열에 대해 재귀 호출
#     return a
        
# def Partition(a, begin, end):
#     pivot_idx = (begin + end) // 2 # 피봇 인덱스 : 중간 위치로 설정.
#     print(a[pivot_idx]) # 피봇 값 확인 위해
#     L = begin
#     R = end
#     while L < R: # L이랑 R 만날 때까지 아래 과정 반복
#         while (a[L] < a[pivot_idx] and L < R) : # 피봇 값보다 왼쪽에 있는데 작다면 L 증가 = 피봇값보다 크거나 같은데 왼쪽에 있는 원소 찾기.
#             L += 1
#         while (a[R] >= a[pivot_idx] and L < R) : # 피봇 값보다 오른 쪽에 있는데 크다면 R 증가 = 피봇값보다 작은데 오른쪽에 있는 원소 찾기.
#             R -= 1
#         if L < R : # 위의 과정을 거쳤는데 만나지 않은 경우
#             if L == pivot_idx : # L이 피봇 값이면
#                 pivot_idx = R # 피봇을 오른쪽으로 바꾸기
#             a[L], a[R] = a[R], a[L] # 만나지 않았다면, L과 R 위치의 원소 바꾸기
#     a[pivot_idx], a[R] = a[R], a[pivot_idx]
#     return R

# 버블 정렬
# 메모리 초과

# def BubbleSort(a):
#     for i in range(len(a)):
#         for j in range(len(a)-1):
#             if a[j] > a[j+1]:
#                 a[j+1], a[j] = a[j], a[j+1]
#     return a



# 선택 정렬
# 메모리 초과

# def SelectionSort(a):
#     for i in range(len(a)-1):
#         min_idx = i
#         for j in range(i+1, len(a)):
#             if a[min_idx] > a[j]:
#                 min_idx = j
#         a[i], a[min_idx] = a[min_idx], a[i]
#     return a

import sys
N = int(sys.stdin.readline())
for num in SelectionSort([int(sys.stdin.readline()) for _ in range(N)]):
    print(num)