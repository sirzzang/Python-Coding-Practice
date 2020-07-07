user_input = input().split()
print(user_input)
numCount = [user_input.count(str(i)) for i in range(1,4)]
print(numCount)
price = [500, 800, 1000]
expenditure = sum([a*b for a,b in zip(numCount,price)])
print(expenditure)
print(5000 - expenditure)