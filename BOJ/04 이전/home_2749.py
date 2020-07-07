# dictionary 이용하면?


# 이렇게 해도 런타임에러가 난다.

# import sys

# n = int(sys.stdin.readline())

# fibList = [0] * (n+1)
# fibList[1] = 1

# for i in range(2, n+1):
#     fibList[i] = fibList[i-1] + fibList[i-2]
# print(fibList[-1] % 1000000)


# 이거 재귀함수로 하면 재귀 깊이 오류 난다.
# RecursionError: maximum recursion depth exceeded in comparison

# import sys

# n = int(sys.stdin.readline())

# dictionary = {}

# def fib(n):
#     if n in dictionary:
#         return dictionary[n]
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n >= 2:
#         result = fib(n-1) + fib(n-2)
#         dictionary[n] = result
#         return result
    
# print(fib(n))
# print(fib(n)%1000000)
