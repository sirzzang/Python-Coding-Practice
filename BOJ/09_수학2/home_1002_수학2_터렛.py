# 이건 틀린 건데 -> 반례가 뭔가?!!!!
# https://mathbang.net/101 : 1, 2, 3, 4, 5, 6의 경우 있음
# (1) 두 점에서 만나는 경우
### (2) 한 점에서 만나는데 외접하는 경우
### (3) 한 점에서 만나는데 내접하는 경우
### (4) 만나지 않는데, 아예 바깥에 서로 다르게 있는 경우
### (5) 만나지 않는데, 한 원이 다른 원 안에 있고, 중심이 일치하지 않는 경우
### (6) 만나지 않는데, 한 원이 다른 원 안에 있고, 중심이 일치하는 경우
### (7) 일치하는 경우


T = int(input())

for _ in range(T):    
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x1-x2)**2 +(y1-y2)**2)**0.5

    if x1 == x2 and y1 == y2:
        if r1 == r2: # (7)
            print(-1)
        else: # (6)
            print(0)
    else:
        if distance == (r1+r2): # (2)
            print(1)
        elif distance == abs(r1-r2): # (3)
            print(1)
        elif distance > (r1+r2): # (4)
            print(0)
        elif distance < abs(r1-r2): # (5)
            # 큰 원의 반지름에서 작은 원의 반지름을 뺀 것이 중심 간 거리보다 커야 함
            print(0)
        else: # (1)
            print(2)


# 왜 틀렸지??? -> 원의 위치관계 다시 꼼꼼하게 생각해보자.
# 헛 미친 경우의 수를 나눠보자
# 만나는 경우
# 2개로 만나는 경우 : 반지름 합 > 거리
# 1개로 만나는 경우 : 반지름 합 = 거리
# 무한대로 만나는 경우: 아예 동일
# 안 만나는 경우 : 반지름 합 < 거리/ 지름 똑같은데 아닌 경우

# T = int(input())

# for _ in range(T):    
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())
#     distance = ((x1-x2)**2 +(y1-y2)**2)**0.5

#     if x1 == x2 and y1 == y2:
#         if r1 == r2:
#             print(-1)
#         else:
#             print(0)
#     else:
#         if distance < (r1+r2):
#             print(2)
#         elif distance == (r1+r2):
#             print(1)
#         else:
#             print(0)


# 시간초과
# 어차피 range로 할 게 아니라 그냥 원주에 있는 애들 대상으로 하면 되는 거 아닌가?

# T = int(input())
# for _ in range(T):
#     answerList = []
#     a, b, c, d, e, f = map(int, input().split())
#     if a == d and b == e:
#         if c == f:
#             print(-1)
#         else:
#             print(0)
#     else:    
#         xStandard_min = min([a-c, a+c, d-f, d+f])
#         xStandard_max = max([a-c, a+c, d-f, d+f])
#         yStandard_min = min([b-c, b+c, e-f, e+f])
#         yStandard_max = max([b-c, b+c, e-f, e+f])
#         for x in range(xStandard_min, xStandard_max+1):
#             for y in range(yStandard_min, yStandard_max+1):
#                 if ((x-a)**2+(y-b)**2)**0.5 == c and ((x-d)**2+(y-e)**2)**0.5 == f:
#                     answerList.append((x,y))
#         print(len(answerList))

