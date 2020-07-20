# 올바른 괄호 문자열인지 검사
def check_bracket(p):
    flag = True
    p = list(p) # 리스트로 만들기
    stack = []
    while p: # 괄호 문자열이 남아 있을 때
        # print(f"현재 괄호 문자열: {p}")
        if p[-1] == ')': # 오른쪽 괄호일 때
            stack.append(p.pop())
            # print(f"  ===== 현재 stack: {stack}")
        else: # 왼쪽 괄호일 때
            if len(stack) == 0 or stack[-1] == '(':
                # print("짝이 맞지 않습니다.")
                flag = False
                break
            elif stack[-1] == ')': # 짝이 맞는 것
                p.pop() # 왼쪽 괄호 제거
                stack.pop() # stack에서 오른쪽 괄호 제거
                # print(f"  ===== 현재 stack: {stack}")
    # 전부 다 검사한 후
    if len(stack) != 0:
        flag = False
    return flag

def split_bracket(p):
    i = 0 # 인덱스
    left = 0
    right = 0
    u = ''
    v = ''
    while i < len(p):
        if p[i] == '(':
            left += 1
        elif p[i] == ')':
            right += 1
        i += 1
        if i > 0 and left == right:
            u = p[:i]
            v = p[i:]
            break
    return u, v

def correct_bracket(p):
    # TypeError: 'str' object does not support item assignment
    # AttributeError: 'str' object has no attribute 'pop'
    p = list(p) # 리스트로 만들어 주기
    p.pop(0) # 앞 문자 제거
    p.pop() # 뒷 문자 제거
    # print(p)
    for i in range(len(p)):
        if p[i] == '(':
            p[i] = ')'
        elif p[i] == ')':
            p[i] = '('
    # print(p)
    return "".join(p) # 문자열로 반환

def solution(p):
    answer = ''
    if p == '':
        return ''

    u, v = split_bracket(p)

    if check_bracket(u):
        v = solution(v) # v에 대해 재귀적으로 수행
        answer = u + v
        # return answer
    else: # 올바른 문자열이 아니라면
        v = solution(v) # v에 대해 재귀적으로 수행
        answer = "(" + v + ")" + correct_bracket(u)
        # return answer
    return answer


# ============= 테스트 =====================

# print(check_bracket(input()))
# u, v = split_bracket(input())
# print(f"u: {u}, v: {v}")
# print(correct_bracket(input()))
print(solution(input()))
