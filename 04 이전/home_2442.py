n = int(input())
for i in range(1, 2*n, 2):
    print((("*"*i).center(2*n)).rstrip())

# 출력 형식이 잘못되었다고 나옴. -> 뒷공백때문에
n = int(input())
for i in range(1, 2*n, 2):
    print((("*"*i).center(2*n)))