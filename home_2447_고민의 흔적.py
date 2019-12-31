# # 분할
star = ["***","* *", "***"]
print(star)




# def stars(n):
#     matrix=[]
#     for i in range(3 * len(n)):
#         if i // len(n) == 1:
#             matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
#         else:
#             matrix.append(n[i % len(n)] * 3)
#     return(list(matrix))

# star = ["***","* *","***"]
# n = int(input())
# k = 0
# while n != 3:
#     n = int(n / 3)
#     k += 1
    
# for i in range(k):
#     star = stars(star)
# for i in star:
#     print(i)




# 기본 단위 9칸인데, 그 9칸 중 가운데가 뻥 뚫려 있다.

# def star(n):
#     if n == 3:
#         return 1
#     else:
#         return star(n//3)

# star(81)

    
# def hello(n):
#     if n == 3:
#         return
#     print(n//3, n)
#     n = n//3
#     hello(n)

# hello(81)

# (2,2) 뚫어

# class point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# p1 = point2D(x = 30, y = 30)
# p2 = point2D(x = )