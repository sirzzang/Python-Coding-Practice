def rshift(lst): # 오른쪽 이동
    for idx, value in enumerate(lst[:]):
        lst[(idx+1) % len(lst)] = value
    return lst

def lshift(lst): # 왼쪽 이동
    for idx, value in enumerate(lst[:]):
        lst[(idx-1) % len(lst)] = value
    return lst

def pop(lst):
    lst.pop(0)
    return lst

import sys

n, m = map(int, sys.stdin.readline().split())
extract = list(map(int, sys.stdin.readline().split())) # 뽑아 낼 숫자 list.

queue = list(range(1, n+1))
cnt = 0

for flag in extract: # flag = 뽑아 낼 숫자.
    # flag가 top에 있을 때만 뽑음.

    idx = queue.index(flag) # flag의 위치
    
    if idx == 0:
        pop(queue)
    
    else:
        if idx <= len(queue) - idx: # flag가 앞쪽에 가까우면,
            while idx != 0: # flag가 top에 올 때까지,
                lshift(queue) # 왼쪽 이동.
                cnt += 1
                idx -= 1 # flag의 위치 왼쪽으로 한 칸씩 밀어줌.
            pop(queue) # top에 오면 뽑아 냄.
        else:
            while idx != 0:
                rshift(queue)
                cnt += 1
                idx = (idx+1) % len(queue)
            pop(queue)

print(cnt)



