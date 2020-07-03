# 1번 풀이: 효율성 X
# import random
#
# # for _ in range(10):
# #     n = random.randint(1, 10)
# #     works = [random.randint(1, 10) for _ in range(n)]
# #     print(f"n: {n}, works: {works}")
#
# works = list(map(int, input().split()))
# n = int(input())
# answer = 0
# if n >= sum(works):
#     print(answer)
# else:
#     while n > 0:
#         works.sort(reverse=True)
#         print(works)
#         works[0] -= 1
#         n -= 1
#         if all(int(sum(works) / len(works)) == work for work in works) and n == 0:
#             break
#         print(n)
#     print(f"최종: {works}")
#
#     for work in works:
#         answer += work*work
#
#     print(answer)

# 2번 풀이: 효율성 X
# def solution(n, works):
#     answer = 0
#     if n >= sum(works):
#         return answer
#     else:
#         while n > 0:
#             works.sort()
#
#             if works[-1] == works[-2]: # 똑같으면
#                 print(f"수행 전: {works}, 남은 시간: {n}")
#                 n -= 1
#                 works[-1] -= 1
#                 print(f"수행 후: {works}, 남은 시간: {n}")
#             else:
#                 if works[-1] - works[-2] + 1 <= n: # 빼줄 수 있으면
#                     print(f"수행 전: {works}, 남은 시간: {n}")
#                     n -= (works[-1] - works[-2] + 1) # 위에서 먼저 안 빼주면 works 이미 바뀌어 있다;;
#                     works[-1] -= (works[-1] - works[-2] + 1)
#                     print(f"수행 후: {works}, 남은 시간: {n}")
#                 else:
#                     print(f"수행 전: {works}, 남은 시간: {n}")
#                     works[-1] -= n
#                     print(f"수행 전: {works}, 남은 시간: {n}")
#                     break
#
#         for work in works:
#             answer += work * work
#
#         return f"            정답: {answer}"


# def solution(n, works):
#     answer = 0
#     if n >= sum(works):
#         return answer
#     else:
#         works.sort(reverse = True) # 한 번만 정렬하자 처음에.
#         i = 0 # 인덱스
#         try:
#             while n > 0:
#                 if works[i] == works[i+1]:
#                     i += 1
#                 elif (works[i] - works[i+1]) * (i+1) <= n:
#                     n -= (works[i] - works[i+1]) * (i+1)
#                     for j in range(i+1):
#                         works[j] -= (works[i] - works[i+1])
#                     i += 1
#                 else:
#                     for j in range(i+1):
#                         works[j] -= 1
#                         n -= 1
#                         if n == 0:
#                             break
#         except IndexError:
#             q, r = n // len(works), n % len(works)
#             if q > 0 :
#                 for i in range(len(works)):
#                     works[i] -= q
#                 n -= q * len(works)
#
#             while n > 0:
#                 for i in range(len(works)):
#                     works[i] -= 1
#                     n -= 1
#                     if n == 0:
#                         break
#
#         for work in works:
#             answer += work * work
#
#         return answer



# 맞은 풀이
def solution(n, works):
    answer = 0
    if n >= sum(works):
        return answer
    else:
        works.sort(reverse = True) # 한 번만 정렬하자 처음에.
        i = 0 # 인덱스
        try:
            while n > 0:
                if works[i] == works[i+1]:
                    i += 1
                elif (works[i] - works[i+1]) * (i+1) <= n:
                    n -= (works[i] - works[i+1]) * (i+1)
                    for j in range(i+1):
                        works[j] -= (works[i] - works[i+1])
                    i += 1
                else:
                    for j in range(i+1):
                        works[j] -= 1
                        n -= 1
                        if n == 0:
                            break
        except IndexError:
            q, r = n // len(works), n % len(works)
            if q > 0 :
                for i in range(len(works)):
                    works[i] -= q
                n -= q * len(works)

            while n > 0:
                for i in range(len(works)):
                    works[i] -= 1
                    n -= 1
                    if n == 0:
                        break

        for work in works:
            answer += work * work

        return answer

print(solution(9, [10, 6, 10, 7, 9, 1, 5, 4, 7])) # 310
print(solution(4, [5, 5, 10, 9])) # 163
print(solution(7, [7, 1, 6, 2, 10, 3, 7])) # 147
print(solution(5, [10, 2, 10, 5, 9])) # 221
print(solution(6, [7, 7, 10, 9, 2, 2])) # 191
print(solution(2, [1, 5])) # 10
print(solution(9, [10, 6, 10, 7, 9, 1, 5, 4, 7])) # 310
print(solution(6, [1, 3, 1, 9, 9, 7])) # 132
print(solution(5, [4, 4, 6, 4, 6])) # 73: 4 4 4 4 3 64+
print(solution(5, [6, 6, 2, 5, 5])) # 77
print(solution(5, [8, 6, 2, 10, 7])) # 174
print(solution(4, [4, 3, 3])) # 12


