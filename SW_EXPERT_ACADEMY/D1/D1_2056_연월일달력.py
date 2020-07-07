n = int(input())

for i in range(n):

    calendar = input()
    year = calendar[:4]
    month = calendar[4:6]
    day = calendar[6:]

    if 1 <= int(month) <= 12:
        if int(month) == 2:
            if 1 <= int(day) <= 28:
                print(f"#{i+1} {year}/{month}/{day}")
            else:
                print(f"#{i+1} -1")
        elif int(month) in [1,3,5,7,8,10,12]:
            if 1 <= int(day) <= 31:
                print(f"#{i+1} {year}/{month}/{day}")
            else:
                print(f"#{i+1} -1")
        else:
            if 1 <= int(day) <= 30:
                print(f"#{i+1} {year}/{month}/{day}")
            else:
                print(f"#{i+1} -1")
    else:
        print(f"#{i+1} -1")

#1. 오답 : -1 출력형식....
# 채점용 input 파일로 채점한 결과 fail 입니다.
# (오답 : 5개의 테스트케이스 중 3개가 맞았습니다.)

n = int(input())

for i in range(n):

    calendar = input()
    year = calendar[:4]
    month = calendar[4:6]
    day = calendar[6:]

    if 1 <= int(month) <= 12:
        if int(month) == 2:
            if 1 <= int(day) <= 28:
                print(f"#{i+1} {year}/{month}/{day}")
            else:
                print(-1)
        elif int(month) in [1,3,5,7,8,10,12]:
            if 1 <= int(day) <= 31:
                print(f"#{i+1} {year}/{month}/{day}")
            else:
                print(-1)
        else:
            if 1 <= int(day) <= 30:
                print(f"#{i+1} {year}/{month}/{day}")
            else:
                print(-1)
    else:
        print(-1)