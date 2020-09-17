# 오키. 경우 나눴다.

# 결국, 그냥 문자열 하나 하나 보면서 중복된 애가 있는지 찾고,
# 중복된 애 없다면 그룹문자
# 중복된 애 있다면 인덱스 위치 찾아서, 연속되지 않는다면 그룹문자가 아니어야 함.

# 중복된 애 없다는 것은 = set의 개수나 list의 개수나 같다는 것

s = "happppppppppppyyyyyyyyyyy"
s_list = list(s)
s_set = set(s)

if len(s_list) == len(s_set):
    print("그룹문자")

else:
    print("no")

# 아닌 경우에
# 1. 일단 중복된 문자 찾기
# 2. 그거 list에 넣기

print(s_list)
print(s_set)
s_set_forcheck = list(s_set)

checkList = []
for i in range(len(s_set_forcheck)):
    if s_list.count(s_set_forcheck[i]) > 1 :
        checkList.append(s_set_forcheck[i])
        # print(s_set_forcheck[i])                # 중복된 문자 p로 나옴.
print(checkList)

indexNum_list = []
for x in checkList:
    indexNum_list.append([index for index, value in enumerate(s_list) if value == x]) 
print(indexNum_list)



if all(indexNum_list[i][-1] - indexNum_list[i][0] + 1 == len(indexNum_list[i]) for i in range(len(indexNum_list))):
    print("그룹문자")
else:
    print("no")

# print([True for i in range(len(indexNum_list)) if indexNum_list[i][-1] - indexNum_list[i][0] + 1 == len(indexNum_list[i])])
# 이러면 false 가 나와야 하는데 True가 나온다...;;

# for i in range(len(indexNum_list)):
#     if all(indexNum_list[i][-1] - indexNum_list[i][0] + 1 == len(indexNum_list[i])):
#         print("그룹문자")
    
    
    # indexNum_list[i][-1] - indexNum_list[i][0] + 1 == len(indexNum_list[i]):
    #     print("그룹문자")
    # else:
    #     pass


# 큰 의미에서 망한 시도

# 문자열 -> list로 만들고 -> 그걸 set으로 만들면 중복된 애들 제거되겠지
# set으로 만든 것 안에 있는 문자열을 원래 list에서 체크한다.
# index number 다 뽑는다
# index 연속되지 않으면?


# 망한 시도 1
# 이렇게 했더니 내가 뽑고 싶었던 index_num_list = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
# s = ['a', 'b', 'c', 'a', 'b', 'c', 'a']
# print(s)
# s_set = list(set(s))
# print(s_set)

# index_num_list = [index for index, value in enumerate(s) for s in s_set]
# print(index_num_list)

# 망한 시도 2
# test = [i for i in range(len(s)) if s[i] == x for x in s_set] -> 오류

# s = ['a', 'b', 'c', 'a', 'b', 'c', 'a']
# s_set = list(set(s))
# print(s_set)
# indexNum_list = [i for i in range(len(s)) if s[i] == s_set[0]]
# test = [i for i in range(len(s)) if s[i] == x for x in s_set]
# print(indexNum_list)
# print(test)

# 일단 문자열 분해해서 만들 때 sorted 해야 함.

# s = sorted(['y','e','a','r'])
# -> 엥 근데 sorted하면 당연히 똑같은 순서로 나오겠지?


# 망한 시도 3
# 애초에 sorted하면 당연히 01234 똑같은 순서로 나옴.
# 게다가, 문자열 길이가 1이면 애초에 +0 해야 했음.

# import sys

# user_input = sys.stdin.readlines()
# user_input_list = [x.strip('\n') for x in user_input] # 이거 가지고 작업해야 함.

# num = 0
# for i in range(1, len(user_input_list)):
#     s = sorted(user_input_list[i])  # a a b
#     s_set = sorted(list(set(s)))    # a b
#     print(s)
#     print(s_set)

#     # if len(s) == 1:
#     #     num += 1
    
#     # else:



#     index_list = []
#     for x in s_set:
#         for i in range(len(s)):
#             if s[i] == x:
#                 index_list.append(i)
#     print(index_list)

# for i in range(len(index_list)-1):
#     if index_list[i+1] - index_list[i] == 1:
#         num += 1
#     elif len(index_list) == 1:
#         num += 1

# print(num)



# 똑같은 애들끼리 잘라

