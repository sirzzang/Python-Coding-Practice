# 1차 시도
'''
정확성  테스트
테스트 1 〉	통과 (0.40ms, 10.1MB)
테스트 2 〉	통과 (0.33ms, 10.2MB)
테스트 3 〉	통과 (0.27ms, 10.1MB)
테스트 4 〉	통과 (0.24ms, 10.2MB)
테스트 5 〉	통과 (0.31ms, 10.2MB)
테스트 6 〉	통과 (0.24ms, 10.2MB)
테스트 7 〉	통과 (6.84ms, 10.2MB)
테스트 8 〉	통과 (8.63ms, 10.2MB)
테스트 9 〉	통과 (11.30ms, 10.2MB)
테스트 10 〉	통과 (8.10ms, 10.2MB)
테스트 11 〉	통과 (6.94ms, 10.2MB)
테스트 12 〉	통과 (8.20ms, 10.3MB)
테스트 13 〉	통과 (119.14ms, 10.4MB)
테스트 14 〉	통과 (116.16ms, 10.4MB)
테스트 15 〉	통과 (121.54ms, 10.1MB)
테스트 16 〉	통과 (105.10ms, 10.4MB)
테스트 17 〉	통과 (101.50ms, 10.5MB)
테스트 18 〉	통과 (120.08ms, 10.2MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (런타임 에러) : 전부 다 와일드카드가 들어 오는 경우.
테스트 4 〉	통과 (102.49ms, 13.4MB)
테스트 5 〉	통과 (120.66ms, 13.7MB)
'''

# 2차 시도
'''
정확성  테스트
테스트 1 〉	통과 (0.39ms, 10.2MB)
테스트 2 〉	통과 (0.20ms, 10.1MB)
테스트 3 〉	통과 (0.25ms, 10.1MB)
테스트 4 〉	통과 (0.20ms, 10.3MB)
테스트 5 〉	통과 (0.24ms, 10.2MB)
테스트 6 〉	통과 (0.21ms, 10.2MB)
테스트 7 〉	통과 (7.47ms, 10.2MB)
테스트 8 〉	통과 (9.35ms, 10.3MB)
테스트 9 〉	통과 (11.16ms, 10.2MB)
테스트 10 〉	통과 (6.15ms, 10.1MB)
테스트 11 〉	통과 (6.37ms, 10.2MB)
테스트 12 〉	통과 (6.72ms, 10.2MB)
테스트 13 〉	통과 (99.33ms, 10.4MB)
테스트 14 〉	통과 (99.87ms, 10.3MB)
테스트 15 〉	통과 (121.43ms, 10.4MB)
테스트 16 〉	통과 (121.58ms, 10.4MB)
테스트 17 〉	통과 (101.83ms, 10.3MB)
테스트 18 〉	통과 (133.73ms, 10.3MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	통과 (48.13ms, 13.5MB)
테스트 5 〉	통과 (55.46ms, 13.7MB)
'''

def solution(words, queries):
    answer = []
    for query in queries:
        temp = 0
        indices = [pos for pos, char in enumerate(query) if char != '?']
        if len(indices) == 0: # 전부 다 와일드카드인 경우: 런타임에러 원인.
            for word in words:
                if len(word) == len(query):
                    temp += 1
        else:
            min_idx, max_idx = indices[0], indices[-1]
            for word in words:
                if len(word) != len(query): # 첫 번째 조건: 글자 수
                    continue
                if query[min_idx:max_idx+1] == word[min_idx:max_idx+1]: # 두 번째 조건: 와일드카드 부분
                    temp += 1
        answer.append(temp)
    return print(answer)

if __name__ == '__main__':
    solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
             ["fro??", "????o", "fr???", "fro???", "pro?"])
    solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
             ["?????", "????o", "fr???", "fro???", "pro?"])