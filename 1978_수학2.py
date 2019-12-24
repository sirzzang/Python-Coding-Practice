# 소수 찾기
# -> 이건 2, 3을 절대 찾을 수가 없는.. : break 위치
# -> 4


# n = int(input())
# primeList = []

# for _ in range(n):
#     num = int(input())
#     if num == 1:
#         pass
#     else:
#         for i in range(2, num//2 + 1):
#             if num % i == 0:
#                 break
#         else:
#             primeList.append(num)
    
# print(primeList)


# num = 4
  
# # If given number is greater than 1 
# if num > 1: 
      
#    # Iterate from 2 to n / 2  
#    for i in range(2, num//2): 
         
#        # If num is divisible by any number between  
#        # 2 and n / 2, it is not prime  
#        if (num % i) == 0: 
#            print(num, "is not a prime number") 
#            break
#    else: 
#        print(num, "is a prime number") 
  
# else: 
#    print(num, "is not a prime number") 

import sys

user_input = sys.stdin.readlines()
s = user_input[-1].strip('\n')
var = [int(x) for x in s.split()]

prime_list = []
for i in var:
    
    nCount = 0
    for x in range(1, i+1):
        if i % x == 0:
            nCount += 1
    if nCount == 2:
        prime_list.append(i)

print(len(prime_list))


# def myPrime(x):
    
#     i = 1
#     prime_list = []
#     while i < x:     
#         nCount = 0
#         for idx in range(1, x+1):
#             if i % idx == 0:
#                 nCount +=1
#         if nCount == 2:
#             prime_list.append(i)   
#         i += 1

#     return len(prime_list)

# print(myPrime(1000))