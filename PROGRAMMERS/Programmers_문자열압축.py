# 테스트 케이스 : 5번 안 됨. 한 글자 넣을 때 예외 처리 필요하다.

from itertools import groupby

myStr = input()

answer = len(myStr)
if len(set(myStr)) == 1:
    if len(myStr) == 1: # 한 글자 예외 처리 필요함.
        answer = 1
    else:
        answer = 1+len(str(answer))
else:
    for n in range(1, len(myStr)//2+1):
        chunks = [myStr[j:j + n] for j in range(0, len(myStr), n)] # 일단 자르고.
        cnt_chunks = [(label, sum(1 for _ in group)) for label, group in groupby(chunks)]
        cnt = 0
        if all(cnt_chunk[1]==1 for cnt_chunk in cnt_chunks):
            continue
        else:
            for cnt_chunk in cnt_chunks:
                if cnt_chunk[1] == 1:
                    cnt += len(cnt_chunk[0])
                else:
                    cnt += (len(cnt_chunk[0]) + len(str(cnt_chunk[1])))
            if cnt < answer:
                answer = cnt
print(answer)

# 문제 조건: 처음부터 자르는 거다.
# for n in range(1, len(myStr)//2 + 1):
#     for i in range(n):
#         chunks = [myStr[j:j+n] for j in range(i, len(myStr), n)]
#         print(f"끊은 개수: {n}, 시작점:{i}, {chunks}")
#         repeated = 0
#         for j in range(len(chunks)-1):
#             cnt = 1
#             if chunks[j] == chunks[j+1]:
#                 cnt += 1
#                 # print(chunks[j], cnt) # 중복이 있을 때만 선택해주면 되지 않을까?
#                 repeated += (n+len(str(cnt)))
#         print(f"{chunks} : {repeated}")
#
#         if repeated == 0:
#             continue
#
#         if answer > i + repeated:
#             answer = i + repeated

# # 아래처럼 짜면 돌아가면서 압축하는 게 아님.
# for n in range(1, len(myStr)//2+1):
#     chunks = [myStr[i:i + n] for i in range(0, len(myStr), n)]
#     print(n, chunks)
#     for j in range(len(chunks)-1):
#         cnt = 0
#         if chunks[j] == chunks[j+1]:
#             cnt += 1
#             print(cnt, chunks[j])

# 오류 체크
# 1. ValueError: range() arg 3 must not be zero