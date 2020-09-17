import sys
import heapq

min_heap = []

N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        if len(min_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(min_heap))
            print(min_heap)
    
    else:
        heapq.heappush(min_heap, num)
        print(min_heap)