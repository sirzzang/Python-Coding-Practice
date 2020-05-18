# 테스트 12에서 실패.

number = input()
k = int(input())
stack = [number[0]]

for n in number[1:]:

    while stack and int(n) > int(stack[-1]) and k > 0:
        stack.pop()
        k -= 1
        print(f"삭제했습니다. 결과는 {stack}입니다. 이제 삭제할 수 있는 숫자의 개수는 {k}입니다.")

    stack.append(n)
    print(f"검사한 숫자 : {n}, 선택된 숫자들 : {stack}, 개수 : {len(stack)}")

    if len(stack) == len(number) - k:
        print("모두 다 선택했습니다. 종료합니다.")
        break

print(f"정답 : {''.join(stack)}")

# # 12개 중 2개 통과
# # 시간 초과도 있음...
#
# number = [int(x) for x in input()]
# k = int(input())
#
# answer = "" # 선택한 숫자 저장
# start = 0
# limit = k
# cnt = 0
#
# while limit < len(number):
#     print(f"start : {start}, limit : {limit}")
#
#     if limit == start + 1 : # 1개만 비교해야 할 경우 비교 대상 늘린다.
#         limit += 1
#
#     if k + cnt <= start: # 남은 모든 숫자를 선택해야 할 경우 break
#         print("모든 숫자를 다 선택해야 합니다.")
#         for n in number[start:]:
#             answer = answer + str(n)
#         break
#
#     selected = 0
#     check_lst = number[start:limit]
#     print(f"{check_lst}를 검사합니다.")
#
#     for i, n in enumerate(check_lst):
#         if n == max(check_lst):
#             answer = answer + str(n)
#             selected += 1
#             temp = i+1
#
#     start += temp
#     limit += selected
#     cnt += selected
#     print(f"총 선택된 숫자의 개수는 {cnt}입니다.")
#
# print(answer)



# # numbers 순회하도록 하면, 똑같은 숫자가 뒤에 있을 때..
#
# while limit < len(number):
#     print(f"시작 인덱스 {start}, 끝 인덱스 {limit}")
#
#     if limit + 1 == len(number): # 남은 모든 숫자를 선택해야 할 경우 break
#         print("모든 숫자를 다 선택해야 합니다.")
#         for n in number[start:]:
#             answer = answer + str(n)
#         break
#
#     if limit - start == 1: # 1개만 비교해야 할 경우 비교 대상 늘린다.
#         limit += 1
#
#     check_lst = number[start:limit]
#     selected = 0 # 선택한 숫자 개수 체크할 때마다 다르게 한다.
#     print(f"{check_lst}를 검사합니다.")
#
#     for i, n in enumerate(number): # number 전체에서 돌게 하여 인덱스 유지 : 마지막에 문제가 된다.
#         if n == max(check_lst):
#             answer = answer + str(n)
#             selected += 1
#             start = i+1
#             print(f"start : {start}")
#
#     print(f"이번 순회에서 {selected}개를 선택했습니다.", answer)
#     limit += selected
#
# print(answer)


# 이렇게 코드 짜면, 기존의 idx가 유지가 안 된다. number 슬라이싱하는 순간 인덱스가 0으로 바뀌니까.
