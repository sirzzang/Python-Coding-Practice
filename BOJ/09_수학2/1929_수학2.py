# # map, input 사용해서.

m, n = map(int, input().split())

numSet = set(range(m, n+1))

if m == 1:
    m = m+1

for i in range(2, int(n**0.5)+2):
    numSet -= set(range(2*i, n+1, i))
    numList = sorted(list(numSet))

for num in numList:
    print(num)

# 코드 

# m = int(input())
# n = int(input())

# numSet = set(range(m, n+1))


# for i in range(2, int(n**0.5)+2):
#     numSet -= set(range(2*i, n+1, i))

# for num in numSet:
#     print(num)


# 시간초과

# m = int(input())
# n = int(input())

# for i in range(m, n+1):
    
#     factor = 2
    
#     while factor <= (i**0.5):
#         if i % factor == 0:
#             break

#         print(i %factor)


#         # if i % factor == 0:
#         #     factor += 1
#         # else:
#         #     break
#         # print(i)




        # if i % factor == 0:
        #     break
        # else:
        #     factor += 1
        #     if factor > (i**0.5):
        #        print(i)


# # 시간초과


# import sys

# user_input = sys.stdin.readline().strip('\n')
# m = int(user_input.split()[0])
# n = int(user_input.split()[-1])

# if m == 1:
#     m = m+1

# else:
#     for i in range(m, n+1):
#         factor = 2
#         while True:
#             if i % factor == 0:
#                 break
#             else:
#                 factor += 1
#         if factor > (i**0.5):
#             print(i)




# import sys

# user_input = sys.stdin.readline().strip('\n')
# m = int(user_input.split()[0])
# n = int(user_input.split()[-1])

# if m == 1:
#     m = m+1

# for i in range(m, n+1):
#     nCount = 1
#     factor = 2

#     while True:
        
#         if i % factor == 0:
#             i = i / factor
#             nCount += 1
#             if nCount == 2:
#                 break
#         else:
#             factor += 1
    
#     print(i)