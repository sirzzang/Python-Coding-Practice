def Hanoi_cnt(n, start, end, spare):
    global cnt_dict
    if n in cnt_dict:
        return cnt_dict[n]
    cnt = Hanoi_cnt(n-1, start, spare, end) + 1 + Hanoi_cnt(n-1, spare, end, start)
    cnt_dict[n] = cnt
    return cnt

def Hanoi_path(n, start, end, spare):
    if n == 1:
        print(start, end)
        return
    Hanoi_path(n-1, start, spare, end)
    print(start, end)
    Hanoi_path(n-1, spare, end, start)


cnt_dict = {1:1}

N = int(input())
print(Hanoi_cnt(N, 1, 3, 2))
Hanoi_path(N, 1, 3, 2)