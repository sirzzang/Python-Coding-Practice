# stack을 활용해서 풀어보려고 했다.
# stack에 push할 때 최댓값이 뒤로 가게만 넣으면 될 것이라 생각했다.

# 이후 stack을 활용하는 방법을 포기하고, 큐를 구현할 때 pop했던 원리를 생각해서 index를 사용하려 했다.
# 2시간 동안 고민한 결과 풀리지 않았다.


# 첫 번째 제출
# 넣을 위치를 idx로 찾고 insert하는 부분에서 시간이 오래 걸린다.
# 심지어 for문과 while문이 함께 작동한다.

import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    com = int(sys.stdin.readline())

    if com == 0:
        if len(stack) == 0:
            print(0)
        else:
            print(stack.pop())

    else: # 큰 수가 뒤로 가게 넣는다.
        if len(stack) == 0:
            stack.append(com)
        else:
            if com >= stack[-1]:
                stack.append(com)
            else:
                idx = 0
                while com > stack[idx]:
                    idx += 1
                stack.insert(idx, com)


# 두 번째 제출
# insert가 시간이 걸린다고 생각해 slicing을 이용해 list를 합치는 방법을 썼다.
# 그런데 결국 insert의 idx 위치까지 찾으나, slicing을 이용해 그 idx까지 자르나 시간복잡도는 비슷할 것 같다.
# 중간값 idx가 N이라 할 때, insert의 시간복잡도는 O(N), slice의 시간복잡도도 O(N-0)이니까.
# 거기다 for문과 while문이 함께 있다.


import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    com = int(sys.stdin.readline())

    if com == 0: # 비어 있으면 0, 아니면 마지막 위치 pop.
        if len(stack) == 0:
            print(0)
        else:
            print(stack.pop())

    else:
        if len(stack) == 0: # 비어 있으면 append
            stack.append(com)

        elif com >= stack[-1]: # 안 비어 있고, 넣을 수가 최댓값보다 크다면 append
            stack.append(com)

        else:
            idx = 0
            while com > stack[idx]: # 넣을 수가 stack에 있는 수보다 작아질 때까지 순회
                idx += 1
            left = stack[:idx] # 넣을 수보다 작은 원소들
            right = stack[idx:] # 넣을 수보다 큰 원소들
            left.append(com) # left에 수 넣고
            stack = left + right # 둘이 합쳐서 stack 초기화