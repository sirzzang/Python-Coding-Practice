# 반드시 원점 역할이 필요하고
# 원점 역할에 들어오는 애는 숫자가 4개여야 한다.
# 따라서 똑같은 숫자가 2개씩 있는 경우 -> 최솟값을 출력하면 되고
# ====> 이 방법은 오히려 너무 비효율적이지 않나?

# 아 그냥 앞에 수 2개, 뒤에 수 2개 나오면 된다.

# a, b = map(int, input().split())
# c, d = map(int, input().split())
# e, f = map(int, input().split())

# if a == c:
#     if b == d:
#         print(e, f)
#     elif b == f:
#         print(e, d)
#     else:
#         print(e, b)
# elif a == e:
#     if b == d:
#         print(c, f)
#     elif b == f:
#         print(c, d)
#     else:
#         print(c, b)
# else:
#     if b == d:
#         print(a, f)
#     elif b == f:
#         print(a, d)
#     else:
#         print(a, b)


# 이거 말고 내가 원래 생각했던 방식으로 하려면?

