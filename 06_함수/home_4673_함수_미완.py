# import sys
# s = sys.stdin

# num_raw = s.readline()
# print(type(num_raw))


# num_raw = input()

# sum_digit = 0
# for i in range(len(num_raw)):
#     sum_digit += int(num_raw[i])
# num_sum = int(num_raw) + sum_digit
# print(num_sum)

# if num_sum == 10000:
#     print("생성자")
# else:
#     print("no")


# numList = list(range(1, 11))
# print(numList) # 1 ~ 10000까지 숫자 들어 있는 list

# for num in numList: # num : 1 ~ 10000까지 숫자
#     while True:
#         sum_digit = 0
#         for i in range(len(str(num))):
#             sum_digit += int(str(num)[i])
#             num_sum = num + sum_digit
#         if num_sum > 100:
#             break
#         else:
#             num = num_sum
#     print(num)
     
def recursive_self(num):
    sum_digit = 0
    for i in range(len(str(num))):
        sum_digit += int(str(num)[i])
        num_sum = num + sum_digit
    if num_sum >= 200:
        return
    print(num)
    num = num_sum
    recursive_self(num)

recursive_self(15)
# 15 21 24 30 33 39 51.. : 15는 51의 생성자.
# 뭔가 맞는데, 이게 생성자를 어떻게..?