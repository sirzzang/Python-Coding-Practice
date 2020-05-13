# 설정할 조건 : INPUT STRING에서 빼와서 STACK에 넣을 애가, STACK의 TOP과 똑같으면 지운다
# 끝날 조건 : INPUT STRING이 남아 있을 때까지

# CAAABBA
# [C,A,A,A,B,B,A] - []
# [A,A,A,B,B,A] - [C]
# [A,A,B,B,A] - [C,A]
# IF 조건 만족
# [A,B,B,A] - [C]
# [B,B,A] - [C,A]
# [B,A] - [C,A,B]
# IF 조건 만족
# [A] - [C,A]
# IF 조건 만족
# [] - [C]
# 종료
# RETURN : stack의 길이

# 생각해줘야 하는 제약
# 초기/중간에 stack이 비어 있다면(len(stack) == 1): stack에 그냥 넣으면 됨.

# 구현 1
# FOR문 사용

# 접근 1 : 정답

T = int(input())

for t in range(T):

    myStr = list(input()) # 애초에 list로 한 글자씩 받기.
    stack = [0] # 처음에 stack[-1]로 조건 지정하므로, 초기화 필요.

    for s in myStr:
        if s != stack[-1]:
            stack.append(s)
        else:
            stack.pop()

    print("#{} {}".format(t+1, len(stack) -1)) # 처음에 지정한 0 빼기.

# 접근 2 : 정답
# 아예 처음부터 stack 초기화시켜 놓고 간다면?

T = int(input())

for t in range(T):

    myStr = list(input())
    stack = []

    for s in myStr:
        if s not in stack:
            stack.append(s)
        else:
            if s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)

    print("#{} {}".format(t+1, len(stack))) 

# 구현 2
# 함수 사용 : 실패 = 나중에 다시 해보기

def erase(myStr):

    stack = [0]

    for s in myStr:
        
        if s != myStr[-1]:
            stack.append(s)
        else:
            stack.pop()

    return len(stack)-1

n = int(input())
for _ in range(n):
    myStr = input()
    print(erase(myStr))



    

        