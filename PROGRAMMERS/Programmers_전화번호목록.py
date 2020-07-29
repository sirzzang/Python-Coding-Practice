'''3) 접두사만 체크하도록 2) 수정'''
def solution(phone_book):
    for i in range(len(phone_book)):
        flag = phone_book[i]
        for v in phone_book[:i] + phone_book[i+1:]:
            if flag in v and v.find(flag) == 0: # 맨 앞에 나오는 경우만
                return False
    return True

'''2) 정확성 테스트 2개 실패'''
def solution(phone_book):
    # answer = True
    for i in range(len(phone_book)):
        flag = phone_book[i]
        for v in phone_book[:i] + phone_book[i+1:]:
            if flag in v:
                return False
    return True

'''1) 시간 초과, 정확성 테스트 2개 실패'''
def solution(phone_book):
answer = True

phone_dict = {}
for i in range(len(phone_book)):
    phone_dict[phone_book[i]] = phone_book[:i] + phone_book[i + 1:]

for key, val in phone_dict.items():
    for v in val:
        if key in v:
            answer = False
            return answer
return answer
