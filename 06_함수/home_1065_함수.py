# 0. 어떤 수에 대해서, 그 수가 한수인지 판별

# n = input()
# diffList = []
# for i in range(len(n)-1):
#     diff = int(n[i])-int(n[i+1])
#     diffList.append(diff)

# if len(set(diffList)) == 0 or len(set(diffList)) == 1:
#     print("한수")
# else:
#     print("아니야")

# 1. 어떤 수보다 작은 모든 수에 대해서, 그 수가 한수인지 판별.

# n = input()
# numList = list(range(1, int(n) + 1))

# for num in numList:
#     diffList = []
#     for i in range(len(str(num))-1):
#         diff = int(str(num)[i]) - int(str(num)[i+1])
#         diffList.append(diff)
#     checkNum = len(set(diffList))
#     if checkNum == 0 or checkNum == 1:
#         print("한수")

# 2. 어떤 수보다 작은 모든 수에 대해서, 그 수가 한수인지 판별하고, 개수 세기.

# n = input()
# numList = list(range(1, int(n) + 1))
# nCount = 0
# for num in numList:
#     diffList = []
#     for i in range(len(str(num))-1):
#         diff = int(str(num)[i]) - int(str(num)[i+1])
#         diffList.append(diff)
#     checkNum = len(set(diffList))
#     if checkNum == 0 or checkNum == 1:
#         nCount += 1
        
# print(nCount)

# 3. 함수로 구현하기

# def hansu(n):
#     numList = list(range(1, n + 1))
#     nCount = 0
#     for num in numList:
#         diffList = []
#         for i in range(len(str(num))-1):
#             diff = int(str(num)[i]) - int(str(num)[i+1])
#             diffList.append(diff)
#         checkNum = len(set(diffList))
#         if checkNum == 0 or checkNum == 1:
#             nCount += 1
            
#     return print(nCount)

# hansu(150)

# 4. 입력값 받으면 돌려주는 애 구하기


def hansu(n):
    numList = list(range(1, n + 1))
    nCount = 0
    for num in numList:
        diffList = []
        for i in range(len(str(num))-1):
            diff = int(str(num)[i]) - int(str(num)[i+1])
            diffList.append(diff)
        checkNum = len(set(diffList))
        if checkNum == 0 or checkNum == 1:
            nCount += 1
            
    return print(nCount)

x = int(input())
hansu(x)

