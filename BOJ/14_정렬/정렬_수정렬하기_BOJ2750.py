# 1000까지 주어지는 경우, 버블정렬 시간복잡도 1000000까지 갈 수 있으나.

import sys

def BubbleSort(a):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]

for ele in BubbleSort(arr):
    print(ele)



# 그냥 풀기

# 가변 변수 인자

# import sys
# n, *x = map(int, sys.stdin.read().split())

# print(n)
# print(x)
# print(type(x))

# for num in sorted(x):
#     print(num)


# # 삽입정렬 알고리즘 - 리스트 사용

# N = int(input())
# numList = []
# for _ in range(N):
#     numList.append(int(input()))

# for i in range(1, len(numList)):
#     for j in range(i, 0, -1):
#         if numList[j] < numList[j-1]:
#             numList[j], numList[j-1] = numList[j-1], numList[j]
#         else:
#             break

# for num in numList:
#     print(num)
