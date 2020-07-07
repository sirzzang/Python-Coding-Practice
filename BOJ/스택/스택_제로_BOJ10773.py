# 궁금증
# Q1) 처음에 지울 숫자가 없으면 어떡하나?
# 조건 : 정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.

# 2. class 사용 구현

# class 내에 sum 구하는 함수까지 구현해야 함.
# 정답 : 30088 KB 120 ms 

class AccountBook:
    def __init__(self):
        self.money = []
    
    def push_money(self, item):
        return self.money.append(item)
    
    def pop_money(self):
        return self.money.pop()
    
    def sum_money(self):
        return sum(self.money)

import sys

n = int(sys.stdin.readline())

jamin_money = AccountBook()

for _ in range(n):

    jamin_num = int(sys.stdin.readline())

    if jamin_num == 0:
        jamin_money.pop_money()

    else:
        jamin_money.push_money(jamin_num)
    
print(jamin_money.sum_money())

# print(jamin_money.sum_money)

# 오류 : TypeError: 'AccountBook' object is not iterable
# 아래처럼 구현하면, jamin_money가 list가 아니라, <__main__.AccountBook object at 0x0099A148>이기 때문.

# class AccountBook:
#     def __init__(self):
#         self.money = []
    
#     def push_money(self, item):
#         return self.money.append(item)
    
#     def pop_money(self):
#         return self.money.pop()

# import sys

# n = int(sys.stdin.readline())

# jamin_money = AccountBook()

# for _ in range(n):

#     jamin_num = int(sys.stdin.readline())

#     if jamin_num == 0:
#         jamin_money.pop_money()

#     else:
#         jamin_money.push_money(jamin_num)

# print(jamin_money)




# 1. if ~ else, list 사용 구현
# 정답 : 30088 KB 112 ms 

# import sys

# n = int(sys.stdin.readline())

# account_book = []

# for _ in range(n):
    
#     jamin_num = int(sys.stdin.readline())

#     if jamin_num == 0:
#         account_book.pop()
#     else:
#         account_book.append(jamin_num)

# print(sum(account_book))
