import sys

user_input = sys.stdin.readlines()
user_input_list = [x.strip('\n') for x in user_input]

group_character_count = 0

for i in range(1, len(user_input_list)):
    myStr = user_input_list[i]    
    myStr_list = list(myStr)    
    myStr_set = set(myStr)    

    if len(myStr_list) == len(myStr_set):
        group_character_count += 1

    else:
        myStr_set_forcheck = list(myStr_set)

        check_list = []
        for i in range(len(myStr_set_forcheck)):
            if myStr_list.count(myStr_set_forcheck[i]) > 1 :
                check_list.append(myStr_set_forcheck[i])
        
        index_list = []
        for x in check_list:
            index_list.append([index for index, value in enumerate(myStr_list) if value == x])
        
        if all(index_list[i][-1] - index_list[i][0] + 1 == len(index_list[i]) for i in range(len(index_list))):
            group_character_count += 1
        else:
            pass

print(group_character_count)

# 그룹문자 제대로 프린트되는지 확인
# 예시파일에 제대로 프린트 오케이.


# import sys

# user_input = sys.stdin.readlines()
# user_input_list = [x.strip('\n') for x in user_input] 

# for i in range(1, len(user_input_list)):
#     myStr = user_input_list[i]
#     print(myStr)
#     myStr_list = list(myStr)
#     print(myStr_list)
#     myStr_set = set(myStr)
#     print(myStr_set)

#     if len(myStr_list) == len(myStr_set):
#         print("그룹문자")

#     else:
#         myStr_set_forcheck = list(myStr_set)

#         check_list = []
#         for i in range(len(myStr_set_forcheck)):
#             if myStr_list.count(myStr_set_forcheck[i]) > 1 :
#                 check_list.append(myStr_set_forcheck[i])
#         print(check_list)

#         index_list = []
#         for x in check_list:
#             index_list.append([index for index, value in enumerate(myStr_list) if value == x])
#         print(index_list)

#         if all(index_list[i][-1] - index_list[i][0] + 1 == len(index_list[i]) for i in range(len(index_list))):
#             print("그룹문자")
#         else:
#             print("no")  
