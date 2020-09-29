'''
출처: https://programmers.co.kr/learn/courses/30/lessons/12939
'''

def solution(s):
    numbers = [int(n) for n in s.split()]
    answer = '{} {}'.format(min(numbers), max(numbers))
    return answer