a, b = map(int, input().split())
while True:
    if a == 0 and b == 0:
        break
    else:
        print(a+b)
        a, b = map(int, input().split())

# n, x = map(int, input().split())
# user_input = input().split()
# for i in user_input:
#     if int(i) < x:
#         print(int(i), end=' ')



# import sys
# t = int(sys.stdin.readline())

# for _ in range(t):
#     n = int(sys.stdin.readline())
#     x = int(n/2)
#     y = int(n - x)
#     nCount = 0
#     while True:
#         for j in range(1, x+1):
#             if x % j == 0:
#                 nCount += 1
#         if nCount == 2:
#             mCount = 0
#             for i in range(1, y+1):
#                 if y % j == 0:
#                     mCount += 1
#             if mCount == 2:
#                 print("{} {}".format(x, y))
                
#         else:
#             x -= 1
#             y = n - x
#             nCount = 0
#             mCount = 0


# # import sys
# # user_input = sys.stdin.readlines()
# # var = [int(x.strip('\n')) for x in user_input]

# # for i in range(1, len(var)):
# #     n = var[i]
# #     x = int(n/2)
# #     y = int(n - x)
# #     nCount = 0
# #     while True:
# #         for j in range(1, x+1):
# #             if x % j == 0:
# #                 nCount += 1
# #         if nCount == 2:
# #             print("{} {}".format(x, y))
# #             break
# #         else:
# #             x -= 1
# #             y = n - x
# #             nCount = 0



# # # for _ in range(t):
# # #     n = int(input())

# # #     x = int(n / 2)
# # #     y = int(n - x)

# # #     nCount = 0

# # #     while True:
# # #         for i in range(1, x+1):
# # #             if x % i == 0:
# # #                 nCount += 1
# # #         if nCount == 2:
# # #             print("{} {}".format(x, y))
# # #             break
# # #         else:
# # #             x -= 1
# # #             y = n - x
# # #             nCount = 0






# # # def myPrime(m, n):
    
# # #     nCount = 1
# # #     factor = 2

# # #     for x in range(m, n+1):
        
# # #         while True:
# # #             if x % factor == 0:
# # #                 x = x / factor
# # #                 nCount += 1
# # #             else:
# # #                 factor += 1
# # #             if x == 1:
# # #                 break
        
# # #         if nCount == 2:
# # #             print(x)
    
# # #     return

# # # myPrime(3, 16)