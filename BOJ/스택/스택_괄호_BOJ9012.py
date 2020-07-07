# SW expert Academy 코드 활용
# SW expert Academy 문제에 비해 중괄호가 없어서 쉬웠다.

import sys

n = int(sys.stdin.readline())

for _ in range(n):

    PS = sys.stdin.readline()
    stack = []

    for i in PS:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                stack.append(i)
                break
            else:
                stack.pop()
    
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")