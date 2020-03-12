# 시간초과

import sys
import heapq

N = int(sys.stdin.readline())
heap = []
len_heap = 0

for _ in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))
    len_heap += 1
    if len_heap == 1 or len_heap == 2:
        print(min(heap))
    else:
        if len_heap % 2 == 1:
            center = len_heap//2+1
        else:
            center = len_heap//2
        print(heapq.nsmallest(center, heap).pop()) # [-1]로 접근하는 것보다 pop()이 시간복잡도가 더 낮을 것이라 판단.
        

