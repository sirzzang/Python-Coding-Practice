# 엉엉엉엉......

numList = [True] * (123456*2)
for i in range(2, int((123456*2)**0.5)+1):
    if numList[i] == True:
        for j in range(2*i, 123456*2, i):
            numList[j] = False
primeList = [i for i in range(2, 123456*2) if numList[i] == True]

n = int(input())

while True:
    if n == 0:
        break
    else:
        answer = [x for x in primeList if x > n and x <= 2*n]
        print(len(answer))
        n = int(input())

# 이것도 아니다
# 애초에 에라스토테네스의 체 방식이 잘못된 것 같음.

# numSet = set(range(2, 123457*2))
# for i in range(2, int((1234567*2)**0.5)):
#     numSet -= set(range(2*i, 123457*2, i))

# n = int(input())
# primeList = []
# while True:
#     if n == 0:
#         break
#     else:
#         for x in numSet:
#             if x >= n and x <= 2*n:
#                 primeList.append(x)
#         print(len(primeList))
#         n = int(input())
#         primeList = []


# # 이렇게 하면 1일 때 numSet이 2가 아니라 1이 된다.
# # 일단 개수만 구할 때는 상관은 없는데.

# # n = int(input())

# # while True:
# #     if n == 0:
# #         break
# #     elif n == 1:
# #         n = n + 1
# #         numSet = set(range(n, 2*n +1))
# #         for i in range(2, int((2*n)**0.5)+2):
# #             mySet = set(range(2*i, 2*n +1, i))
# #             numSet -= mySet
# #         print(len(numSet))
# #         n = int(input())
# #     else:
# #         numSet = set(range(n, 2*n +1))
# #         for i in range(2, int((2*n)**0.5)+2):
# #             mySet = set(range(2*i, 2*n +1, i))
# #             numSet -= mySet
# #         print(len(numSet))
# #         n = int(input())


# # 2, 3에서 자꾸 틀린다.

# # n = int(input())

# # while True:
# #     if n == 0:
# #         break
# #     elif n == 1:
# #         print(1)
# #         n = int(input())
# #         continue
# #     elif n == 2:
# #         print(2)
# #         n = int(input())
# #         continue
# #     else:
# #         numSet = set(range(n, 2*n +1))
# #         for i in range(2, int((2*n+1)**0.5)+2):
# #             mySet = set(range(i, 2*n +1, i))
# #             numSet -= mySet
# #         print(numSet)
# #         print(len(numSet))
# #         n = int(input())


# numSet = set(range(2, 246913))
# for i in range(2, int(246913**0.5)+2):
#     numSet -= set(range(2*i, 246913, i))

# n = int(input())

# while True:
#     if n == 0:
#         break
#     else:
#         for x in numSet:
#             if x < n and x >= 2*n:
#                 primeSet = numSet.remove(x)
#                 print(len(primeSet))
#     n = int(input())
 

# 한 번에 입력을 받는 건가?
# # 입력 복사해서 넣어보면 그것도 아님...

# import sys

# user_input = sys.stdin.readlines().strip('\n')
# print(user_input)
# print(type(user_input))


# numSet = set(range(2, 246913))
# for i in range(2, int(246913**0.5)+2):
#     numSet -= set(range(2*i, 246913, i))

# n = int(input())
# primeList = []
# while True:
#     if n == 0:
#         break
#     else:
#         for x in numSet:
#             if x >= n and x <= 2*n:
#                 primeList.append(x)
#         print(len(primeList))
#         n = int(input())
#         primeList = []



# 질문 검색했더니 
# 1부터 246913까지 전부 다 저장해놓고 뽑으라고 해서
# 그렇게 뽑았더니 또 틀렸어 시댕...

# numSet = set(range(2, 246913))
# for i in range(2, int(246913**0.5)+2):
#     numSet -= set(range(2*i, 246913, i))

# n = int(input())
# primeList = []
# while True:
#     if n == 0:
#         break
#     else:
#         for x in numSet:
#             if x >= n and x <= 2*n:
#                 primeList.append(x)
#         print(len(primeList))
#         n = int(input())
#         primeList = []


# # 이렇게 하면 1일 때 numSet이 2가 아니라 1이 된다.
# # 일단 개수만 구할 때는 상관은 없는데.

# # n = int(input())

# # while True:
# #     if n == 0:
# #         break
# #     elif n == 1:
# #         n = n + 1
# #         numSet = set(range(n, 2*n +1))
# #         for i in range(2, int((2*n)**0.5)+2):
# #             mySet = set(range(2*i, 2*n +1, i))
# #             numSet -= mySet
# #         print(len(numSet))
# #         n = int(input())
# #     else:
# #         numSet = set(range(n, 2*n +1))
# #         for i in range(2, int((2*n)**0.5)+2):
# #             mySet = set(range(2*i, 2*n +1, i))
# #             numSet -= mySet
# #         print(len(numSet))
# #         n = int(input())


# # 2, 3에서 자꾸 틀린다.

# # n = int(input())

# # while True:
# #     if n == 0:
# #         break
# #     elif n == 1:
# #         print(1)
# #         n = int(input())
# #         continue
# #     elif n == 2:
# #         print(2)
# #         n = int(input())
# #         continue
# #     else:
# #         numSet = set(range(n, 2*n +1))
# #         for i in range(2, int((2*n+1)**0.5)+2):
# #             mySet = set(range(i, 2*n +1, i))
# #             numSet -= mySet
# #         print(numSet)
# #         print(len(numSet))
# #         n = int(input())

# # # # 제곱수가 안 빠짐.
# # # n = int(input())

# # # while True:
# # #     if n == 0:
# # #         break
   
# # #     else:
# # #         numSet = set(range(n, 2*n +1))
# # #         print(numSet)
# # #         for i in range(2, int(n**0.5)+2):
# # #             print(i)
# # #             mySet = set(range(i, 2*n +1, i))
# # #             print(mySet)
# # #             numSet -= mySet
# # #         print(numSet)
# # #         print(len(numSet))
# # #         n = int(input())