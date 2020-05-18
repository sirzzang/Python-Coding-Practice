# 124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.
# 124 나라에는 자연수만 존재합니다. 124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
# 자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return하세요.

# 제한사항
# n은 500,000,000이하의 자연수 입니다.

num = int(input())

ans = ""
while num > 0:
    print(f"현재 숫자는 {num}")
    q, r  = divmod(num, 3)
    if r == 0:
        q -= 1
        r = 4
    print(f"몫과 나머지는 {q}, {r}")
    print(f"124 나라의 숫자는 {ans}")
    ans = str(r) + ans
    if q == 0:
        break
    print(f"바뀐 124나라의 숫자는 {ans}")
    num = q
    print(f"바뀐 숫자는 {num}")

print(num, ans)