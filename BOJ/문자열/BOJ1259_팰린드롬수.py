def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False

while True:
    myStr = input()
    if myStr == '0':
        break
    if is_palindrome(myStr):
        print('yes')
    else:
        print('no')