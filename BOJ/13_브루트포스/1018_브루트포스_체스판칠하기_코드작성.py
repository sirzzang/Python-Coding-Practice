# 반례 : 답 29인데 나는 35로 나온다.
# 8 8
# BBBBWBBW
# WWWWBBWB
# WWBBWBWW
# WBWWBWBW
# WBBWBBWB
# BWBWBWWB
# BWWWWWBW
# BWBBBBWW

# 첫 줄을 아예 W로 바꿔서 칠하는 게 나을 수도 있지 않나?


n, m = map(int, input().split())

chess = []
for _ in range(n):
    chess.append(input())

# 체스판 그릴 수 있는 경우의 수를 만들기 위한 작업
# 체스판 8개씩 왼쪽 ~ 오른쪽 이동시켜가면서 좌우가 다 되면
# 아래로 내린다.

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

# 만든 체스판에 대해 색칠하는 경우의 수
# B로 시작하거나 W로 시작하거나 굳이 고정시킬 필요 없다.
# BWBWBW~로 칠하든 WBWBWB~로 칠하든, 시작이 어찌되었든 최소 개수를 뽑아내면 된다.
# 처음에 틀렸던 이유?
# 반드시 경우를 B로 시작할 때와 W로 시작할 때를 나눴기 때문.

numList = []

for i in range(0, len(chessList), 8):
    nCount = 0

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
    numList.append(nCount)

for i in range(0, len(chessList), 8):
    nCount = 0

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