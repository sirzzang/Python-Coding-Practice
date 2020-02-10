# timetable 미리 정의 안하면 런타임에러 뜬다.

timetable = []
t = int(input())

for _ in range(t):
    timetable.append(list(map(int, input().split())))
    timetable.sort(key = lambda x: x[-1]) # 회의 끝나는 시간에 따라 정렬

def greedy_time(timetable):
    cnt = 0
    time = 0
    for meeting in timetable:
        if time <= meeting[0]: # 시작시간이 기준 time보다 뒤라면
            time = meeting[1] # 기준 time을 해당 시간대의 끝 타임으로 바꾸고
            cnt += 1 # 회의 숫자에 하나 추가
    return print(cnt)

greedy_time(timetable)

            



