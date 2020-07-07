# Q_01

# 하노이 탑(Tower of Hanoi)은 퍼즐의 일종입니다. 
# 세 개의 기둥과 이 기동에 꽂을 수 있는 크기가 다양한 원판들이 있고, 퍼즐을 시작하기 전에는 한 기둥에 원판들이 작은 것이 위에 있도록 순서대로 쌓여 있습니다. 
# 게임의 목적은 다음 두 가지 조건을 만족시키면서, 한 기둥에 꽂힌 원판들을 그 순서 그대로 다른 기둥으로 옮겨서 다시 쌓는 것입니다.

# 한 번에 하나의 원판만 옮길 수 있습니다.
# 큰 원판이 작은 원판 위에 있어서는 안됩니다.

# 하노이 탑의 세 개의 기둥을 왼쪽 부터 1번, 2번, 3번이라고 하겠습니다. 1번에는 n개의 원판이 있고 이 n개의 원판을 3번 원판으로 최소 횟수로 옮기려고 합니다.
# 1번 기둥에 있는 원판의 개수 n이 매개변수로 주어질 때, n개의 원판을 3번 원판으로 최소로 옮기는 방법을 return하는 solution를 완성해주세요.

# 제한사항
# n은 15 이하의 자연수 입니다.

# answer = []
#
# def Hanoi(n, start, end, mid):
#     global answer
#     if n == 1:
#         answer.append([start, end])
#         return
#     else:
#         Hanoi(n-1, start, mid, end)
#         answer.append([start, end])
#         Hanoi(n-1, mid, end, start)
#
# def solution(n):
#     Hanoi(n, 1, 3, 2)
#     return answer


# Q_02. 기지국

# Q_03. N, 사칙연산

# x테스트 5만 실패

from itertools import product

def ops(a, b):
    return set(item for item in [a+b, a-b, a*b, a//b] if item > 0)

def check(container, n, number, order):

    # result 내에서 다른 애들과
    for x, y in product(container, repeat=2):
        if number in ops(x, y):
            return order*2

    # result와 N들과의 애들에서
    for c in container:
        if number in ops(n, c) or number in ops(c, n):
            return order

    return False


def solution(N, number):

    if number in [int(str(N)*i) for i in range(1, 8)]:
        return len(str(number))

    else:
        if number % (11*N) == 0:
            return len(str(number))

        counts = set()
        result_set = {N}

        for i in range(7):
            print(f"{N}을 {i+2}번 사용합니다.")
            print(f"현재 result set : {result_set}")

            temp_set = set()

            if check(result_set, N, number):
                print("위에서 일치하는 결과를 발견했습니다.")
                counts.add(i+2)

            else:
                for result in result_set:
                    temp_set.update(ops(N, result))
                    temp_set.update(ops(result, N))
                for x, y in product(result_set, repeat=2):
                    temp_set.update(ops(x, y))

            print(temp_set)

            for t in temp_set:
                for j in range(6-i):
                    # print(int(str(N) * (j + 1)))
                    if number in ops(int(str(N) * (j + 1)), t) or number in ops(t, int(str(N) * (j + 1))):
                        print(ops(int(str(N) * (j + 1)), t), ops(int(str(N) * (j + 1)), t))
                        print("아래서 일치하는 결과를 발견했습니다.")
                        counts.add(i+j+3)


            temp_set.add(int(str(N) * (i+2)))
            print(temp_set)

            result_set = temp_set # 업데이트

        if counts:
            return min(counts)
        else:
            return -1





N = int(input())
number = int(input())
print(solution(N, number))



#  = int(input())
#         number = int(input())
#
#         print(ops(N, N))
#
#
#
#
#         #
#         # else:
#         #     print(-1)
#         #
#         #
#         # # print("이어붙이기 결과")
#         #
#         # temp_set.add(11*N)
#         # #     print(result, [ops[op](result, N) for op in ops])
#         # #     temp.extend([ops[op](result, N) for op in ops])
#         # #
#         # # print(temp)
#         # result_set = temp_set
#         # print(result_set)
#
#
#
# #
# print(int('1111'))