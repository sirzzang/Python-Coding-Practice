import sys
s = sys.stdin
myStr = s.readline().upper()

char_list = []
char_set = set()

for i in range(len(myStr)):
    char_list.append(myStr[i])
    char_set.add(myStr[i])

check_char_list = list(char_set)

numList = [char_list.count(check_char_list[i]) for i in range(len(check_char_list))]
checkNum = max([char_list.count(check_char_list[i]) for i in range(len(check_char_list))])

indexNumList = [index for index, value in enumerate(numList) if value == checkNum]

if len(indexNumList) != 1:
    print("?")
else:
    print(check_char_list[indexNumList[0]])