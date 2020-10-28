'''
문제 출처: https://programmers.co.kr/learn/courses/30/lessons/68645?language=python3
'''

# # 1차 시도
# '''
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	실패 (런타임 에러)
# 테스트 5 〉	실패 (런타임 에러)
# 테스트 6 〉	실패 (런타임 에러)
# 테스트 7 〉	실패 (런타임 에러)
# 테스트 8 〉	실패 (런타임 에러)
# 테스트 9 〉	실패 (런타임 에러)
# '''
#
# # def solution(n):
# #     answer = [[0]*i for i in range(1, n+1)]
# #     num = 0
# #     for i in range(n):
# #         if i%3 == 0:
# #             for j in range(i//3, n):
# #                 if answer[j][i//3] != 0:
# #                     continue
# #                 num += 1
# #                 answer[j][i//3] = num
# #         elif i%3 == 1:
# #             for j in range(n-i//3-1):
# #                 if answer[n-i//3-1][j+1] != 0:
# #                     continue
# #                 num += 1
# #                 answer[n-i//3-1][j+1] = num
# #         else:
# #             for j in range(n-1):
# #                 if answer[n-j-1][n-i//3-j-1] != 0: # 여기서 인덱스 -1, -2 나와 버리는 경우 발생.
# #                     continue
# #                 num += 1
# #                 answer[n-j-1][n-i//3-j-1] = num
# #
# #     return [t for temp in answer for t in temp]

# 2차 시도: 효율성 개선 필요.
'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (2.26ms, 10.9MB)
테스트 5 〉	통과 (2.17ms, 10.8MB)
테스트 6 〉	통과 (2.24ms, 10.8MB)
테스트 7 〉	통과 (252.17ms, 58.3MB)
테스트 8 〉	통과 (258.39ms, 59.9MB)
테스트 9 〉	통과 (256.33ms, 60.2MB)
'''

def solution(n):
    answer = [[0]*i for i in range(1, n+1)]
    num = 0
    for i in range(n):
        if i%3 == 0:
            for j in range(i//3, n):
                if answer[j][i//3] != 0:
                    continue
                num += 1
                answer[j][i//3] = num
        elif i%3 == 1:
            for j in range(n-i//3-1):
                if answer[n-i//3-1][j+1] != 0:
                    continue
                num += 1
                answer[n-i//3-1][j+1] = num
        else:
            for j in range(n-1):
                if n-i//3-j-1 < 0:
                    break
                if answer[n-j-1][n-i//3-j-1] != 0:
                    continue
                num += 1
                # answer[n-i-j][n-i-j] = (n*i) + j
                answer[n-j-1][n-i//3-j-1] = num

    return [t for temp in answer for t in temp]

if __name__ == '__main__':
    for i in range(1, 1001): # 문제 조건 검사
        try:
            solution(i)
            print(i, 'done')
        except:
            print(i)
            break

    # solution(15)
