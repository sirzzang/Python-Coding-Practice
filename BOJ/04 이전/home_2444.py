# 문제 분석
# 1
# 2
# 3
# 4
# 5
# 4
# 3
# 2
# 1
# 이런 식이니까

# 1. 123454321 구현하고
# 2. 그걸 한 줄씩 내려서 출력하는데
# 3. 별로만 출력하면 되지 않을까
# 4. n = 5일 때 생각해보면

# for문 2개 사용

# n = int(input())

# for i in range(1, 2*n, 2):
#     print((("*"*i).center(2*n-1)).rstrip())
# for i in range(2*(n-1)-1, 0, -2):
#     print((("*"*i).center(2*n-1)).rstrip())

# for문 1개 사용?

n = int(input())
for i in range(1, 2*n):
    if i <= n:
        print((("*"*(2*i-1)).center(2*n)).rstrip())
    else:
        print((("*"*(2*(2*n-i)-1)).center(2*n)).rstrip())
