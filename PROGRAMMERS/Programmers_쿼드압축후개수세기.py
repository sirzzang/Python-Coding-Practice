'''
문제출처: https://programmers.co.kr/learn/courses/30/lessons/68936
'''

# # 첫 번째
# '''
# 테스트 1 〉	통과 (1.70ms, 10.2MB)
# 테스트 2 〉	통과 (0.98ms, 10.2MB)
# 테스트 3 〉	통과 (0.47ms, 10.2MB)
# 테스트 4 〉	통과 (0.13ms, 10.1MB)
# 테스트 5 〉	통과 (436.13ms, 13.1MB)
# 테스트 6 〉	통과 (123.48ms, 13MB)
# 테스트 7 〉	통과 (58.21ms, 13.1MB)
# 테스트 8 〉	통과 (23.30ms, 13.1MB)
# 테스트 9 〉	통과 (9.54ms, 13MB)
# 테스트 10 〉	실패 (28.66ms, 22.1MB)
# 테스트 11 〉	통과 (0.07ms, 10.1MB)
# 테스트 12 〉	통과 (0.52ms, 10.1MB)
# 테스트 13 〉	통과 (13.77ms, 13.1MB)
# 테스트 14 〉	통과 (111.63ms, 22.2MB)
# 테스트 15 〉	통과 (184.67ms, 22.2MB)
# 테스트 16 〉	통과 (89.83ms, 13.1MB)
# '''
#
# def solution(arr, answer):
#
#     dx = len(arr)//2
#     dy = len(arr)//2
#     for y in range(0, dy * 2, dy):
#         for i in range(2):
#             temp = [arr[x][dx*i:dx*(i+1)] for x in range(y, y+dx)]
#             print(temp)
#             numbers = {x for t in temp for x in t}
#             if len(numbers) == 2:
#                 solution(temp, answer)
#             else:
#                 answer[list(numbers)[0]] += 1
#     return answer
#
#     # if dx == 0: # dx가 0이 아니다!
#     #     return answer


# 두 번째 풀이: 시간 + 체크하는 부분 합치는 방법 고민.
'''
테스트 1 〉	통과 (1.94ms, 10.3MB)
테스트 2 〉	통과 (1.53ms, 10.1MB)
테스트 3 〉	통과 (0.56ms, 10.3MB)
테스트 4 〉	통과 (0.15ms, 10.1MB)
테스트 5 〉	통과 (513.48ms, 13.2MB)
테스트 6 〉	통과 (152.14ms, 13.2MB)
테스트 7 〉	통과 (78.97ms, 13.1MB)
테스트 8 〉	통과 (35.75ms, 13.1MB)
테스트 9 〉	통과 (15.70ms, 13MB)
테스트 10 〉	통과 (18.23ms, 18.8MB)
테스트 11 〉	통과 (0.08ms, 10.1MB)
테스트 12 〉	통과 (0.13ms, 10.2MB)
테스트 13 〉	통과 (23.33ms, 13.1MB)
테스트 14 〉	통과 (189.90ms, 22.2MB)
테스트 15 〉	통과 (296.07ms, 22.2MB)
테스트 16 〉	통과 (124.45ms, 13.1MB)
'''
def solution(arr, answer):

    numbers = {x for t in arr for x in t}
    if len(numbers) == 1:
        answer[list(numbers)[0]] += 1
        return answer

    dx = len(arr)//2
    dy = len(arr)//2
    for y in range(0, dy * 2, dy):
        for i in range(2):
            temp = [arr[x][dx*i:dx*(i+1)] for x in range(y, y+dx)]
            print(temp)
            numbers = {x for t in temp for x in t}
            if len(numbers) == 2:
                solution(temp, answer)
            else:
                answer[list(numbers)[0]] += 1
    return answer

    # if dx == 0: # dx가 0이 아니다!
    #     return answer

if __name__ == '__main__':
    print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]], [0, 0]))
    print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]], [0, 0]))
    print(solution([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]], [0, 0])) # 첫 번째 풀이에서 틀리는 부분.