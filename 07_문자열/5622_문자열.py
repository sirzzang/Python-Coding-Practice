import sys
s = sys.stdin

dial = "ABC,DEF,GHI,JKL,MNO,PQRS,TUV,WXYZ"
button = dial.split(",")

user_input = s.readline().strip("\n")
phonenumber = [user_input[i] for i in range(len(user_input))]

dialtime = 0

for i in range(len(phonenumber)):
    for j in range(len(button)):
        if phonenumber[i] in button[j]:
            dialtime += (j + 3)

print(dialtime)


# button : ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# phonenumber : ['U', 'N', 'U', 'C', 'I', 'C']
