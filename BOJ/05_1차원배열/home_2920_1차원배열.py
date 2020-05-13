myList = [int(x) for x in input().split()]
if myList == sorted(myList):
    print("ascending")
elif myList == sorted(myList, reverse = True):
    print("descending")
else:
    print("mixed")