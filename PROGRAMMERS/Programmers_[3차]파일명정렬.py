# 파이썬 정렬: 정렬은 안정적임이 보장됩니다. 즉, 여러 레코드가 같은 키를 가질 때, 원래의 순서가 유지됩니다.
import re

def solution(files):
    answer = []
    for file in files:
        number = re.findall('[0-9]+', file)[0]
        head, tail = re.split('[0-9]+', file, maxsplit=1)
        answer.append([head, number, tail])
    print(f"정렬 전: {answer}")
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    for i in range(len(answer)):
        answer[i] = "".join(answer[i])
    print(f"정렬 후: {answer}\n")
    return answer


solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])
solution(["MUZI01.zip", "muzi1.png"])