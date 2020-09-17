import sys
s = sys.stdin

user_input = s.readlines()

numStr = user_input[-1].strip('\n')

numSum = 0
for i in range(len(numStr)):
    num = int(numStr[i])
    numSum += num
print(numSum)