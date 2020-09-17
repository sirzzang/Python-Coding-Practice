# 그림에 낚이지 말 것
# 1 - 2- 3- 4 순서대로 다시 배열해보기

# user_input : 말 그대로 몇 번째인지
# num : 그 이전까지 몇 개였는지
# room : 몇 번째 칸인지
# 규칙 : 분자 + 분모 = room + 1
# 분모를 나눠야 함 경우를
# room이 짝수일 때는 분자 = 입력값 - 이전의 num
# room이 홀수일 때는 분모 = 입력값 - 이전의 num


user_input = int(input())

num = 1
room = 1

if user_input == 1:
    print("1/1")
else:
    while True:
        
        room += 1

        if room % 2 == 0:
            numerator = user_input - num
            denominator = (room + 1) - numerator
            num += room

        else:
            denominator = user_input - num
            numerator = (room + 1) - denominator
            num += room

        if user_input <= num:
            break

    print('{var1}/{var2}'.format(var1 = numerator, var2 = denominator))


# 망한 코드 2
# 미친 다 괜찮은데'''''' ㅅㅂ 지그재그;;;;;;;;;;; ㅅㅂ
# 문제 좀 제대로...

# user_input = int(input())

# num = 1
# room = 1

# if user_input == 1:
#     print("1/1")
# else:
#     while True:
        
#         room += 1
#         denominator = user_input - num
#         numerator = (room + 1) - denominator
#         num += room

#         if user_input <= num:
#             break

#     print('{var1}/{var2}'.format(var1 = numerator, var2 = denominator))


# # while True:
    
# #     denominator = 
    
# #     if user_input <= num:
# #         break
    
# #     room += 1
# #     num += room

# # print(numerator, denominator)


# # 망한 코드 1
# # 4까지는 잘 나오는데, 5부터 2/2가 안 나오고 3/1이 나옴
# # 분자 : 몇 번째 칸인지와 일치 -> room -> 이렇게 짜서 그런듯

# # user_input = int(input())

# # num = 1
# # room = 1

# # while True:
    
# #     numerator = room
# #     denominator = (room + 1) - numerator
    
# #     if user_input <= num:
# #         break
    
# #     room += 1
# #     num += room

# # print(numerator, denominator)
