user_input = input().split()
myStr = [txt[::-1] for txt in user_input]
numList = [int(x) for x in myStr]
print(max(numList))