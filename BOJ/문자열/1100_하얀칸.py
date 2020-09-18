from itertools import chain

chess = [list(input()) for _ in range(8)]
print(chess)

for row in range(8):
    if row % 2 == 0: # 홀수번째 줄이면
        chess[row][1] = '.'
        chess[row][3] = '.'
        chess[row][5] = '.'
        chess[row][7] = '.'
    else:
        chess[row][0] = '.'
        chess[row][2] = '.'
        chess[row][4] = '.'
        chess[row][6] = '.'

print(list(chain(*chess)).count('F'))
