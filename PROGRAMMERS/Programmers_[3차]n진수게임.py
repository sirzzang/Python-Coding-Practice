# 첫 번째 풀이
'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.05ms, 10.3MB)
테스트 5 〉	통과 (0.83ms, 10.2MB)
테스트 6 〉	통과 (0.80ms, 10.3MB)
테스트 7 〉	통과 (0.76ms, 10.3MB)
테스트 8 〉	통과 (0.40ms, 10.3MB)
테스트 9 〉	통과 (0.40ms, 10.3MB)
테스트 10 〉	통과 (0.46ms, 10.3MB)
테스트 11 〉	통과 (0.42ms, 10.1MB)
테스트 12 〉	통과 (0.38ms, 10.2MB)
테스트 13 〉	통과 (0.24ms, 10.2MB)
테스트 14 〉	통과 (77.39ms, 10.6MB)
테스트 15 〉	통과 (77.13ms, 10.5MB)
테스트 16 〉	통과 (77.37ms, 10.5MB)
테스트 17 〉	통과 (4.83ms, 10.3MB)
테스트 18 〉	통과 (3.54ms, 10.2MB)
테스트 19 〉	통과 (1.33ms, 10.4MB)
테스트 20 〉	통과 (3.10ms, 10.2MB)
테스트 21 〉	통과 (18.50ms, 10.3MB)
테스트 22 〉	통과 (10.14ms, 10.2MB)
테스트 23 〉	통과 (25.72ms, 10.2MB)
테스트 24 〉	통과 (72.53ms, 10.5MB)
테스트 25 〉	통과 (88.27ms, 10.7MB)
테스트 26 〉	통과 (9.89ms, 10.3MB)
'''

# n진수로 교체
def change_base(n, base):
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    num_str = ''
    while n:
        num_str += num_list[n%base]
        n //= base
    return num_str[::-1]

# 더 생각해야 할 것
'''
1) N진수 몇 개까지 구해야 하는지
2) 굳이 구해놓지 않고 length만 체크해서 자기 차례 되면 바로 return하도록
'''

def solution(n, t, m, p):
    answer = ''

    flag = '0'
    temp = 1
    while temp < t*m: # 시간 비효율 여지 있음.
        flag += change_base(temp, n)
        temp += 1

    idx = p-1
    for _ in range(t):
        answer += flag[idx]
        idx += m

    return answer

# 테스트
if __name__ == '__main__':
    print(solution(2, 4, 2, 1))
    print(solution(16, 16, 2, 1))
    print(solution(16, 16, 2, 2))