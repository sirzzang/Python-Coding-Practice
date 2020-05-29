def fib(n):

    if n in fib_dict_:
        return fib_dict_[n]

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        fib_dict_[n] = fib(n-1) + fib(n-2)
        return fib_dict_[n]

def solution(n):
    if n == 0:
        return "1 0"
    elif n == 1:
        return "2 0"
    elif n == 2:
        return "1 1"
    else:
        fib(n)
        return f"{fib_dict_[n]} {fib_dict_[n-1]}"


fib_dict_ = {}

n = int(input())
print(solution(n))