# 서류 심사와 면접 성적이 모두 떨어진다면 결코 선발되지 않는다
# 서류 심사로 먼저 정렬 -> 면접 성적 떨어지면 선발 안하는 list 추가

# 시간 초과2
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     candidates = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x : (x[0], x[1]))
#     # 서류점수 1,2,3,4,5등 순이니까, 면접도 2등이 1등보다 낮으면, 3등이 2등이나 1등보다 낮으면 안 된다.

#     interview = len(candidates)
#     recruited = 0

#     for candidate in candidates:
#         if candidate[1] < interview:
#             interview = candidate[1]
#             recruited += 1
#     print(recruited)
                       
# 시간 초과1
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     candidates = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x : (x[0], x[1]))    
#     recruited = [0]*n
#     for i in range(len(candidates)-1):
#         if candidates[i+1][1] > candidates[i][1]:
#             recruited[i+1] += 1 

# print(recruited.count(0))