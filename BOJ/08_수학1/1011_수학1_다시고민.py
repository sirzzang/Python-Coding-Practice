# 일단 이렇게 하면 -2해주면 될 것 같긴한데?

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
        
    d = 1
    result = 0
    distance = (y-x)

    while True:
        
        if distance >= d:
            result += 1
            d += (result//2)            
        else:
            break

    print(result-1)


# import sys
# T = int(sys.stdin.readline())

# for _ in range(T):
#     x, y = map(int, sys.stdin.readline().split())

#     distance = 1
#     result = 1

#     while True:
#         if distance < (y-x) + 1:
#             result += (distance//2)
#             distance += 1
#         else:
#             break

#     print(result)


# 오케. 이러면 거리별로 나온다.

# x = int(input())
# y = int(input())

# distance = 1    # y-x와 같은 값: d = 22라고 친다면
# result = 1

# while True:
#     if distance < (y-x) + 1:
#         result += (distance//2)
#         distance += 1
#     else:
#         break
# print(result)




# d =22일 때 result = 122

# d = 1
# n = int(input())

# while True:
#     if result <= n :
#         result += (d//2)
#         d += 1
#     else:
#         break
# print(result)
# print(d)