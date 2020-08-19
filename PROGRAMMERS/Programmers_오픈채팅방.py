def solution(record):
    messages = []

    # action 확인
    users = {}
    for r in record:
        action, user_info = r.split(' ', maxsplit=1)
        if action == "Enter":
            messages.append([user_info.split()[0], "님이 들어왔습니다."])
            users[user_info.split()[0]] = user_info.split()[1]
        elif action == "Leave":
            messages.append([user_info.split()[0], "님이 나갔습니다."])
        else:
            users[user_info.split()[0]] = user_info.split()[1]
    for i in range(len(messages)):
        messages[i][0] = users.get(messages[i][0])
        messages[i] = ''.join(messages[i])

    return messages



'''
테스트 1 〉	통과 (0.06ms, 10.7MB)
테스트 2 〉	통과 (0.07ms, 10.6MB)
테스트 3 〉	통과 (0.14ms, 10.8MB)
테스트 4 〉	통과 (0.17ms, 10.6MB)
테스트 5 〉	통과 (1.81ms, 11.1MB)
테스트 6 〉	실패 (30.10ms, 11.3MB)
테스트 7 〉	통과 (1.72ms, 11MB)
테스트 8 〉	실패 (1628.88ms, 11.2MB)
테스트 9 〉	실패 (209.07ms, 12.1MB)
테스트 10 〉	실패 (29.03ms, 11.5MB)
테스트 11 〉	실패 (78.75ms, 11.3MB)
테스트 12 〉	실패 (69.65ms, 11.2MB)
테스트 13 〉	실패 (38.89ms, 11.5MB)
테스트 14 〉	실패 (262.25ms, 12.4MB)
테스트 15 〉	통과 (0.06ms, 10.6MB)
테스트 16 〉	실패 (0.68ms, 10.7MB)
테스트 17 〉	실패 (3.06ms, 10.8MB)
테스트 18 〉	실패 (2.19ms, 10.9MB)
테스트 19 〉	실패 (48.74ms, 11.6MB)
테스트 20 〉	실패 (6.86ms, 11.2MB)
테스트 21 〉	실패 (43.15ms, 11.2MB)
테스트 22 〉	실패 (43.81ms, 11.2MB)
테스트 23 〉	통과 (6.04ms, 11.1MB)
테스트 24 〉	실패 (68.44ms, 11.6MB)
테스트 25 〉	실패 (시간 초과)
테스트 26 〉	실패 (시간 초과)
테스트 27 〉	실패 (시간 초과)
테스트 28 〉	실패 (시간 초과)
테스트 29 〉	실패 (시간 초과)
테스트 30 〉	실패 (시간 초과)
테스트 31 〉	실패 (시간 초과)
테스트 32 〉	실패 (시간 초과)
'''
#
# def solution(record):
#     messages = []
#
#     # action 확인
#     for r in record:
#         action, user_info = r.split(' ', maxsplit=1)
#         if action == "Enter":
#             messages.append(user)ub
#         print(r, r.split()[0])
    #
    #
    # users = {}
    # for r in record:
    #     action, user_info = r.split(maxsplit=1)
    #     if action == "Enter":
    #         uid, uname = user_info.split()
    #         messages.append(printEnterMessage(uid))
    #         # print(printEnterMessage(uname))
    #         users[uid] = uname # 이름 저장
    #     elif action == "Leave":
    #         messages.append(printExitMessage(user_info)) # user_info = id
    #         # print(printExitMessage(users[user_info]))
    #     else: # change일 경우
    #         uid, uname = user_info.split()
    #         users[uid] = uname
    #
    # print(f"최종 아이디-닉네임: {users}")
    # print(f"바꾸기 전: {messages}")
    # for i in range(len(messages)):
    #     for uid in users.keys():
    #         messages[i] = messages[i].replace(uid, users.get(uid))
    # print(f"바꾼 후: {messages}")

    # return messages

# 테스트
solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])