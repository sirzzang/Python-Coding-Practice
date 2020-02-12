# - 키가 가장 큰 사람은 어차피 자기 옆에 0일 것이다.
# - 가장 큰 사람부터 배치하고, 그 다음 순서인 사람을 기억하는 정보에 따라서 해당하는 위치에 끼워 넣는다.

# 키가 1인 사람은 자기보다 큰 사람이 2명 있었다고
# 키가 2인 사람은 자기보다 큰 사람이 1명 있었다고
# 키가 3인 사람은 자기보다 큰 사람이 1명 있었다고
# 키가 4인 사람은 자기보다 큰 사람이 0명 있었다고

# 4 먼저 배치
# 3이 0이라고 말하면 0위치에, 1이라고 말하면 1위치에 -> [4, 3]
# 2가 1이라고 말했으니까, [4,3]에서 1 위치에 들어가야 함. : 2명이라고 말하면 len(heights) 위치에,
# 1명이라고 말하면 len(heights)-1위치에, 0명이라고 말하면, len(heights)-2위치에 1명이면 -2, 0명이면 -3
# 일반화하면, len(heights)-(i-information[i])위치에 

# 가장 큰 사람은 어딜 가나 자기보다 큰 사람이 0명이겠지
# 가장 큰 사람 배치하고
# 그 다음 사람은 0이면 왼쪽에, 1이면 오른쪽에 
# 그 다음 사람을 1명이면 그 리스트 위치에 넣고
# 그 다음 사람도 그 리스트 위치에 넣고

# [2,1,1,0] : 키 가장 큰 사람 먼저 배치

# for문으로 구현

n = int(input())
heights = [n]

information = list(map(int, input().split()))[::-1]
print(information)

for i in range(1, len(information)):
    heights.insert(information[i], n-i)
print(*heights)

# 함수로 구현

def greedy_height(information, n):
    heights = [n]
    for i in range(1, len(information)):
        heights.insert(information[i], n-i)
    return print(*heights)

num = int(input())
information_list = list(map(int, input().split()))[::-1]
greedy_height(information_list, num)
