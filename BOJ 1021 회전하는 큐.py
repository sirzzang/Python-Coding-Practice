def shift(lst, shft=0):
    ln = len(lst)
    for i, ele in enumerate(lst[:]):
        lst[(i + shft) % ln] = ele
    return lst

myList = list(range(1, 11))
# print(shift(myList, -1))

print(myList.index(1))



# n = int(input())
# m = int(input())
# find = input()




# 왼쪽 이동 : shift(lst, -1)
# 오른쪽 이동 : shift(lst, 1)




# 의문점
# list[:] = list의 모든 요소값, list= 그냥 list.
# lst[:]에서 왼쪽 이동하면 [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]이지만, lst에서 왼쪽 이동하면 [2, 3, 4, 5, 6, 7, 8, 9, 1, 1]가 된다.