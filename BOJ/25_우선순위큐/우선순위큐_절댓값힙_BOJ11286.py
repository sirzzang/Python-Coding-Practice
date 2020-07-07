import sys
import heapq

N = int(sys.stdin.readline())
neg_heap = []
pos_heap = []

for _ in range(N):
    num = int(sys.stdin.readline())

    if num > 0:
        heapq.heappush(pos_heap, num)
    
    elif num < 0 :
        heapq.heappush(neg_heap, -num)
    
    else: # 0이 들어올 때
        try:
            if pos_heap[0] < neg_heap[0]:
                print(heapq.heappop(pos_heap))
            elif pos_heap[0] >= neg_heap[0]:
                print(-heapq.heappop(neg_heap))
        except IndexError:
            if len(neg_heap) == 0:
                if len(pos_heap) == 0:
                    print(0)
                else:
                    print(heapq.heappop(pos_heap))
            elif len(pos_heap) == 0:
                if len(neg_heap) == 0:
                    print(0)
                else:
                    print(-heapq.heappop(neg_heap))










        # try:
        #     while pos_heap[0] < neg_heap[0]:
        #         print(heapq.heappop(neg_heap))
        
        # except IndexError:
        #     if len(neg_heap) == 0:
        #         if len(pos_heap) == 0:
        #             print(0)
        #         else:
        #             pass

        # else:
        #     print(heapq.heappop(pos_heap))