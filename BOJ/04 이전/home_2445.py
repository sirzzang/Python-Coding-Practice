# 절댓값으로 찍어도 된다

n = int(input())
for i in range(-n+1, n):
    print(("*"*(n-abs(i))+" "*(2*abs(i))+"*"*(n-abs(i))).rstrip())



# for문 사용해서 원래 제출한 방법

# n = int(input())
# for i in range(1, 2*n):
#     if i <= n :
#         print(("*"*i+" "*(2*n-2*i)+"*"*i).rstrip())
#     else:
#         print(("*"*(2*n-i)+" "*(2*i-2*n)+"*"*(2*n-i)).rstrip())
