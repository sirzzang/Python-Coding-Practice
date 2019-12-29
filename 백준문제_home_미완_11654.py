# 아스키코드 숫자일 때, 문자일 때 다름
# 먼저 input값이 숫자인지/문자인지 구분

# 이렇게 작성하니까 0일 때 48 출력 안 됨. 9도 안 됨.
# user_input = input()

# try:
#    val = int(user_input)
#    print(chr(val))
# except ValueError:
#    print(ord(user_input))

# 0?

user_input = input()

try:
   val = int(user_input)
   print(chr(val))
except ValueError:
    print(ord(user_input))