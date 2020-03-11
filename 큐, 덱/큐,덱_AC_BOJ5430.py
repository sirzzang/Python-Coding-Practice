def reverse(arr):
    return arr[::-1]

def delete(arr):
    if len(arr) == 0:
        return "error"
    else:
        return arr[1:]

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    
    user_command = sys.stdin.readline().strip("\n")
    n = sys.stdin.readline()

    while True:
        try:
            user_arr = [int(i) for i in sys.stdin.readline().strip('\n').strip('[]').split(",")]
            break
        except ValueError:
            user_arr=[]
            break

    for command in user_command:
        if command == "R":
            user_arr = reverse(user_arr)
        else:
            user_arr = delete(user_arr)
        
    print(user_arr)