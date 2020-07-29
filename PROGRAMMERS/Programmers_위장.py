def solution(clothes):
    # 의상 dictionary
    outfit = {}
    for c in clothes:
        if c[1] in outfit:
            outfit[c[1]].append(c[0])
        else:
            outfit[c[1]] = [c[0]]
    print(outfit)

    # 모든 가능한 조합 구하기
    answer = 1
    for v in outfit.values():
        answer *= (len(v) + 1)
        
    return answer - 1