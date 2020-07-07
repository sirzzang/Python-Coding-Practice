# class 사용해서 구현
# 시간 : 112ms

class Stack:
    def __init__(self):
        self.itemList = []
    
    def push(self, item):
        self.itemList.append(item)
    
    def pop(self):
        return self.itemList.pop()
    
    def size(self):
        return len(self.itemList)

import sys

user_input = sys.stdin.readline().strip('\n')

sticks = Stack()
pieces = 0

for i in range(len(user_input)):
    if user_input[i] == "(":
        sticks.push(user_input[i])
    else:
        if user_input[i-1] == "(":
            sticks.pop()
            pieces += sticks.size()
        else:
            sticks.pop()
            pieces += 1

print(pieces)
       
# 정답 : stack 사용하지 않음.
# 시간 : 80ms

import sys

sticks = sys.stdin.readline().strip('\n')

pieces = 0
left = 0

for i in range(len(sticks)):
    if sticks[i] == "(":
        left += 1
    else:
        if sticks[i-1] == "(": # 레이저("()")인 경우
            left -= 1 # 레이저 짝 제거
            pieces += left
        else: # 쇠막대의 끝인 경우
            left -= 1 # 쇠막대 짝 제거
            pieces += 1

print(pieces)
