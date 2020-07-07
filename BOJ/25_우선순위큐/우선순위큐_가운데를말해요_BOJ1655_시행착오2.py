import sys
import heapq

len_heap = 1
min_heap = []
max_heap = []
ctr = None

N = int(sys.stdin.readline())


# values = [1, 5, 2, 10, -99, 7, 5] : 디버그용
# values = [-1, -3, 5, 4, 2, 131, -1110, 13579, -7, 7, 6, 4]

for _ in range(N):
    
    # for value in values: # : 디버그용
    val = int(sys.stdin.readline())
    # val = value #: 디버그용

    if len_heap == 1 :
        heapq.heappush(max_heap, val)
        len_heap += 1
        ctr = val
        print("min", min_heap, "max", max_heap)
        print("현재 중간값", ctr)
    
    # elif len_heap == 2:
    #     if val > ctr : # 원래 max에 있던 애가 min으로 가야 함. max에 val push.
    #         if ctr < 0 :
    #             heapq.heappush(min_heap, (ctr, ctr))
    #             heapq.heappush(max_heap, val)
    #             len_heap += 1
    #         else:
    #             heapq.heappush(min_heap, (-ctr, ctr))
    #             heapq.heappush(max_heap, val)
    #             len_heap += 1
    #     else:
    #         if val < 0 :
    #             heapq.heappush(min_heap, (val, val))
    #             len_heap += 1
    #         else:
    #             heapq.heappush(min_heap, (-val, val))
    #     ctr = min_heap[0][1]
    #     print("min", min_heap, "max", max_heap)
    #     print("현재 중간값", ctr)

    else:
        if len_heap % 2 == 1: # 전체 개수가 홀수일 때, 이전에 min_heap과 max_heap의 개수가 같으므로, ctr보다 크거나 같은 값이 들어오면 max에 push. 아니면 min pop하고 max로 옮긴 뒤 val을 min에 push. 중간값은 max_heap의 최솟값.
            if val >= ctr : # max에 push해야 함.
                heapq.heappush(max_heap, val)
                len_heap += 1
            else:
                heapq.heappush(max_heap, heapq.heappop(min_heap)[1])
                heapq.heappush(min_heap, (-val, val))
                len_heap += 1
                # if val < 0 :
                #     heapq.heappush(min_heap, (val, val))
                #     len_heap += 1
                # else:
                #     heapq.heappush(min_heap, (-val, val))
                #     len_heap += 1
            ctr = max_heap[0]
            print("min", min_heap, "max", max_heap)
            print("현재 중간값", ctr)        
        elif len_heap % 2 == 0: # 전체 개수가 짝수일 때, 이전에 max_heap의 개수가 한 개 더 많으므로, ctr보다 큰 값이 들어오면 max pop후 min으로 옮기고 val을 max에 push. 작거나 같은 값이 들어오면 min에 push.
            if val > ctr :
                heapq.heappush(min_heap, (-ctr, heapq.heappop(max_heap)))
                # if ctr < 0 :
                #     heapq.heappush(min_heap, (ctr, heapq.heappop(max_heap)))
                # else:
                #     heapq.heappush(min_heap, (-ctr, heapq.heappop(max_heap)))                
                heapq.heappush(max_heap, val)
                len_heap += 1
            else:
                heapq.heappush(min_heap, (-val, val))
                len_heap += 1


                # if val < 0 :
                #     heapq.heappush(min_heap, (val, val))
                #     len_heap += 1
                # else:
                #     heapq.heappush(min_heap, (-val, val))
                #     len_heap += 1
            ctr = min_heap[0][1]
            print("min", min_heap, "max", max_heap)
            print("현재 중간값", ctr)
        
        

