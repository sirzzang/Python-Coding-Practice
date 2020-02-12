# 최소의 강의실을 사용해야 한다.
# 1 3 - 3 5 이렇게 이어지는 애들은 한 강의실에서 할 수 있으니까 cnt += 1하면 안 된다.
# 회의실 문제 변형하면, 끝 시간으로 쭉 정렬한 애가 한 강의실에서 할 수 있는 애들.
# 근데 좀 응용해야 하는게, 처음 애 말고 그 다음 애가 한 강의실에서 할 수 있을 경우도 있다.

# 시간 초과 3번 떴다

# n = int(input())
# lectures = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x : x[0])
                  
# meeting_room = [0] * len(lectures)

# for i in range(len(lectures)):
#     end = lectures[i][1]
#     for j in range(i+1, len(lectures)):
#         if lectures[j][0] >= end:
#             end = lectures[j][1]
#             meeting_room[j] += 1

# print(meeting_room.count(0))

# n = int(input())
# lectures = [list(map(int, input().split())) for _ in range(n)]

# meeting_room = [0] * len(lectures)

# for i in range(len(lectures)):
#     end = lectures[i][1]
#     for j in range(i+1, len(lectures)):
#         if lectures[j][0] >= end:
#             end = lectures[j][1]
#             meeting_room[j] += 1

# print(meeting_room.count(0))