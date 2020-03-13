# 결국 이 두 방식은 모두 heappop을 통해 접근하고, 이 과정에서 heap이 초기화된다는 문제를 해결하려다가 시간 초과가 난다.

# 첫 번째 제출.
# 중간값 인덱스를 찾기는 했는데, 그 인덱스까지 pop하면 결국 받아 놓은 heap이 사라지게 된다.
# 그래서 nsmallest를 이용해 중간값 인덱스까지 모든 원소를 반환함으로써 입력받아 놓은 heap을 유지하고자 했다. 
# 중간값 인덱스를 찾고, nsmallest를 이용해 그 인덱스까지 접근하는 데서 시간복잡도가 늘어날 것 같다.
# 마지막에 nsmallest에서 [-1]로 접근하지 않고, pop()으로 빼온다고 해도, 애초에 접근 자체가 시간이 오래 걸리는 방식이다.


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
        print(heapq.nsmallest(center, heap).pop()) 
        # [-1]로 접근하는 것보다 pop()이 시간복잡도가 더 낮을 것이라 판단.

# 두 번째 제출.
# 첫 번째 제출 방법보다 당연히 시간이 많이 걸릴 수밖에 없다.
# 1) 수열을 전부 다 받아 놓고, while loop를 돌 때마다 slicing을 통해 heap을 초기화한다.
# - pop을 하더라도 새롭게 입력받아 놓은 숫자들은 초기화되지 않는다.
# 2) 중간값 인덱스에 도달할 때까지 pop하고 출력한다.
# 첫 번째 제출 방법보다 더 시간이 많이 걸릴 수밖에 없다.
# while이 있고, 각 단계별로 while문 안에서 for문을 돌면서 pop해오는 구조이기 때문이다.

import sys
import heapq

user_input = sys.stdin.readlines()
len_heap = 1 # heap의 길이

while len_heap <= int(user_input[0]):

    heap = []
    for i in user_input[1:len_heap+1]:
        heapq.heappush(heap, int(i)) # 숫자 하나 더 말할 때마다 heap에 push

    if len_heap == 1 or len_heap == 2:
        print(min(heap))
    else:        
        if len_heap % 2 == 0: # 짝수 개일 때는 어차피 가운데 두 개 중 왼쪽이 작으므로 중간값
            ctr_idx = len_heap//2 -1
        else:                # 홀수 개일 때는 가운데 애가 중간값
            ctr_idx = len_heap//2

        ctr = None
        for _ in range(ctr_idx+1): # ctr_idx에 갈 때까지 pop
            ctr = heapq.heappop(heap)
        print(ctr)

    len_heap += 1