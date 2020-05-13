# 출력 초과

import sys

n = sys.stdin.readline().rstrip()

if '0' not in n or int(n) % 3 != 0:
    print(-1)
else:
    n = sorted(n, key = lambda x: -int(x))
    for num in n:
        print(num, end="")





# 이 문제는 출력이 너무 크기 때문에

# -1 을 출력해야할 때, 10^5에 해당하는 문자들을 모두 출력하면 출력 초과가 발생할 수도 있습니다.



# 무엇보다 참고로 이 문제는 주어진 숫자를 모두 사용해야합니다.