def reverse(arr):
    return arr[::-1]

def delete(arr):
    if len(arr) == 0:
        return "error"
    else:
        arr.pop(0)
        return arr

import sys

t = int(sys.stdin.readline())

for _ in range(t):

    try:

        user_command = sys.stdin.readline().strip("\n")
        n = sys.stdin.readline()

        user_arr = list(map(int, sys.stdin.readline().strip('\n')[1:-1].split(',')))

        for command in user_command:
            if command == "R":
                user_arr = reverse(user_arr)
            else:
                user_arr = delete(user_arr)
        
        print(user_arr)
    
    except:
        
        print("error")

# user_arr = list(map(int, sys.stdin))

# user_arr = list(map(int, sys.stdin.readline().strip('\n')[1:-1].split(',')))
# print(user_arr)