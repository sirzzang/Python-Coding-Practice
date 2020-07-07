numList = list(range(1, 1000000+1))

bunhaehapList = []
for i in range(1, 1000000+1):
    for j in str(i):	# j는 i라는 숫자의 자릿수
        i += int(j)		# i에 j를 합해 나간다.
    bunhaehapList.append(i)	# i는 분해합이 되고, 그 분해합을 bunhaehapList에 넣는다.

n = int(input())
if n in bunhaehapList:
    print(numList[bunhaehapList.index(n)])
else:
    print(0)

# numList = list(range(1,1000000+1))

# strList = []
# for i in range(1, 1000000+1):
#     for j in str(i):
#         i += int(j)
#     strList.append(i)

# n = int(input())
# if n in strList:
#     print(numList[strList.index(n)])
# else:
#     print(0)
    

# print([i + int(j) for i in range(1, 100+1) for j in str(i)])


# strList = [str(num) for num in numList]
# print(strList)
