'''
출처: https://programmers.co.kr/learn/courses/30/lessons/68644
'''

def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        self_number = numbers[i]
        for other_number in numbers[:i] + numbers[i+1:]:
            answer.add(self_number+other_number)
    answer = list(answer)
    answer.sort()
    return answer