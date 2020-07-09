def solution(answers):
    res = [0, 0, 0, 0]
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]        
    for i in range(len(answers)):
        if first[i%5] == answers[i]:
            res[1] += 1
        if second[i%8] == answers[i]:
            res[2] += 1
        if third[i%10] == answers[i]:
            res[3] += 1
    answer = []
    for i, v in enumerate(res):
        if v == max(res):
            answer.append(i)
    return answer

def solution(answers):
    res = [0, 0, 0, 0]
    first = [1, 2, 3, 4, 5]

    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if first[i%len(first)] == answers[i]:
            res[1] += 1
    for i in range(len(answers)):
        if second[i%len(second)] == answers[i]:
            res[2] += 1
    for i in range(len(answers)):
        if third[i%len(third)] == answers[i]:
            res[3] += 1
    # print(res)
    answer = []
    for i, v in enumerate(res):
        if v == max(res):
            answer.append(i)
    return answer

# 아래처럼 하려면 elif쓰면 안 되고 if써야 한다.
def solution(answers):
    res = [0, 0, 0, 0]
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if first[i%len(first)] == answers[i]:
            res[1] += 1
        if second[i%len(second)] == answers[i]:
            res[2] += 1
        if third[i%len(third)] == answers[i]:
            res[3] += 1
    answer = []
    for i, v in enumerate(res):
        if v == max(res):
            answer.append(i)
    return answer