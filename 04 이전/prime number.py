# 에라토스테네스의 체

# n개 요소에 True 설정 => 소수로 간주.
# n의 최대 약수는 n의 제곱근 이하이므로 i = n의 제곱근까지 검사.
# i가 소수인경우
# i 이후 i의 배수들을 false 판정
# 소수 목록 산출

n = int(input())
numList = [True] * n
m = int(n**0.5)
for i in range(2, m+1):
    if numList[i] == True:
        for j in range(2*i, n, i):
            numList[j] = False
print(numList)
primeList = [i for i in range(2, n) if numList[i]==True]
print(primeList)

# 소수 판별 함수


# def myPrime(m, n):
    
#     nCount = 1
#     factor = 2

#     for x in range(m, n+1):
        
#         while True:
#             if x % factor == 0:
#                 x = x / factor
#                 nCount += 1
#             else:
#                 factor += 1
#             if x == 1:
#                 break
        
#         if nCount == 2:
#             print(x)
    
#     return

# myPrime(3, 16)