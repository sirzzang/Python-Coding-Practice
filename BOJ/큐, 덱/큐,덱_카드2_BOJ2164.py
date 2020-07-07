# 시간 초과

import sys

n = int(sys.stdin.readline().strip('\n'))
queue = []

# n장의 카드 큐에 push
for i in range(1, n+1):
    queue.append(i)

# queue의 길이가 1이 될 때까지 버리기(pop), 순서 바꾸기(pop and push) 반복.

while len(queue) != 1:
    # 버리기
    queue.pop(0)

    # 순서 바꾸기
    card_pop = queue.pop(0)
    queue.append(card_pop)

for card in queue:
    print(card)

# index 사용 구현

import sys
n = int(sys.stdin.readline())

queue = [i for i in range(1, n+1)] # 입력된 숫자까지 push

front_index = 0 # queue의 top
queue_len = len(queue)

while queue_len != 1: # queue의 길이가 1이 될 때까지 아래의 연산 반복
    front_index += 1 # 버리기 : top 위치 한 칸 밀리고, 카드 장수 줄어듦.
    queue_len -= 1

    queue.append(queue[front_index]) # 바꾸기 : top을 맨 뒤로 보내고, top 한 칸 밀림.
    front_index += 1

print(queue.pop())

# class로 구현

class Queue:
    def __init__(self):
        self.itemList = []
        self.itemList_len = 0
        self.front_index = 0

    def push(self, item):
        self.itemList.append(item)
        self.itemList_len += 1

    def size(self):
        return self.itemList_len
    
    def pop(self):
        self.front_index += 1
        self.itemList_len -= 1
    
    def change(self):
        self.itemList.append(self.itemList[self.front_index])
        self.front_index += 1
    
    def back(self):
        return self.itemList[-1]

import sys

n = int(sys.stdin.readline())

cards = Queue()

# 입력받은 숫자만큼 push

for i in range(1, n+1):
    cards.push(i)

# 반복

while cards.size() != 1:
    cards.pop()
    cards.change()

print(cards.back())

