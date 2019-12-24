import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    boolList = [True] * n
    for i in range(2, int(n**0.5)+1):
        if boolList[i] == True:
            for j in range(2*i, n, i):
                boolList[j] = False
    primeList = [i for i in range(2, len(boolList)) if boolList[i] == True]

    m = int(len(primeList)/2)-1

    x = primeList[m]
    y = n - x

    if n == 6:
        print("3 3")
    else:
        while True:
            if y in primeList:
                print("{} {}".format(x, y))
                break
            else:
                x = primeList[m-1]        
                y = n-x





# n보다 작은 소수 다 출력해놓고
# n/2 - 1 x부터 시작해서 그 안에 있으면???
# 이렇게 하면 4 되고, 8, 10, ... 되는데
# 6이 안된다.

# 시간초과

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     boolList = [True] * n
#     for i in range(2, int(n**0.5)+1):
#         if boolList[i] == True:
#             for j in range(2*i, n, i):
#                 boolList[j] = False
#     primeList = [i for i in range(2, len(boolList)) if boolList[i] == True]

#     m = int(len(primeList)/2)-1

#     x = primeList[m]
#     y = n - x


#     if x == 2:
#         m = m + 1
#         x = primeList[m]
#         y = n - x
#         if y in primeList:
#             print("{} {}".format(x, y))
#     else:
#         while True:
#             if y in primeList:
#                 print("{} {}".format(x, y))
#                 break
#             else:
#                 x = primeList[m-1]        
#                 y = n-x
        

# x = int(n / 2 - 1)
# y = int(n - x)

# print(x)
# print(y)

# # x가 소수이고, y가 소수이면 x, y 출력
# # 아니면 x 2 작게, y 2 크게
# # x = 2가 되는순간 x = 2, y = n-x

# xList = [True] * x
# for i in range(2, int(x**0.5)+1):
#     if xList[i] == True:
#         for j in range(2*i, x+1, i):
#             xList[j] = False
# xPrimeList = [i for i in range(2, x) if xList[i] == True]
# print(xPrimeList)




# numSet = set(range(2, x+1))
# for i in range(2, x+1):
#     numSet -= set(range(2*i, x+1, i))
# print(numSet)