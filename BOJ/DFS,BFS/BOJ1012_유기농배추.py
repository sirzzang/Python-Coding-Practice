'''
to be continued...
'''

columns, rows, cabbage = map(int, input().split())

# 전체 배추밭 만들기
field = [[0 for column in range(columns)] for row in range(rows)]
print(field)

# 벌레 먹은 배추 위치
for _ in range(cabbage):
    c, r = map(int, input().split())
    field[r][c] = 1
print(field)
