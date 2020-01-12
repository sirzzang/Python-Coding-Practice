# 재귀 활용 메모

dictionary = {}          # 결과 메모할 dictionary 생성

# 함수 선언
def memo_factorial(n):
    if n in dictionary:     # n(key이 dictioary 안에 있다면
        return dictionary[n]        # 그 n(key)의 값(value)를 return하라
    if n == 0:      # n = 0일 때 1 return하고 저장
        return 1
    if n == 1:      # n = 1일 때 1 return하고 저장
        return 1
    elif n>=2:           # 그 외에는 result = n * factorial(n-1)이고,그 result값을 dictioanry의 n번째 칸에 저장
        result = n * memo_factorial(n-1)
        dictionary[n] = result
        return result

n = int(input())    # 입력값 : n>=0인 정수

print(memo_factorial(n))    # 출력값 : factorial 값



# 재귀 활용(메모 있음)

# dictionary = {}

# def factorial(n):
#     if n in dictionary:
#         return dictionary[n]
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     else:
#         output = n * factorial(n-1)
#         dictionary[n] = output
#         return output

# n = int(input())
# print(factorial(n))


# 재귀 활용한 방법(메모 없음)

# n = int(input())    # 첫째 줄에 0 이상인 정수 n이 주어진다

# def recursive_factorial(n):
#     if n == 0:      # 0일 때는 1
#         return 1
#     if n == 1:      # 1일 때도 1
#         return 1
#     elif n > 1:     # 재귀
#         return n * recursive_factorial(n-1)

# print(recursive_factorial(n))   # 출력해라

# 과정

# n = 1: recursive_factorial(1) = 1
# n = 2: recursive_factorial(2) = 2 * recursive_factorial(1) = 2*1 
# n = 3 : recursive_factorial(3) = 3 * recursive_factorial(2) = 3*2*1

# # 재귀 활용한 방법

# def factorial(n):
#     if n == 1:
#         return 1
#     elif n>1:
#         return n * factorial(n-1)

# n = int(input())
# print(factorial(n))




# for문 활용한 방법

# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result = result * i
    
#     return result

# n = int(input())
# print(factorial(n))
 