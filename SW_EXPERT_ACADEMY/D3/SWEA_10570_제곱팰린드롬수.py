def is_palindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    return False

def solution(a, b):
    if a**(1/2) == int(a**(1/2)):
        start = int(a**(1/2))
    else:
        start = int(a**(1/2)) +1
    end = int(b**(1/2))+1

    answer = 0
    for n in range(start, end):
        if is_palindrome(n) and is_palindrome(n**2):
            answer += 1
    return answer

TC = int(input())
for tc in range(TC):
    a, b = map(int, input().split())
    answer = solution(a, b)
    print("#{0} {1}".format(tc+1, answer))
