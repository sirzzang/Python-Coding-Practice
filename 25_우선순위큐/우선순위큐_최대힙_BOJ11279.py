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





# user_input = sys.stdin.readlines()
# print(user_input)

# heap = [int(i) for i in user_input[1:]]
# heapq.heapify(heap)
# print(heap)

# for com in heap:
#     if com == 0:



# M = 0
# pop_idx = 0
# cur_idx = 0
# ln = int(user_input[0])

# for com in user_input[1:]:
#     com = int(com)

#     if com == 0:
#         if pop_idx == 0:
#             print(0)
#             pop_idx = cur_idx
#         elif cur_idx == pop_idx:
#             print(M)
#             pop_idx -= 1
#             M = int(user_input[1:][pop_idx])
#         else:
#             print(M)
#             pop_idx += 1
#         cur_idx += 1
    
#     else:
#         if com >= M:
#             M = com
#             pop_idx = cur_idx
#         else:
#             cur_idx += 1
#         cur_idx += 1 





# for com in user_input[1:]:
#     com = int(com)

#     if com == 0:
#         if len(stack) == 0:
#             print(0)
#         else:
#             print(stack.pop())
#     else:
#         if len(stack) == 0: # 비어 있으면 append
#             stack.append(com)
#         elif com >= stack[-1]: # 안 비어 있고, 넣을 수가 최댓값보다 크다면 append
#             stack.append(com)
#         else:
#             idx = 0
#             while com > stack[idx]: # 넣을 수가 stack에 있는 수보다 작아질 때까지 순회
#                 idx += 1
#             left = stack[:idx] # 넣을 수보다 작은 원소들
#             right = stack[idx:] # 넣을 수보다 큰 원소들
#             left.append(com) # left에 수 넣고
#             stack = left + right # 둘이 합쳐서 stack 초기화




# # # 큰 수가 가장 뒤로 가게 구현할 것.

# # for _ in range(n):
# #     com = int(sys.stdin.readline())

# #     if com == 0: # 비어 있으면 0, 아니면 마지막 위치 pop.
# #         if len(stack) == 0:
# #             print(0)
# #         else:
# #             print(stack.pop())

# #     else:
# #         if len(stack) == 0: # 비어 있으면 append
# #             stack.append(com)
# #         elif com >= stack[-1]: # 안 비어 있고, 넣을 수가 최댓값보다 크다면 append
# #             stack.append(com)
# #         else:
# #             idx = 0
# #             while com > stack[idx]: # 넣을 수가 stack에 있는 수보다 작아질 때까지 순회
# #                 idx += 1
# #             left = stack[:idx] # 넣을 수보다 작은 원소들
# #             right = stack[idx:] # 넣을 수보다 큰 원소들
# #             left.append(com) # left에 수 넣고
# #             stack = left + right # 둘이 합쳐서 stack 초기화

# # # stack = [3]

# # # # stack[:1]까지는 괜찮은데, append하면 none이 된다.

# # # left = stack[:1]
# # # left.append(2)
# # # print(left)
# # # right = stack[1:]
# # # print(right)
# # # print(left+right)

# # # # print(type(stack[:1]))
# # # # print(stack[0:])

                