# 1) 틀린 풀이
def solution(participant, completion):
    # 동명이인 있어도 어차피 걔가 완주 못했으면 홀수 아닌가?
    run_dict = {}
    for p in participant:
        if p not in run_dict:
            run_dict[p] = 1
        if p in completion:
            run_dict[p] += 1

    print(run_dict)
    for k, v in run_dict.items():
        if v % 2 != 0:
            answer = k
    return answer

# 2) 해쉬 안 썼는데?
def solution(participant, completion):
    participant.sort()
    completion.sort()
    # print(f"참가자: {participant}")
    # print(f"완주자: {completion}")

    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return participant[i]
    else:
        return participant[-1]