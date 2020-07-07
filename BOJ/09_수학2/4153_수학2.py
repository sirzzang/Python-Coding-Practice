a, b, c = map(int, input().split())

while True:
    if a == 0 and b == 0 and c == 0:
        break
    else:
        pytagList = sorted([a, b, c])
        if (pytagList[-1]) ** 2 == (pytagList[0])** 2 + (pytagList[1]) ** 2:
            print("right")
        else:
            print("wrong")

        a, b , c = map(int, input().split())