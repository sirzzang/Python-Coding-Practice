def solution(n, words):
    # answer = []
    for i, v in enumerate(words):
        if i > 0 and (v[0] != words[i-1][-1] or v in words[:i]): # 지는 조건
            # print(i, v, "졌습니다")
            return [i%n+1, i//n+1]
    else:
        return [0, 0]