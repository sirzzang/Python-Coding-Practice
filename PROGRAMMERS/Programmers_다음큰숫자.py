def count_one(n):
    n_bin = ""
    # 이진수 만들기
    while n > 0:
        q, r = divmod(n, 2)
        n_bin = str(r) + n_bin
        n //= 2
    return n_bin.count("1") # 이진수에서 1 개수 반환

def solution(n):
    answer = 0
    for i in range(n+1, 10000001):
        if count_one(i) == count_one(n):
            answer = i
            break
    return answer