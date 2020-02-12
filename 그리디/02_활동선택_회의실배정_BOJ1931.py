# 정답 인정 : 시간이 너무 오래 걸린다
def greedy_meeting(timetable):
    cnt = 0
    end = 0
    for time in timetable :
        if time[0] >= end :
            end = time[-1]
            cnt += 1
    return cnt

t = int(input())
timetable = sorted([list(map(int, input().split(' '))) for _ in range(t)], key = lambda x: (x[-1], x[0]))

print(greedy_meeting(timetable))


# timetable 미리 정의 안하면 런타임에러 뜬다.
# 시간초과

# t = int(input())
# timetable = sorted([list(map(int, input().split(' '))) for _ in range(t)], key = lambda x: x[-1]) # 회의 끝나는 시간에 따라 정렬

# def greedy_time(timetable):
#     cnt = 0
#     end = 0
#     for time in timetable:
#         if end <= time[0]: # 시작 시간이 기준 time보다 뒤라면
#             end = time[1] # 기준 time을 해당 시간대의 끝 타임으로 바꾸고
#             cnt += 1 # 회의 숫자에 하나 추가
#     return print(cnt)

# greedy_time(timetable)

            



