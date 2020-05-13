n = int(input())

for i in range(n):
    myList = input().split()
    nSum = 0
    for num in myList:
        nSum += int(num)
    print(f"#{i+1} {round(nSum/len(myList))}")
        