n = int(input())

ant = [1] # 초기 개미수열
if n == 1:
    print(1)
else:
    n -= 1

    while n:
        stack, temp = [], []
        while ant:
            flag = ant.pop(0)
            try:
                if flag == stack[-1]:
                    temp[-1] += 1
                else:
                    temp.extend([flag, 1])
                    stack.append(flag)
            except:
                stack.append(flag)
                temp.extend([flag, 1])
        n -= 1
        ant = temp

    for a in ant:
        print(a, end="")