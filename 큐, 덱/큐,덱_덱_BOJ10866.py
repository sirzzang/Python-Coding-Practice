# 시간초과 날 것 없이 괜찮게 풀렸네?

import sys

n = int(sys.stdin.readline())
deque = []

for _ in range(n):

    input_method = sys.stdin.readline()

    if "push_front" in input_method:
        deque.insert(0, int(input_method.split()[1]))
    elif "push_back" in input_method:
        deque.append(int(input_method.split()[1]))
    elif "pop_front" in input_method:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0))
    elif "pop_back" in input_method:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif "size" in input_method:
        print(len(deque))
    elif "empty" in input_method:
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif "front" in input_method:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    else:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])

    
