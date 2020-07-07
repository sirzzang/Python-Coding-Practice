# 정답 : 31564 KB 276 ms

# 접근 6
# 경우를 3가지로 나눈다.
# - 1) input 받은 숫자가 stack의 top보다 클 때 : input 받은 숫자까지 stack에 append.
# - 2) input 받은 숫자가 stack의 top과 같을 때 : pop
# = 3) input 받은 숫자가 stack의 top보다 크거나 같지 않을 때(== 작을 때라는 의미이므로) : 불가능한 경우.
# 3)의 경우는 왜? 어차피 오름차순으로 stack에 입력받을 거니까, 나중에 pop하려면 stack의 가장 마지막 수와 같아야 pop할 수 있다.
# 1)의 경우는 while문으로 구현하고, 2), 3)은 if문으로 구현한다.

# 이전까지 1), 2)의 push, pop 단계를 같이 하려고 해서 난리가 났던 것 같다.
# 윗부분에서 한 번에 처리했던 push, pop을 나눠버린다 : 어차피 top == check_num이라고 한다면 while문 진행하는 단계에서 그 부분까지 처리된다.
# 이렇게 되면, 고질적 문제점이었던 NO 일 때 나누는 것을 그냥 flag 사용해서 쉽게 break해버리면 된다.

import sys
n = int(sys.stdin.readline())
stack = [] # 구현할 stack
check_list = [] # 정답 저장
num_add = 1 # stack에 어디까지 넣었는지 기록
flag = True # 조기 종료 위한 기준

for _ in range(n):
    
    input_num = int(sys.stdin.readline())
    
    # append는 처음 단계(input을 처음 받는 단계)이거나, input 받은 숫자가 stack의 top보다 클 때에만 append.
    while num_add <= input_num:
        stack.append(num_add)
        num_add += 1
        check_list.append("+")
        top = stack[-1]
        
    # 입력받은 숫자가 stack의 top과 같다면 pop.
    if input_num == top:
        stack.pop()
        check_list.append("-")
        if len(stack) != 0: # stack의 크기가 1일 때, pop 진행 후 나타나는 index error 방지.
            top = stack[-1]
    
    else:
        flag = False
        break
        
if flag:
    for check in check_list:
        print(check.strip("'"))
else:
    print("NO")




# 접근 5
# 문제점 2 : 1부터 넣을 때 문제가 됨.
# 1을 어떻게 해결한다 해도, 2일 때 문제...

# n = int(input())
# stack = []
# check_list = [] # 정답 저장

# num_add = 1 # stack에 어디까지 넣었는지 저장하기 위한 용도
# top = 0 # stack의 top을 확인할 것
# flag = True # 조기 종료 위한 것

# for _ in range(n):
    
#     check_num = int(input())
    
#     if check_num > num_add:        
#         stack.extend(range(num_add+1, check_num+2)) # 4까지 넣고 /
#         for _ in range(check_num):
#             check_list.append("push")
#         stack.pop() # 4만 뺀다 -> 그러면 3이 남지 /
#         check_list.append("pop")
#         top = stack[-1] # 모든 과정 완료 시 top 세팅
#         num_add = check_num
#         print("num_add : {}".format(num_add))
#         print(stack)
    
#     else:
#         if check_num == top :
#             stack.pop()
#             check_list.append("pop")
#             if len(stack) != 0:
#                 top = stack[-1]
#             print(stack)
        
#         else:
#             flag = False
#             break
            
#     if flag:
#         continue
#     else:
#         print("NO")
#         break

# print(check_list)

# 문제점 1 : num_add가 6까지 넣었으니까 6부터 들어와야 되는데 그게 안 됨.

# n = int(input())
# stack = []
# check_list = [] # 정답 저장

# num_add = 1 # stack에 어디까지 넣었는지 저장하기 위한 용도
# top = 0 # stack의 top을 확인할 것
# flag = True # 조기 종료 위한 것


# for _ in range(n):

#     check_num = int(input())

#     if check_num > num_add:
#         stack.extend(range(num_add, check_num+1)) # 4까지 넣고 /
#         num_add = check_num # 현재 들어온 check_num까지 num_add 저장 /
#         for _ in range(check_num):
#             check_list.append("push")
#         stack.pop() # 4만 뺀다 -> 그러면 3이 남지 /
#         check_list.append("pop")
#         top = stack[-1] # 모든 과정 완료 시 top 세팅
#         print(stack)

#     else: # 그게 아니라면
#         if check_num == top :
#             stack.pop()
#             check_list.append("pop")
#             print(stack)
#         else:
#             flag = "NO"

#     if not flag:
#         break

# if not flag:
#     print(flag)
# else:
#     print(check_list)

# 접근 4 
# push와 pop을 한 번에 처리해 보자. 
# - 43687521 순서라고 할 때
# - 1번으로 들어오는 애까지 push하고 pop
# - 2번으로 들어오는 애가 기존의 stack에 있으면 pop
# - 3번으로 들어오는 애는 기존의 stack에 없으니까 거기까지 push하고 pop
# - 4번으로 들어오는 애도 거기까지 없으니까 push하고 pop
# push & pop이 set로 이루어지나 봐야 하고,
# 기존의 stack에 그 다음에 들어오는 애가 있나 봐야 한다.

# 문제점 : 역시나, NO를 실행해야 하는 경우 구분이 안 된다.


# n = int(input('숫자를 입력하세요 : '))

# stack = [0]

# num_add = 1

# check_list = []

# flag = False

# for k in range(n):
    
#     check_num = int(input())

#     if check_num in stack:
#         print("pop 필요")
        
#         if check_num != stack[-1]:
#             flag = True
#             break
        
#         else:                   
#             while stack[-1] >= check_num:
#                 print(stack)
#                 stack.pop()
#                 print(stack)
#                 check_list.append("pop")
    
#     if flag:
#         print("NO")
#         break


#     else:
#         print("push 필요")
#         while num_add <= check_num:
#             stack.append(num_add)
#             check_list.append("push")
#             num_add += 1
#         stack.pop()
#         check_list.append("pop")
        
# print(check_list)

# 접근 3
# 이전처럼 어렵게 할 게 아니라, 입력받고, 입력받는 숫자가 없으면 append하고, 있으면 pop하면 되지 않나?

# 문제점 : NO를 출력해야 할 경우에도 push 필요가 출력된다.

# n = int(input('숫자를 입력하세요 : '))

# stack = []

# num_add = 1
# num_del = 0

# check_list = []

# for k in range(n):
    
#     check_num = int(input())

#     if check_num in stack:
#         print("pop 필요")
#         while stack[-1] >= check_num:
#             stack.pop()
#             check_list.append("pop")
#         print(stack)
#         print(check_list)
    
#     else:
#         print("push 필요")
#         while num_add <= check_num:
#             stack.append(num_add)
#             check_list.append("push")
#             num_add += 1
#         print(stack)
#         print(check_list)        

#         stack.pop()
#         print(stack)
#         check_list.append("pop")
#         print(check_list)

# num_add = 1

# for i in range(len(check_list)):
#     if check_list[i] in stack:
#         while stack[-1] < check_list[i]:
#             stack.pop()
#             print(stack)
    
#     else:
#         while num_add > check_list[i]:
#             stack.append(num_add)
#             num_add += 1
#             print(f"num_add : {num_add}")
#             print(stack)
        

# 접근 2
# 변곡점을 찾아서 그 중 max까지 push해버리고, pop하는 것은?
# - 4 / 3 / 6 8 / 7 5 2 1 : push 필요한 수는 4, 8
# - 1 2 5 / 3 / 4
# -일단 변곡점을 찾아야 한다. 

# 실행하기 전 문제점 : 변곡점 찾는 방법이 뭔데?

# init_list = list(range(n, 0, -1))
# print(init_list)
# stack = []

# for idx in range(len(check_list)-1):
#     if check_list[i] > check_list[i+1]:
#         for _ in range(check_list[i]-1):
#             stack.append()

# 접근 1 : 오답
# 실행해보니까 문제점
# - 6, 8까지 push push할 게 아니라, 8까지 한 번에 다 push해버리면 된다!

# 실행하기 전 문제점 
# - 일단 구현은 됐다. : stack이 0이 남으면, 이게 구현이 되는 거다.
# - break해야 할 경우 : pop을 해야 하는 경우인데, 12534에서 처럼, pop해야 할 때()
# - flag를 통해 break해야 하는 경우 표현하고 싶었는데 안 된다.

# n = int(input())

# stack = [0]
# max_num = 0
# flag = False
# check_list = []

# for _ in range(n):

#     check_num = int(input())

#     if check_num not in stack:
            
#         if check_num > stack[-1] :
#             stack.extend(range(max_num+1, check_num+1))
#             for _ in range(check_num - max_num):
#                 check_list.append("push")
#             max_num = check_num
    
#     else:
#         while check_num <= stack[-1]: # stack에 가장 마지막 숫자가 이거보다 입력된 숫자보다 커질 때까지 pop
#             stack.pop()
#             check_list.append("pop")


# if len(stack) != 1:
#     print("NO")
# else:
#     print(check_list)

# 초기 접근 방법 의식의 흐름
# 1) 일단 처음 나오는 애까지는 push해야 함.
# - list에 range를 붙이고 싶으면, append가 아니라 extend 사용해야 함.
# 2) 나중에 print할 거 생각하면, 한 줄 한 줄 +, - 사용해야 하므로, for문 쓰는 게 낫지 않을까?
# 일단 수열 구현하고, print할 생각으로 바꿔보자.
# 3) 어떻게 pop한 뒤부터 다음까지만 append할 수 있을까?
