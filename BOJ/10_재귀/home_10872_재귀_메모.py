# 메모하는 방법
# 이렇게 하면 근데 메모했을 때 n=0, n=1일 때는 저장 안되지 않나?
# ㅇㅇ. keyerror뜬다. 애초에 key로 저장하니까, key를 2부터 저장하는듯.

dictionary = {}             # 메모할 dictionary

def fibonacci(n):

    if n in dictionary:
        return dictionary[n]
    if n == 0 :             # 0일 때는 0
        return 0
    elif n == 1 :           # 1일 때는 1
        return 1
    elif n >= 2:             # 2일 때부터는 앞의 두 수 더한 값
        result = fibonacci(n-1) + fibonacci(n-2) 
        dictionary[n] = result               
        return result

n = int(input())
print(fibonacci(n))


# 2. 아래처럼 짰을 때
# 오류 NameError: name 'fibonacci' is not defined
# 왜???
# def fibonnaci(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     elif n >= 3:
#         fibonacci(n-1) + fibonnaci(n-2)
#         return fibonacci(n)

# print(fibonacci(3))

# 1. 아래처럼 짰을 때:
# 오류 SyntaxError: cannot assign to function call
# def fibonnaci(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     elif n >= 3:
#         fibonacci(n-1) + fibonnaci(n-2)
#         return fibonacci(n)

# print(fibonacci(3))