name = input()

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
loc = 0
cnt = 0
for char in name:
    idx = alphabets.index(char)
    print(f"입력해야 할 문자 : {char}, 위치 : {idx}")
