# 첫 번째 제출

import sys
import heapq

max_heap = []
N = int(sys.stdin.readline())

for _ in range(N):
    com = int(sys.stdin.readline())

    if com == 0:
        if len(max_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(max_heap)[1])
    
    else:
        heapq.heappush(max_heap, (-com, com))

# 두 번째 제출

import sys
import heapq

max_heap = []
N = int(sys.stdin.readline())

for _ in range(N):
    com = int(sys.stdin.readline())

    if com == 0:
        if len(max_heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(max_heap))
    
    else:
        heapq.heappush(max_heap, -com)