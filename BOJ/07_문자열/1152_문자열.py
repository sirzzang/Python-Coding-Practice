import sys
s = sys.stdin

user_input = s.readline().lower()

myStr = user_input.strip()

myStr_new = myStr.split()
print(len(myStr_new))

