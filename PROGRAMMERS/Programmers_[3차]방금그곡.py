# return None이 아니라 return 'None'.....
'''
테스트 1 〉	통과 (9.35ms, 10.4MB)
테스트 2 〉	통과 (8.68ms, 10.4MB)
테스트 3 〉	통과 (11.13ms, 10.6MB)
테스트 4 〉	통과 (9.20ms, 10.5MB)
테스트 5 〉	통과 (15.39ms, 10.3MB)
테스트 6 〉	통과 (8.62ms, 10.4MB)
테스트 7 〉	통과 (8.58ms, 10.4MB)
테스트 8 〉	통과 (8.54ms, 10.5MB)
테스트 9 〉	통과 (8.78ms, 10.5MB)
테스트 10 〉	통과 (10.46ms, 10.5MB)
테스트 11 〉	통과 (11.39ms, 10.4MB)
테스트 12 〉	통과 (10.53ms, 10.4MB)
테스트 13 〉	통과 (9.48ms, 10.3MB)
테스트 14 〉	통과 (6.47ms, 10.4MB)
테스트 15 〉	통과 (6.83ms, 10.4MB)
테스트 16 〉	통과 (9.79ms, 10.5MB)
테스트 17 〉	통과 (6.15ms, 10.5MB)
테스트 18 〉	통과 (6.53ms, 10.5MB)
테스트 19 〉	통과 (6.61ms, 10.4MB)
테스트 20 〉	통과 (6.46ms, 10.4MB)
테스트 21 〉	통과 (9.82ms, 10.4MB)
테스트 22 〉	실패 (6.23ms, 10.5MB)
테스트 23 〉	실패 (9.39ms, 10.4MB)
테스트 24 〉	실패 (11.81ms, 10.5MB)
테스트 25 〉	통과 (6.37ms, 10.3MB)
테스트 26 〉	통과 (5.96ms, 10.4MB)
테스트 27 〉	통과 (5.82ms, 10.6MB)
테스트 28 〉	통과 (6.06ms, 10.4MB)
테스트 29 〉	실패 (12.90ms, 10.5MB)
테스트 30 〉	통과 (8.25ms, 10.5MB)
'''
# 1) #붙은 애들 바꿔주기
# 2) 재생 시간 구하고
# 3) 음악 길이에 따라서 재생된 음악을 구하고
from datetime import datetime

def get_duration(start_time, end_time):
    return int((datetime.strptime(end_time, '%H:%M')-datetime.strptime(start_time, '%H:%M')).total_seconds() / 60)

def change_melody(melody):
    melody = list(melody)    
    stack = []
    for m in melody:
        if m == '#':
            stack[-1] = stack[-1].lower()
        else:
            stack.append(m)
    return ''.join(stack)

def solution(m, musicinfos):
    musicinfos.sort(reverse=True, key=lambda x:get_duration(x.split(',')[0], x.split(',')[1]))
    for musicinfo in musicinfos:
        start = musicinfo.split(',')[0]
        end = musicinfo.split(',')[1]
        title = musicinfo.split(',')[2]
        melody = change_melody(musicinfo.split(',')[3])
        q, r = divmod(get_duration(start, end), len(melody))
        music = melody*q + melody[:r]
        if change_melody(m) in music:
            return title
    # return None # ...
    # return 'None'


print(solution('ABCDEFG', ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']))
print(solution('CC#BCC#BCC#BCC#B', ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']))
print(solution('C#', ['03:00,03:05,FOO,CC#BCC#BCC#B', '04:00,04:05,BAR,C#CC#BCC#BCC#B', '04:00,04:06,BART,C#CC#BCC#BCC#B'])) # 문제가 생기는 테스트 케이스!
print(solution('ABC', ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']))