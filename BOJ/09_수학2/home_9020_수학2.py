# 시간초과 개선 방안 : ㅠㅠㅠㅠㅠ 드디어 맞았다...
# 0) input 대신 sys 사용.
# 1) 미리 문제의 조건에 맞는 소수 모두 구해놓는다.

import sys

numSet = set(range(2, 10001))
for i in range(2, int(10001**0.5)+2):
    numSet -= set(range(2*i, 10001, i))
primeList = list(sorted(numSet))

# 2) 주어진 짝수가 있고,
# - 그 짝수를 2로 나눈 몫이 primeList에 있으면 그 수와 나머지를 출력하고
# - 아니면 while loop 이용해서 2로 나눈 몫에서 1씩 줄여나가며 찾는다.

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    idx = 0
    while True:
        if (n//2-idx) in primeList and (n-(n//2-idx)) in primeList:
            print(n//2-idx, n-(n//2-idx))
            break
        idx += 1



# t = int(input())                                       # 첫 줄 입력

# for _ in range(t):
#     n = int(input())                            
#     numSet = set(range(2, n+1))                        # 입력되는 수보다 작은 소수 list 구하기
#     for i in range(2, int(n**0.5)+2):
#         numSet -= set(range(2*i, n+1, i))
#     primeList = list(sorted(numSet))

#     answerList = []
#     for x in primeList:                                 # 소수 list 내의 한 원소 x, n-x =y
#         if x<=(n/2) and (n-x) in primeList:             # x가 n/2보다 작거나 같고, y가 소수 list에 있으면 answerlist에 넣기
#             answerList.append((x,n-x))
#     print(*answerList[-1])                              # 그 중 가장 마지막에 있는 tuple을 unpack하여 출력


# 이렇게 해도 시간초과;;;

# t = int(input())                                       # 첫 줄 입력

# for _ in range(t):
#     n = int(input())                            
#     numSet = set(range(2, n+1))                        # 입력되는 수보다 작은 소수 list 구하기
#     for i in range(2, int(n**0.5)+2):
#         numSet -= set(range(2*i, n+1, i))
#     primeList = list(sorted(numSet))

#     answerList = []
#     for x in primeList:                                 # 소수 list 내의 한 원소 x, n-x =y
#         if x<=(n/2) and (n-x) in primeList:             # x가 n/2보다 작거나 같고, y가 소수 list에 있으면 answerlist에 넣기
#             answerList.append((x,n-x))
#     print(*answerList[-1])                              # 그 중 가장 마지막에 있는 tuple을 unpack하여 출력



# tuple index 있나 -> ㅇㅋ

# myTuple = (3, 4)
# print(type(myTuple))
# print(myTuple[0])

# n = 12

# 일단 n을 2로 나눈 몫이 짝수이면 그 수에서 1 뺀 게 x, 나머지가 y
# n을 2로 나눈 몫이 홀수이면 


# 그냥 애초에 그거 이하 홀수를 다 구해놓는 것은..?

# n = int(input())

# numSet = set(range(2, n+1))
# print(numSet)
# for i in range(2, int(n**0.5)+2):                   # 소수 list 구하고
#     numSet -= set(range(2*i, n+1, i))   
# primeList = list(sorted(numSet))
# print(primeList)    

# answerList = []
# for x in primeList:                                 # 소수 list에 들어 있는 애들 중
#     if x <= (n/2) and (n-x) in primeList :          # x를 n의 절반보다 작은 애라고 하고, n에서 x 뺀 게 소수 list에 있으면
#         answerList.append((x, n-x))                 # 그걸 answerlist에 넣고
# print(answerList)
# print(*answerList[-1])                              # 그 중에 가장 마지막 원소를 뽑으면 된다. 그래야 차가 최소일테니. -> 출력형식 맞추기 위해 unpacking.

