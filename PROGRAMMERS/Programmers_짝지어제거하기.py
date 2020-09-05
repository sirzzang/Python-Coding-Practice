import re


# 1차 시도
'''
정확성  테스트
테스트 1 〉	실패 (0.15ms, 10MB)
테스트 2 〉	통과 (0.76ms, 10.5MB)
테스트 3 〉	통과 (0.32ms, 10.4MB)
테스트 4 〉	통과 (0.35ms, 10.4MB)
테스트 5 〉	통과 (0.32ms, 10.5MB)
테스트 6 〉	실패 (1.05ms, 10.5MB)
테스트 7 〉	실패 (0.32ms, 10.5MB)
테스트 8 〉	실패 (0.34ms, 10.4MB)
테스트 9 〉	통과 (0.14ms, 10MB)
테스트 10 〉	통과 (0.16ms, 10.2MB)
테스트 11 〉	실패 (0.16ms, 10.1MB)
테스트 12 〉	실패 (0.15ms, 10.1MB)
테스트 13 〉	실패 (0.16ms, 10.2MB)
효율성  테스트
테스트 1 〉	실패 (65.71ms, 13.8MB)
테스트 2 〉	통과 (1.79ms, 13.8MB)
테스트 3 〉	통과 (1.85ms, 13.9MB)
테스트 4 〉	통과 (1.79ms, 13.9MB)
테스트 5 〉	통과 (1.88ms, 13.8MB)
테스트 6 〉	실패 (1.74ms, 13.8MB)
테스트 7 〉	실패 (1.72ms, 13.9MB)
테스트 8 〉	실패 (1.73ms, 13.8MB)
'''

def is_duplicate(s, pattern):
    if re.search(pattern, s) is None:
        return False
    return re.sub(pattern, '', s, count=1) 

def solution(s):
    pattern = r'((\w)\2)'
    flag = is_duplicate(s, pattern)
    if not flag:
        return 0
    s = flag
    is_duplicate(s, pattern)
    return 1

 