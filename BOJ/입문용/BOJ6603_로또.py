k = int(input()) # 주어지는 수의 개수
S = [int(input()) for _ in range(k)] # 수의 순서
# 012345
# 012346
# 012356
for i in range(len(S)):
    start = 0
    end = 6
    print()