import sys

t = int(sys.stdin.readline())

for _ in range(t):

    com = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline()[1:-2].split(',')

    if n == 0: # 빈 배열이 들어올 때,
        if "D" in com: # 삭제할 수 없으므로 error.
            print("error")
        else:
            print("[]")
    
    else:

        arr = [int(i) for i in arr]
        
        rCount = 0

        try:
            for command in com:
                if command == "R":
                    rCount += 1
                else:
                    if rCount % 2 == 0: # 지금까지 명령 내 reverse 횟수가 짝수면,
                        arr.pop(0) # 앞을 pop.
                    elif rCount % 2 == 1: # 홀수면,
                        arr.pop() # 뒤를 pop.

        except IndexError:
            print("error")
        
        else:           
            if rCount % 2 == 1: # 명령 내 모든 reverse 횟수가 홀수번이면 반대로 출력
                print("[", end="")
                print(*arr[::-1], sep=",", end="") # 모든 원소 출력
                print("]")
            else:
                print("[", end="")
                print(*arr, sep=",", end="")
                print("]")