# A*B = L*G
a, b = map(int, input().split())
ab = a*b
if b > a: # 작은 순서로 정렬
    a, b = b, a
while a > 0: # 유클리드 알고리즘
    a, b = b%a, a

print(f"최대공약수: {b}, 최소공배수: {ab//b}")