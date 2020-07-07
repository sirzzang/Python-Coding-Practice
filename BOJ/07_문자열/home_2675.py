import sys
s = sys.stdin

user_input = s.readlines()

test_case = [user_input[i].strip('\n') for i in range(1, len(user_input))]
repeat_num = [int(case[0]) for case in test_case]
repeat_str = [case[2:] for case in test_case]

for i in range(len(test_case)):
    print(''.join([char*repeat_num[i] for char in repeat_str[i]]))



# for i in range(1, len(user_input)):
#     test_case = user_input[i].strip('\n')
#     repeat_num = int(test_case[0])
#     repeat_str = test_case[2:]
#     for j in range(len(repeat_str)):
#         repeat_str[j]
#         print(repeat_str[j], end = ' ')
    