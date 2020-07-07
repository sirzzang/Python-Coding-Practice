import sys

def hansu(N):
    global cnt

    for num in range(1, N+1):
        if num < 100:
            cnt += 1
        else:
            hansu_set = set()
            for i in range(len(str(num))-1):
                hansu_set.add(int(str(num)[i])-int(str(num)[i+1]))
            if len(hansu_set) == 1:
                cnt += 1

    return cnt

n = int(sys.stdin.readline())
cnt = 0

print(hansu(n))