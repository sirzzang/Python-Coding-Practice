# 정확성 테스트 2개(3, 15) 실패
'''
문제: 동일한 재생횟수 가지는 경우
["classic", "pop", "classic", "classic", "pop"]
[500, 600, 500, 500, 600]
[0, 2, 1, 4]가 나와야 하는데, [0, 0, 1, 1]이 나온다.
'''
def solution(genres, plays):
    answer = []
    songs = {}
    for i, v in enumerate(genres):
        if v not in songs:
            songs[v] = [plays[i]]
        else:
            songs[v].append(plays[i])
    songs = sorted(songs.items(), key=lambda x: sum(x[1]), reverse=True)
    # print(songs)
    for _, s in songs:
        for i in sorted(s, reverse=True)[:2]:
            answer.append(plays.index(i))

    return answer

# 너무 길게 쓰는 게 아닌가?
def solution(genres, plays):
    answer = []
    songs = {}
    for i, v in enumerate(genres):
        if v not in songs:
            songs[v] = [plays[i], (i, plays[i])]
        else:
            songs[v][0] += plays[i]
            songs[v].append((i, plays[i]))

    songs = sorted(songs.values(), key=lambda x: x[0], reverse=True)
    # print(songs)

    for song in songs:
        for s in sorted(song[1:], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(s[0])

    return answer