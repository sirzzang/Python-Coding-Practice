def solution(p, s):
    # 남은 기간으로 바꿔 주기
    for i in range(len(p)):
        if (100 - p[i]) % s[i] == 0:
            p[i] = (100 - p[i]) // s[i]
        else:
            p[i] = (100 - p[i]) // s[i]
            p[i] += 1

    # 작업 기간 비교
    max_day = p[0]
    answer = [1]
    for i in range(len(p)):
        if p[i] <= max_day:
            answer[-1] += 1
        else:
            max_day = p[i]
            answer.append(1)

    return answer