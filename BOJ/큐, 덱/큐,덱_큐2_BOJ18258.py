# 시간초과
# FAQ : python에서 pop(0)은 절대 하면 안 된다.
# 링크 : https://wayhome25.github.io/python/2017/06/14/time-complexity/
# 특정 위치에 있는 원소를 뺴는 pop은 O(n)의 시간복잡도를 가지고 있다.
# 시간초과 문제를 해결하려면 O(1)의 시간복잡도를 갖도록 해야 한다.
# list에서 O(1)의 시간 복잡도를 갖는 연산 
# : index, store, length, append, pop()(마지막 위치)

import sys

n = int(sys.stdin.readline())
queue = []

for _ in range(n):
    input_method = input().split()

    if input_method[0] == "push":
        queue.append(int(input_method[1]))
    
    elif input_method[0] == "pop":
        if len(queue) != 0:
            print(queue.pop(0))
        else:
            print(-1)
    
    elif input_method[0] == "size":
        print(len(queue))
    
    elif input_method[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif input_method[0] == "front":
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)

    else:
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)


# 오답 : 틀렸습니다...

# Q1) pop 계속 해서 front index는 계속 커지고, queue_length는 계속 작아지면 어떡하지?
# 어차피 queue_length가 0, 즉 queue가 비게 되면 front index 커질 일 없고, queue_length는 작아질 일 없다.
# Q2) front 연산 수행하는 과정에서, queue의 길이가 front_index보다 작으면 어떡하지?
# push, pop만 넣고 꺼내고가 가능한 연산인데, 
# pop에서 if절 조건에 0이 되는 순간 front_index 초기화시켜야 할 듯.

n = int(sys.stdin.readline())
queue = []
queue_length = 0 # push할 때마다 length 증가.
front_index = 0 # pop 연산 이루어질 때마다 처음 index를 나타낼 것.

for _ in range(n):
    input_method = sys.stdin.readline().split()

    if input_method[0] == "push":
        queue.append(int(input_method[1]))
        queue_length += 1
    
    elif input_method[0] == "pop":
        if queue_length == 0:
            print(-1)
            front_index = 0 # pop 연산에서 길이가 0이 되어 버리는 순간, 즉, queue가 비는 순간 front_index 초기화
        else:
            print(queue[front_index])
            front_index += 1
            queue_length -= 1

    elif input_method[0] == "size":
        print(queue_length)
    
    elif input_method[0] == "empty":
        if queue_length == 0:
            print(1)
        else:
            print(0)
    
    elif input_method[0] == "front":
        if queue_length == 0:
            print(-1)
        else:
            print(queue[front_index])


    else:
        if queue_length == 0:
            print(-1)
        else:
            print(queue[queue_length + front_index - 1]) # front index + queue_length를 하면, index 1 초과.


# 만약에 pop을 계속해서 size가 0보다 작아지면 어떡하나?


# 오답 : 틀렸습니다!

# pop 연산을 어떻게 index만 가지고 구현할 수 있을까?
# 뽑아 오는 건 문제되지 않는데,
# 앞의 요소를 삭제해야 하기 때문에 어렵다.

# 앞의 요소를 삭제하지 말고, index만 이용해서 구현해 보자.
# 어차피 pop에서는 그냥 맨 앞의 애만 보여주면 되고,
# real_index를 사용하자.

n = int(sys.stdin.readline())
queue = []
queue_length = 0 # push할 때마다 length 증가.
front_index = 0 # pop 연산 이루어질 때마다 처음 index를 나타낼 것.

for _ in range(n):
    input_method = input().split()

    if input_method[0] == "push":
        queue.append(int(input_method[1]))
        queue_length += 1
    
    elif input_method[0] == "pop":
        if front_index < queue_length:
            print(queue[front_index])
            front_index += 1
            
        else: # front_index가 queue_length보다 크거나 같으면 index error가 난다.
            print(-1)
    
    elif input_method[0] == "size":
        if queue_length < front_index : # length가 음수가 되면 그냥 0 출력해 버리자.
            print(0)
        else:
            print(queue_length - front_index)
    
    elif input_method[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif input_method[0] == "front":
        if len(queue) != 0:
            print(queue[front_index])
        else:
            print(-1)

    else:
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)


