# SW expert Academy에 비해 괄호 종류 늘어남.

# sys.stdin.readline : 줄바꿈 기호 조심

# 구글링 통해 찾아보니, 1) readlines로 받지 말아야 할 것 같고, 2) '.'일 때 끝나야 할 것 같음.
# 왜냐 : 조건으로 "입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다."가 있기 때문.

# 그냥 마지막의 점 하나에 대해 처리하지 않게 하면 되지 않을까?
# 정답 :29664 KB 96 ms 


import sys

myStr_list = sys.stdin.readlines()

for idx in range(len(myStr_list)-1):

    myStr = myStr_list[idx].strip('\n')

    check_list = []

    for i in myStr:
        if i in "({[":
            check_list.append(i)
        
        elif i in "]})":
            if len(check_list) == 0:
                check_list.append(i)
                break
            else:
                if (i == ")" and check_list[-1] != "(") or (i == "}" and check_list[-1] != "{") or (i == "]" and check_list[-1] != "["):
                    break
                else:
                    check_list.pop()

    if len(check_list) == 0:
        print("yes")
    else:
        print("no")


# 오답 : 제출2
# 열고 닫는 것에 반례가 있을 수 있다고 생각해서 pop 하는 부분 바꿨는데 아니었음.

# import sys

# myStr_list = sys.stdin.readlines()

# for idx in range(len(myStr_list)):

#     myStr = myStr_list[idx].strip('\n')

#     check_list = []

#     for i in myStr:
#         if i in "({[":
#             check_list.append(i)
        
#         elif i in "]})":
#             if len(check_list) == 0:
#                 check_list.append(i)
#                 break
#             else:
#                 if i == ")" and check_list[-1] == "(":
#                     check_list.pop()
#                 elif i == "}" and check_list[-1] == "{":
#                     check_list.pop()
#                 elif i == "]" and check_list[-1] == "[":
#                     check_list.pop()
#                 else:
#                     break

#     if len(check_list) == 0:
#         print("yes")
#     else:
#         print("no")




# 오답 처리
# # 반례가 무엇일까?

# import sys

# myStr_list = sys.stdin.readlines()

# for idx in range(len(myStr_list)):

#     myStr = myStr_list[idx].strip('\n')

#     check_list = []

#     for i in myStr:
#         if i in "({[":
#             check_list.append(i)
        
#         elif i in "]})":
#             if len(check_list) == 0:
#                 check_list.append(i)
#                 break
#             else:
#                 if (i == ")" and check_list[-1] != "(") or (i == "}" and check_list[-1] != "{") or (i == "]" and check_list[-1] != "["):
#                     break
#                 else:
#                     check_list.pop()

#     if len(check_list) == 0:
#         print("yes")
#     else:
#         print("no")