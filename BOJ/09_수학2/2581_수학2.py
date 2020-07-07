m = int(input())
n = int(input())

primeList = []

for i in range(m, n+1):
    
    nCount = 0

    for x in range(1, i+1):
        if i % x == 0:
            nCount += 1
    if nCount == 2:
        primeList.append(i)

if len(primeList) == 0:
    print(-1)
else:
    print(sum(primeList))
    print(primeList[0])
    




# 밑에 코드 런타임에러

# for i in range(m, n+1):

#     nCount = 1
#     factor = 2
#     x = i

#     while True:
        
#         if x % factor == 0:
#             x = x / factor
#             nCount += 1
#         else:
#             factor += 1
#         if x == 1:
#             break
    
#     if nCount == 2:
#         myNum += i

# if len(primeList) == 0:
#     print(-1)
# else:
#     print(sum(primeList))

# print(min(primeList))


# # 소수 판별
# def myPrime(x):
    
#     nCount = 1
#     factor = 2
    
#     while True:
#         if x % factor == 0:
#             x = x / factor
#             nCount += 1
#         else:
#             factor += 1
#         if x == 1:
#             break
    
#     if nCount == 2:
#         print("소수입니다.")
#     else:
#         print("아닙니다.")
    
#     return

# myPrime(4)



# 틀린 답변 1
# while을 계속 돌려야 하니까 시간이..

# # 시간초과...

# m = int(input())
# n = int(input())

# prime_list = []

# for i in range(m, n+1):
    
#     nCount = 0
#     for x in range(1, i+1):
#         if i % x == 0:
#             nCount += 1
#     if nCount == 2:
#         prime_list.append(i)

# if len(prime_list) == 0:
#     print(-1)
# else:
#     print(sum(prime_list))

# print(min(prime_list))
