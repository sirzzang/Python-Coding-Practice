'''
# 짝수 개의 연속된 자연수이려면
    - 2: 2로 나누었을 때 1로
    - 4: 4로 나누었을 때 2로
# 홀수 개의 연속된 자연수로 표현할 수 있으려면: 해당 홀수의 배수여야 함.
# 1개로는 모두 다 표현할 수 있으므로 +1
'''

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
테스트 13 〉	통과 (0.02ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (0.05ms, 10.2MB)
테스트 5 〉	통과 (0.04ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
'''

def is_divide_even(n, d):
    if n%d == (d//2):
        return True
    return False

def is_divide_odd(n, d):
    if n%d == 0:
        return True
    return False

def solution(num):
    answer = 0
    # 마지막에 어디까지 나누어 보아야 하는가
    for i in range(2, num):
        if i*(i+1) > 2*num:
            break
        if i%2 == 0:
            answer += is_divide_even(num, i)
            # print(i, is_divide_even(num, i))
        else:
            answer += is_divide_odd(num, i)
            # print(i, is_divide_odd(num, i))
    return answer+1

if __name__ == '__main__':
    print(solution(15))
    print()
    print(solution(31))