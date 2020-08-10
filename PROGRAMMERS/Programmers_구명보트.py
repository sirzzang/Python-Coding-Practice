'''
정확성  테스트
테스트 1 〉	통과 (0.91ms, 11.1MB)
테스트 2 〉	통과 (0.76ms, 11.1MB)
테스트 3 〉	통과 (0.65ms, 11MB)
테스트 4 〉	통과 (0.62ms, 10.9MB)
테스트 5 〉	통과 (0.35ms, 10.8MB)
테스트 6 〉	통과 (0.25ms, 10.7MB)
테스트 7 〉	통과 (0.34ms, 10.9MB)
테스트 8 〉	통과 (0.06ms, 10.7MB)
테스트 9 〉	통과 (0.09ms, 10.7MB)
테스트 10 〉	통과 (0.64ms, 10.9MB)
테스트 11 〉	통과 (0.55ms, 11MB)
테스트 12 〉	통과 (0.51ms, 10.9MB)
테스트 13 〉	통과 (0.67ms, 11MB)
테스트 14 〉	통과 (0.88ms, 11MB)
테스트 15 〉	통과 (0.10ms, 10.9MB)
효율성  테스트
테스트 1 〉	통과 (9.13ms, 40.4MB)
테스트 2 〉	통과 (9.60ms, 41MB)
테스트 3 〉	통과 (8.41ms, 39.1MB)
테스트 4 〉	통과 (9.63ms, 43MB)
테스트 5 〉	통과 (9.11ms, 37.4MB)
'''
def solution(people, limit):
    answer = 0
    people.sort(reverse=True) # 내림차순 정렬: 무거운 사람부터 태워야 함.
    # print(people)
    l, r = 0, len(people)-1
    while l < r:
        # print(f"현재 왼쪽 인덱스: {l}, 오른쪽 인덱스: {r}")
        if people[l] + people[r] > limit: # 못 태움
            # print(f"{people[l]}만 탈 수 있음.")
            l += 1 # 왼쪽 사람만 태움
        else: # 둘 다 태움
            # print(f"{people[l]}, {people[r]} 모두 탈 수 있음.")
            l += 1
            r -= 1
        answer += 1
    # print(f"현재 왼쪽 인덱스: {l}, 오른쪽 인덱스: {r}")
    if l == r: # 다 안 탔을 때
        answer += 1
    return answer

'''
테스트 1 〉	통과 (1.99ms, 11.1MB)
테스트 2 〉	통과 (1.49ms, 10.8MB)
테스트 3 〉	통과 (1.33ms, 10.9MB)
테스트 4 〉	통과 (1.17ms, 11MB)
테스트 5 〉	통과 (0.73ms, 11MB)
테스트 6 〉	통과 (0.47ms, 10.8MB)
테스트 7 〉	통과 (0.69ms, 10.9MB)
테스트 8 〉	통과 (0.11ms, 10.7MB)
테스트 9 〉	통과 (0.14ms, 10.8MB)
테스트 10 〉	통과 (1.31ms, 11MB)
테스트 11 〉	통과 (1.06ms, 10.9MB)
테스트 12 〉	통과 (1.04ms, 10.9MB)
테스트 13 〉	통과 (1.36ms, 11MB)
테스트 14 〉	통과 (1.79ms, 11MB)
테스트 15 〉	통과 (0.20ms, 10.7MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	통과 (21.01ms, 41MB)
테스트 3 〉	통과 (32.82ms, 39MB)
테스트 4 〉	통과 (22.81ms, 43MB)
테스트 5 〉	통과 (18.83ms, 37.4MB)
'''
def solution(people, limit):
    answer = 0
    people.sort()  # 오름차순 정렬
    while people:
        temp = people.pop() # 가장 무거운 사람
        answer += 1
        for i in range(len(people)):
            if temp + people[i] > limit: # 어차피 못 태움
                break
            # print(f"태울 수 있습니다 : {temp} + {people[i]}")
            people.pop(i)
            break
        # temp = 0

    return answer

# 3) 시간이 더 늘어났는데?
def solution(people, limit):
    '''
    테스트 1 〉	통과 (2547.35ms, 11.1MB)
    테스트 2 〉	통과 (402.48ms, 10.9MB)
    테스트 3 〉	통과 (570.46ms, 11MB)
    테스트 4 〉	통과 (1021.86ms, 10.8MB)
    테스트 5 〉	통과 (231.44ms, 10.8MB)
    테스트 6 〉	통과 (35.49ms, 10.7MB)
    테스트 7 〉	통과 (125.77ms, 10.8MB)
    테스트 8 〉	통과 (0.91ms, 10.7MB)
    테스트 9 〉	통과 (2.97ms, 10.6MB)
    테스트 10 〉	통과 (562.31ms, 10.9MB)
    테스트 11 〉	통과 (332.26ms, 10.9MB)
    테스트 12 〉	통과 (252.89ms, 10.9MB)
    테스트 13 〉	통과 (404.94ms, 10.9MB)
    테스트 14 〉	통과 (526.25ms, 11MB)
    테스트 15 〉	통과 (4.91ms, 10.6MB)
    '''
    answer = 0
    people.sort()  # 오름차순 정렬
    i = 0
    boat = []  # 탑승한 사람
    while i < len(people):
        print(f"{i}번째 사람 검사")
        # 탄 사람이면 pass
        if i in boat:
            i += 1
            continue

        # 타지 않은 사람에 대해서
        if i < len(people) - 1 and people[i + 1] >= limit:  # 그 다음 사람들 어차피 무게 제한보다 크면
            return answer + (len(people) - i)
        else:
            boat.append(i)
            answer += 1
            for j in range(len(people) - 1, i, -1):
                if people[i] + people[j] <= limit and j not in boat:
                    print("       태울 수 있습니다.")
                    boat.append(j)
                    break
            i += 1
            print(f"현재까지 탑승한 사람: {boat}")
    return answer


# # 정확성 태스트 all pass, 효율성 테스트.
'''
통과 (206.37ms, 10.8MB)
테스트 2 〉	통과 (281.19ms, 10.9MB)
테스트 3 〉	통과 (110.14ms, 11MB)
테스트 4 〉	통과 (63.01ms, 10.9MB)
테스트 5 〉	통과 (26.66ms, 11MB)
테스트 6 〉	통과 (18.41ms, 10.8MB)
테스트 7 〉	통과 (37.81ms, 10.7MB)
테스트 8 〉	통과 (0.84ms, 10.8MB)
테스트 9 〉	통과 (1.07ms, 10.9MB)
테스트 10 〉	통과 (116.27ms, 11MB)
테스트 11 〉	통과 (52.21ms, 10.9MB)
테스트 12 〉	통과 (60.76ms, 10.9MB)
테스트 13 〉	통과 (135.26ms, 10.9MB)
테스트 14 〉	통과 (369.44ms, 10.9MB)
테스트 15 〉	통과 (3.23ms, 10.8MB)
'''
# def solution(people, limit):
#     answer = 0
#     people.sort()  # 오름차순 정렬
#     while people:
#         temp = people.pop(0)
#         answer += 1
#         print(f"현재 보트 수: {answer}, 무게: {temp}")
#         for i in range(len(people) - 1, -1, -1):
#             if temp + people[i] <= limit:
#                 print("       태울 수 있습니다.")
#                 temp += people.pop(i)
#                 print(f"현재 보트 수: {answer}, 무게: {temp}")
#                 break
#         # 태울 수 있는 사람이 없는 경우
#         temp = 0
#
#     return answer
#
# # 조건 1개 못 봄, 내림차순
# def solution(people, limit):
#     answer = 0
#     people.sort()
#     while people:
#         temp = people.pop()  # 현재 타고 있는 사람
#         # print(f"현재 타고 있는 사람: {temp}, 보트 개수: {answer}, 사람: {people}")
#         answer += 1
#         for i in range(len(people) - 1, -1, -1):
#             if temp + people[i] <= limit:
#                 people.pop(i)
#             else:
#                 break
#         # temp = 0
#         # while flag + people[-1] <= limit: # 더 태울 수 있을 때까지 태우기
#         #     flag += people.pop()
#         # print(people)
#         # flag = 0 # flag 초기화
#
#     return answer