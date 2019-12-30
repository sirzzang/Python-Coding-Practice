# 어쨌든 벌집 가려면 그 벌집이 몇 번째 칸에 놓여 있는지 알면 됨.
# 그거만 알면 알아서 잘 찾아갈 것.
# 개수에 따라서 생성되는 list만들고, 숫자가 list의 몇 번째 index에 위치해 있는지 알면 될 것datetime A combination of a date and a time. Attributes: ()
# 생성되는 list는 공비 6인 등비수열



# 내가 만들고 싶은 list = [[1], [2~7], [8~19], [20~37]]
# [range(1,2), range(2,8), range(8, 20), range(20, 38)]



# ㄴㄴ. 1, 10000000~ 까지의 수를 1, 6, 12, ...로 잘라서 list 만들기

user_input = int(input())
hive = 1
hive_count = 1
cell = 1

if user_input == 1:
    print(1)
else:
    while True:
        hive += hive_count * 6
        cell += 1
        if user_input <= hive:
            break
        hive_count += 1
    print(cell)


