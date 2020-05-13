n, m = map(int, input().split())
var = input().split()
print(var)
numList = sorted([int(x) for x in var], reverse = True)
print(numList)

# 그럼 그 중에서 최대 x+y+z를 출력하면 되지 않는가?
answer = []
for x in numList:
    for y in numList:
        if y != x and y <= x:
            for z in numList:
                if z != x and z != y and z <= y and x+y+z<=m:
                    answer.append(x+y+z)
print(max(answer))

# x+y+z가 m보다 작거나 같을 때만 출력하라고 조건 추가해보면? -> 잘 나온다.

# for x in numList:
#     for y in numList:
#         if y != x and y <= x:
#             for z in numList:
#                 if z != x and z != y and z <= y and x+y+z<=m:
#                     print(x,y,z, x+y+z)

# 순서대로 경우의 수

# for x in numList:
#     for y in numList:
#         if y != x and y <= x:
#             for z in numList:
#                 if z != x and z != y and z <= y:
#                     print(x,y,z, x+y+z)


# 모든 경우의 수
# for x in numList:
#     for y in numList:
#         if y!= x:
#             for z in numList:
#                 if z != x and z != y:
#                     print(x, y, z)
