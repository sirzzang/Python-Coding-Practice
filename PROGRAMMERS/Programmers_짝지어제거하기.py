# 2차 시도
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 9.48MB)
테스트 2 〉	통과 (6.98ms, 10.8MB)
테스트 3 〉	실패 (런타임 에러)
테스트 4 〉	실패 (런타임 에러)
테스트 5 〉	실패 (런타임 에러)
테스트 6 〉	실패 (런타임 에러)
테스트 7 〉	실패 (런타임 에러)
테스트 8 〉	실패 (런타임 에러)
테스트 9 〉	통과 (0.00ms, 9.51MB)
테스트 10 〉	통과 (0.09ms, 9.52MB)
테스트 11 〉	통과 (0.01ms, 9.65MB)
테스트 12 〉	통과 (0.01ms, 9.7MB)
테스트 13 〉	통과 (0.01ms, 9.54MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	통과 (64.58ms, 22.4MB)
테스트 3 〉	실패 (런타임 에러)
테스트 4 〉	실패 (런타임 에러)
테스트 5 〉	실패 (런타임 에러)
테스트 6 〉	실패 (런타임 에러)
테스트 7 〉	실패 (런타임 에러)
테스트 8 〉	실패 (런타임 에러)
'''


def solution(s):
    if len(s) == 0:
        return 1
    elif len(s) == 1:
        return 0
    
    duplicates = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm',
                 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']
    for d in duplicates:
        if d in s:
            s = s.replace(d, '')
            return solution(s)
    else:
        return 0


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

import re

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

'''
def change_duplicates(s):
    duplicates = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp',
                 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']
    for dup in duplicates:
        if dup in s:
            return s.replace(dup, '')
    return False
        
def solution(s):
    print(s)
    while s:
        s = change_duplicates(s)
        if not s:
            return 0
    if len(s) == 0:
        return 1
'''