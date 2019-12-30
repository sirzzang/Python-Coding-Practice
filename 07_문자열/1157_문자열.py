# 공백 주의...
# 줄바꿈 개행문자 주의

import sys
s = sys.stdin

user_input = s.readline()
myStr = user_input.upper()

myStr_list = list(set(myStr)-set("\n"))

num_list = [myStr.count(myStr_list[i]) for i in range(len(myStr_list))]

index_list = [index for index, value in enumerate(num_list) if value == max(num_list)]

if len(index_list) == 1:
    print(myStr_list[index_list[0]])
else:
    print("?")


# 런타임 에러

# myStr = input().upper()

# myStr_list = [myStr[i] for i in range(len(myStr))]
# myStr_set = set(myStr_list)
# check_list = list(myStr_set)


# num_list = [myStr_list.count(check_list[i]) for i in range(len(check_list))]
# check_num = max(num_list)


# index_list = [index for index, value in enumerate(num_list) if value == check_num]

# if len(index_list) == 1 :
#     print(check_list(index_list[0]))
# else:
#     print("?")


# # 공백있을 때??