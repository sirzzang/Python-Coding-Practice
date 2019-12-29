import time
start = time.time()

# 생각해보면
# 일단 H * W = 방 전체 개수
# n번째로 도착한 손님 h로 모듈라해서 나온 나머지가 층수가 됨 -> YY
# (n-1)을 h로 나눈 몫에 1 더한 게 엘리베이터로부터 세었을 때의 번호가 됨. -> XX

# 즉, 나머지 + 몫

# 아 미친;;;
# 30, 60 등일 때.

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    distance = ((n - 1) // h) + 1
    if n % h == 0:
        floor = h
    else:
        floor = n % h
    room_number = 100 * floor + distance
    print(room_number)


import sys
user_input = sys.stdin.readlines()

for x in user_input[1:]:
    h, w, n = map(int, x.strip('\n').split())
    distance = ((n - 1) // h) + 1
    if n % h == 0:
        floor = h
    else:
        floor = n % h
    room_number = 100 * floor + distance
    print(room_number)



# 틀린 코드2
# 입력의 문제가 아니다!


# t = int(input())
# for _ in range(t):
#     h, w, n = map(int, input().split())
#     floor = n % h
#     distance = ((n - 1) // h) + 1
#     room_number = 100 * floor + distance
#     print(room_number)


# 틀린 코드1

# 맞은 것 같은데 왜때문에?
# h, w, n = map(int, input().split())

# import sys
# user_input = sys.stdin.readlines()

# for x in user_input[1:]:
#     h, w, n = map(int, x.strip('\n').split())
#     floor = n % h
#     distance = ((n - 1) // h) + 1
#     room_number = 100 * floor + distance
#     print(room_number)
    



# floor = n % h
# distance = ((n - 1) // h) + 1
# answer = 100 * floor + distance
# print(answer)

# 엘베로부터의 번호가 10 이상이 될 수 있나??? ㅇㅇ 그렇지.





print("time :", time.time() - start)