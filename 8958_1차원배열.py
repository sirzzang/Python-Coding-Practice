import sys

s = sys.stdin

n = int(s.readline())  # 이거는 첫 줄에 입력할 것 -> 내가 입력하면 백준이 알아서 그 크기만큼 입력해주겠지 개수

tests = s.readlines()

for test in tests:
    test = test.rstrip("\n")
    i = 1
    num = 0
    answer = 0

    while i < len(test):
        chunk = test[0:i]
        i += 1    
        if chunk[-1] == "X":
            num = 0
        else:        
            while True:
                indexNum = chunk.find("X")
                if indexNum != -1:
                    chunk = chunk[indexNum+1:]
                else:
                    break
            num = chunk.count("O")    
        answer += num
    print(answer)


# 정규식가지고 풀어보기 import re!

#  문제를 잘못 이해했잖아 멍충아!

# import re                             # 정규식 사용하기 위한 모듈.
# itemSequence = "A7B5C4A1A8B9B3A5A8B9B1C7C1A1B3C7B9B3A7B8A1C9A8C9C7B9C3A5A8B3C9C8A7A8B9C9C7"

# regex = re.compile(".[789]")           # 앞에 문자는 상관 없고 뒤에 숫자가 789인 애들 찾기
# result = regex.findall(itemSequence)
# valid_str = "".join(result)
# regex = re.compile("A.B.C.")
# result = regex.findall(valid_str)
# print(result)