import sys

T = int(sys.stdin.readline())
lectures = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(T)], key = lambda x : x[0])
# print(lectures)
rooms = [0] * (T)
# print(rooms)


# lectures = [[0, 6], [1, 4], [2, 13], [3, 5], [3, 8], [5, 7], [5, 9], [6, 10], [8, 11], [8, 12], [12, 14]]# 디버그용
# rooms = [0] * len(lectures)
# print("강의 리스트 :", lectures) # 디버그용
# print("강의실 번호 :", rooms) # 디버그용

# 이러면 바뀌었던 애들도 계속 바뀐다!
room_num = 1
for i in range(len(lectures)):
    if rooms[i] == 0:
        rooms[i] = room_num
        end_time = lectures[i][1]
        for j in range(i+1, len(lectures)):
            if lectures[j][0] >= end_time and rooms[j]==0: 
                rooms[j] = room_num
                end_time = lectures[j][1]        
        room_num += 1
print(room_num-1)

# print("최종 강의실 번호 :", rooms) # 디버그용

    
    



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