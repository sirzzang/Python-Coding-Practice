# 메모화 필수
# 이동 횟수 : 2의 거듭제곱.. https://en.wikipedia.org/wiki/Tower_of_Hanoi

def Hanoi_cnt(n, start, end, spare):
    if n in cnt_dict: # 메모화
        return cnt_dict[n]
    cnt = Hanoi_cnt(n-1, start, spare, end) + Hanoi_cnt(1, start, end, spare) + Hanoi_cnt(n-1, spare, end, start)
    cnt_dict[n] = cnt
    return cnt

def Hanoi_path(n, start, end, spare):
    if n == 1:
        print(start, end)
        return # 없으면 RecursionError
    Hanoi_path(n-1, start, spare, end)
    print(start, end)
    Hanoi_path(n-1, spare, end, start)

cnt_dict = {1: 1} # BaseCase 설정

N = int(input())

if N <= 20:
    print(Hanoi_cnt(N, 1, 3, 2))
    Hanoi_path(N, 1, 3, 2)
else:
    print(Hanoi_cnt(N, 1, 3, 2))