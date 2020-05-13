# class로 문제 풀 때는 항상,
# 변수 생성해서 class 할당하고, 그 class에 대해 문제를 풀어야 한다.

# 3. 접근법 3
# 인터넷 보고, class 사용했다.
# 1) input_method에서 출력이 필요하지 않은 명령 + 넣어야 되는 명령 확인 : push -> self + 넣어야 되는 item에 대한 인자 필요
# 2) input_method에서 출력이 필요한 명령 + 넣지 않아도 되는 명령 확인 : pop, size, empty, top. -> 인자 self만 필요

# 인터넷에서 찾아본 기본 class 구현
# class Stack:
    
#     def __init__(self):
#         self.lst = []
    
#     def push(self, item):
#         self.lst.append(item)
    
#     def pop(self):
#         self.lst.pop()
    
#     def empty(self): # 있으면 False, 없으면 True 출력됨.
#         return not self.items


# 정답 : 29616 KB 68 ms 

class Stack:
    
    def __init__(self):
        self.itemList = []

    def push(self, item):
        self.itemList.append(item)
    
    def pop(self):        
        if len(self.itemList) == 0: # self.itemList.len 해도 되나?
            return -1
        else:
            return self.itemList.pop()
    
    def size(self):
        return len(self.itemList)
    
    def empty(self):
        if len(self.itemList) == 0:
            return 1
        else:
            return 0
    
    def top(self):
        if len(self.itemList) == 0:
            return -1
        else:
            return self.itemList[-1]

import sys

n = int(sys.stdin.readline())

myStack = Stack()

for _ in range(n):

    input_method = sys.stdin.readline().split()

    if input_method[0] == "push":
        myStack.push(int(input_method[1]))
    
    if input_method[0] == "pop":
        print(myStack.pop())

    if input_method[0] == "size":
        print(myStack.size())
    
    if input_method[0] == "empty":
        print(myStack.empty())
    
    if input_method[0] == "top":
        print(myStack.top())

# 오류 1
# push() missing 1 required positional argument: 'item'
# class를 선언하지 않았기 때문에 나타나는 문제였다!!!

# import sys

# n = int(sys.stdin.readline())

# for _ in range(n):

#     input_method = sys.stdin.readline().split()

#     if input_method[0] == "push":
#         Stack.push(int(input_method[1]))
    
#     if input_method[0] == "pop":
#         print(Stack.pop())

#     if input_method[0] == "size":
#         print(Stack.size())
    
#     if input_method[0] == "empty":
#         print(Stack.empty())
    
#     if input_method[0] == "top":
#         print(Stack.top())

# 2. 접근법 2 
# 그냥 기본적으로, if ~ else 문 사용한다.

# 1) input_method까지만 잘 출력되는지 확인
# input().split[0]만 하면, 앞에 있는 명령이 무엇인지 확인 가능.
# 2) input_method에서 출력이 필요한 명령 확인 : pop, size, empty, top.
# 3) input_method에서 출력이 필요 없는 경우 stack에 넣는 과정 확인

# 정답 : sys.stdin.readline() 사용했더니 시간초과 해결, 29616 KB 68 ms 

import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):

    input_method = sys.stdin.readline().split()

    if input_method[0] == "push":
        stack.append(int(input_method[1]))
    
    if input_method[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    if input_method[0] == "size":
        print(len(stack))
    
    if input_method[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    if input_method[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])


# 오답 : 시간 초과

# n = int(input())
# stack = []

# for _ in range(n):

#     input_method = input().split()

#     if input_method[0] == "push":
#         stack.append(int(input_method[1]))
    
#     if input_method[0] == "pop":
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack.pop())

#     if input_method[0] == "size":
#         print(len(stack))
    
#     if input_method[0] == "empty":
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)
    
#     if input_method[0] == "top":
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[-1])


# 1. 접근법 1
# 함수 정의한 후, 실행하려고 했는데
# 문제는 입력이 주어지는 형식이 이걸 구현할 수 있는 게 아닌 것 같아 보였다.

# stack = []

# def push(x):
#     return stack.append(x)

# def pop():
#     if len(stack) == 0:
#         return -1
#     else:
#         stack.pop(-1)

# def size():
#     return len(stack)

# def 