# 재귀함수 사용하는 방법

dictionary = {}

def Fib(n):
    if n in dictionary:
        return dictionary[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n >= 2:
        result = Fib(n-1) + Fib(n-2)
        dictionary[n] = result
        return result

n = int(input())

print(Fib(n))    

#################################################################

# 재귀함수 사용하지 않는 방법

# n = int(input())
# fibList = [0] * (n+1)
# fibList[1] = 1

# for i in range(2, n+1):
#     fibList[i] = fibList[i-1] + fibList[i-2]
# print(fibList[-1])

# 이렇게 해도 여전히 list index assignment out of range
# 아 이렇게 하면, list index가 당연히 n-1번째까지 생기고
# 그러면 i도 당연히 n-1까지 들어가야 한다
# 그 앞에까지 다 되다가 마지막에서 안 된다.


#####################################################################


# n = int(input())
# fibList = [0] * n)
# fibList[1] = 1

# for i in range(2, n+1):
#     fibList[i] = fibList[i-1] + fibList[i-2]
# print(fibList[-1])



# append 방법 써보면?
# 역시나.. 안됨.

# n = int(input())

# fibList = [0, 1]
# for i in range(2, n+1):
#     fibList[i] = fibList[i-1] + fibList[i-2]
#     fibList.append(fibList[i])
# print(fibList)


# 이것도 index out of range

# for i in range(2,n+1):
#     fibList[i] = fibList[i-1] + fibList[i-2]
# print(fibList)


# 이렇게 되면 list index out of range
# # 디버깅 하니까: 당연히 n = 45넣었으니까 list index 이상해짐.
# n = int(input())

# fibList = [0, 1]

# for i in range(2,n+1):
#     fibList[n] = fibList[n-1] + fibList[n-2]
# print(fibList)

# # keyerror 난다

# fibonacci = {}

# n = int(input())

# if n == 0 :
#     fibonacci[n] = 0
# elif n == 1:
#     fibonacci[n] = 1
# elif n >= 2:
#     fibonacci[n] = fibonacci[n-1] + fibonacci[n-2]

# print(fibonacci(n))

