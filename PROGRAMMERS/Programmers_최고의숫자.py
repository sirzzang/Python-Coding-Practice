def solution(n, s):
    if n > s:
        return [-1]
    elif n == s:
        return [1] * s
    else:
        answer = [s//n] * n
        print(f"분배해야 할 나머지: {s%n}")
        for i in range(s%n):
            answer[n-1-i] += 1
    return answer