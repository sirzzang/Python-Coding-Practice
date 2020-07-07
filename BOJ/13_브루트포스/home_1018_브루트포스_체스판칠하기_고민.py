# 일단 먼저 고르는 것을 해야 한다.

n, m = map(int, input().split())

# 체스판! : n행(index : 0~n-1), m열(index : 0~m-1)

chess = []
for _ in range(n):
    chess.append(input())
print(chess)

# 이렇게 하면 고를 수 있는 좌표들이 나온다. -> i를 세로로, j를 가로로 해서 자르면 된다.
# 와 드디어!!!!!!!!!!!! 잘랐다

i = 0
j = 0
chessList = []
while i+8 <= n:
    while j+8 <= m:
        k = i
        for k in range(i, i+8):
            chessList.append(chess[k][j:j+8])
        j += 1
    j = 0
    i += 1
print(chessList)
# print("".join(chessList))
# print(len(chessList))

# 자른 걸 64개씩 다시 자르기
# len(chessList) / 8 = 체스판 개수
# chessList에 있는 걸 문자열로 이어붙이고, 그걸 64개씩 자르기
# print(type("".join(chessList)))

# 혹은?
# chessList에 있는 애들을 8개씩 자르기 -> 그게 한 체스판이다
# 시작이 B면 홀수번째 체스판은 BWBWBWBW여야 하고, 짝수번째 체스판은 WBWBWBWB여야 한다.
# 시작이 W면 홀수번째 체스판은 WBWBWBWB여야 하고, 짝수번째 체스판은 BWBWBWBW여야 한다.

# chessChunk = [chessList[i:i+8] for i in range(0, len(chessList), 8)]
# print(chessChunk)
# print(len(chessChunk)) # 체스판 가능한 개수

numList = []

for i in range(0, len(chessList), 8):
    nCount = 0
    print(chessList[i:i+8])
    if chessList[i:i+8][0][0] == "B":
        for j in range(len(chessList[i:i+8])):
            if j % 2 == 0:
                for k in range(len(chessList[i:i+8][j])):
                    if k % 2 == 0 and chessList[i:i+8][j][k] != "B":
                        nCount += 1
                    elif k  % 2 == 1 and chessList [i:i+8][j][k] != "W":
                        nCount += 1     
            else:
                for k in range(len(chessList[i:i+8][j])):
                    if k % 2 == 0 and chessList[i:i+8][j][k] != "W":
                        nCount += 1
                    elif k  % 2 == 1 and chessList [i:i+8][j][k] != "B":
                        nCount += 1    
    else:
        for j in range(len(chessList[i:i+8])):
            if j % 2 == 0:
                for k in range(len(chessList[i:i+8][j])):
                    if k % 2 == 0 and chessList[i:i+8][j][k] != "W":
                        nCount += 1
                    elif k  % 2 == 1 and chessList [i:i+8][j][k] != "B":
                        nCount += 1        
            else:
                for k in range(len(chessList[i:i+8][j])):
                    if k % 2 == 0 and chessList[i:i+8][j][k] != "B":
                        nCount += 1
                    elif k  % 2 == 1 and chessList [i:i+8][j][k] != "W":
                        nCount += 1
    numList.append(nCount)

print(min(numList))

# # i = 0
# # j = 0
# # while i+8 <= n:
# #     while j+8 <= m:
# #         print(range(i+1, i+8), range(j+1, j+8))
# #         for i in range(i+1, i+8):
# #             print(chess[i][j+1:j+8])
# #         j += 1
# #     j = 0
# #     i += 1



# i = 0
# j = 0
# while i+8 <= n:
#     while j+8 <= m:
#         print(range(i, i+8), range(j, j+8))
#         j += 1
#     j = 0
#     i += 1

# print(chess[0][0:8],chess[1][0:8],chess[2][0:8],chess[3][0:8],chess[4][0:8],chess[5][0:8],chess[6][0:8],chess[7][0:8]) # 첫 번째 조각
# print(chess[0][1:9],chess[1][1:9],chess[2][1:9],chess[3][1:9],chess[4][1:9],chess[5][1:9],chess[6][1:9],chess[7][1:9]) # 두 번째 조각
# # print(chess[0][2:10], ~ chess[7][2:10])

# # 마지막은 exclusive
# # range(0,8), range(0, 9)~range(5, 12)
# # range(1,9), range(0, 9)~range(5, 12)
# # range(2, 10), range(0, 9)~range(5, 12)

# # i가 0으로 안 간다!!! -> list index out of range

# # i = 0
# # j = 0

# # while i+8 <= n:
# #     while j+8 <= m:
# #         for i in range(i, i+8):
# #             print(chess[i][j:j+8])
# #         j += 1
# #     j = 0
# #     i += 1

# # i = 0
# # j = 0
# # # i  7일 때까지는 괜찮은데, j = 1로 돌고 난 후에 i = 0으로 안 간다. .

# # while j+8 <= m:
# #     while i+8 <= n:
# #         for i in range(i, i+8):
# #             print(chess[i][j:j+8])
# #         j += 1
# # i += 1
    
# # chessList = []
# # while j+8 <= m:
# #     while i+8 <= n:
# #         for i in range(i, i+8):
# #             print(chess[i][j:j+8])
# #         j += 1
# #     j = 0
# #     i += 1

# # while i+8 <= n:
# #     while j+8 <= m:
# #         for i in range(i, i+8):
# #             print(chess[i][j:j+8])
# #         j += 1
# #         i = 0
# #     j = 0
# #     i += 1

# print(chess[0][0:8],chess[1][0:8],chess[2][0:8],chess[3][0:8],chess[4][0:8],chess[5][0:8],chess[6][0:8],chess[7][0:8]) # 첫 번째 조각
# print(chess[0][1:9],chess[1][1:9],chess[2][1:9],chess[3][1:9],chess[4][1:9],chess[5][1:9],chess[6][1:9],chess[7][1:9]) # 두 번째 조각
# # print(chess[0][2:10], ~ chess[7][2:10])
# # print(chess[0][3:11], ~ chess[7][3:11])
# # print(chess[0][4:12], ~ chess[7][4:12])



# # 체스판 고르기?

# # 망한 방법 1
# # 실행 결과
# # ['BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB']
# # ['BBBBBBBBBWBWB', 'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB']
# # ['BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB']
# # ['BBBBBBBBBWBWB', 'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB']
# # ['BBBBBBBBWBWBW', 'BBBBBBBBBWBWB']
# # ['BBBBBBBBBWBWB']
# # ['BBBBBBBBBWBWB', 'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'WWWWWWWWWWBWB']
# # ['BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'WWWWWWWWWWBWB']
# # ['BBBBBBBBBWBWB', 'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'WWWWWWWWWWBWB']
# # ['BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'WWWWWWWWWWBWB']
# # ['BBBBBBBBBWBWB', 'WWWWWWWWWWBWB']
# # ['WWWWWWWWWWBWB']
# # ['BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'WWWWWWWWWWBWB', 'WWWWWWWWWWBWB']
# # ['BBBBBBBBBWBWB', 'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'WWWWWWWWWWBWB', 'WWWWWWWWWWBWB']
# # ['BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'WWWWWWWWWWBWB', 'WWWWWWWWWWBWB']
# # ['BBBBBBBBBWBWB', 'WWWWWWWWWWBWB', 'WWWWWWWWWWBWB']
# # ['WWWWWWWWWWBWB', 'WWWWWWWWWWBWB']
# # ['WWWWWWWWWWBWB']

# # i = 0
# # j = 0
# # while i+8 <= n:
# #     while j+8 <= m:
# #         print(chess[i+1: i+8][j+1: j+8])
# #         j += 1
# #     j = 0
# #     i += 1