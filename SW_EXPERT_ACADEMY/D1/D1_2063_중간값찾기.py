# 항상 홀수 개수로 주어짐
# 홀수일 때 중간값은 

n = int(input())
myList = sorted(list(map(int, input().split())))
print(myList[n//2])




