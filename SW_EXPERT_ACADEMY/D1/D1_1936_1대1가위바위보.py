# 이걸 진짜 경우 다 나눠서 하는 방법 뿐인가?
a, b = map(int, input().split())

if a == 1:
    if b == 1:
        print("B")
    else:
        print("A")
elif a == 2:
    if b == 1:
        print("A")
    else:
        print("B")
elif a == 3:
    if b == 1:
        print("B")
    else:
        print("A")