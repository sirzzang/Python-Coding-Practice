import time
start = time.time()


a, b, v = map(int, input().split())
day_spent = (v-b)//(a-b)
print(day_spent if day_spent == int(day_spent) else int(day_spent) + 1)


# 망한 코딩4

# 이렇게 되면 4 2 9일때처럼... 3.5 같이 분수 나오면 ㄴㄴ
# 그냥 while문 쓰지 말고 구해보자
# 애초에 달팽이는 올라가기만 하면 밤을 보내지 않을테니
# 올라가야 할 높이는 v-b
# 하루에 올라가는 양은 a-b

a, b, v = map(int, input().split())
day_spent = (v-b)//(a-b)
print((v-b)//(a-b))


# 망한 코딩 3
# while문을 쓰면 자꾸 시간초과가 나나봐ㅠㅠㅠ


# 애초에 a-b가 v-b보다 크기만 하면 된다.
# 애초에 조건에서 b<a<=v
# a=v라면 그냥 끝나버림 : a-b >= v-b일테니
# 그게 아니라고 하더라도 n(a-b) = v일 때 끝날텐데



# import sys

# user_input = sys.stdin.readline().split()
# a = int(user_input[0])
# b = int(user_input[1])
# v = int(user_input[2])
# # a, b, v = map(int, input().split())

# n = 0

# while True:
#     n += 1
#     if (a-b)*n >= v-b:
#         break    
# print(n)


# 망한 방법
# 시간 초과

# a, b, v = map(int, input().split())

# n = 0

# while True:
#     n += 1
#     if a*n - b*(n-1) >= v:
#         break    
# print(n)

# 망한 방법
# 답은 나오는데 자꾸 시간 초과가 뜬다

# import sys

# user_input = sys.stdin.readline().split()
# a = int(user_input[0])
# b = int(user_input[1])
# v = int(user_input[2])

# days_spent = 1

# if a >= v:              # 첫 날에 그냥 낮에 올라가는 높이가 1보다 크다면 그냥 올라가버리면 됨.
#     print(1)

# else:
#     height = a - b                 # 초기 시작 높이는 1일차 낮에 올라갔다가 미끄러진 만큼.

#     while True:

#         days_spent += 1         # 둘째 날부터 시작 -> 2일차 낮.
#         day_height = height + a   # 둘째날 낮에 a만큼 올라감.
        
#         if day_height >= v:       # 낮에 올라간 높이가 정상보다 높으면 그냥 끝내면 됨.
#             break

#         height = day_height - b   # 그게 아니라면 b만큼 미끄러짐.
     
#     print(days_spent)

# # 망한 코드
# # 이러면 2 1 5 넣을 때 5 나옴
# # 못 생각한 조건: 일단 올라가면!!! 안 미끄러짐
# # 낮이랑 밤을 나눠서 생각해야 하지 않을까?

# # days_spent = 1

# # while True:
# #     height = (a - b) * days_spent
    
# #     if height >= v :
# #         break

# #     days_spent += 1

# # print(days_spent)


print("time :", time.time() - start)