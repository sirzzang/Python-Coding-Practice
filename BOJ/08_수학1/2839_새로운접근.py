

sugarList = list(range(3, 501))

for sugar in sugarList:                      # 각 숫자에 대해서
    fiveCount = sugar // 5                   # 일단 5로 나눈 몫을 5키로 배달횟수라고 하고
    sugar = sugar % 5                        # 5로 나눈 나머지를 더 배달해야 할 설탕이라고 한다
    threeCount = 0                           # 지금은 3키로 배달횟수는 없음 
    while fiveCount >= 0 :                   # 5키로 배달횟수가 0이거나(전부 다 3키로만 배달해야 할 수도 있으니까, 예컨대 6키로나 9키로나) 0이상일 때
        if sugar % 3 == 0:                   # 만약 더 배달해야 할 설탕의 키로수가 3의 배수이면
            threeCount = sugar // 3          # 3키로 배달횟수는 더 배달해야 할 설탕을 3으로 나눈 몫
            sugar = sugar % 3                # 그러면 이제 남은 설탕은 3으로 나눈 나머지 -> 원래 처음에 5로 나눈 나머지가 0, 1, 2, 3, 4였는데 그 중에서 3인 경우 처리해준거고, 이제 그러면 0, 1, 2, 4 남겠지
            break
        fiveCount -= 1                       # 나머지 경우는 5키로 배달 1번 줄이고
        sugar += 5                           # 그걸 남은 설탕에 넘겨줘

    그러면 이제 5키로 배달횟수 1만큼 줄어들 거고, 남은 설탕은 0, 1, 2, 4에서 5만큼 늘어나겠지
    그럼 이제 남은 설탕 9키로 되는 애들 거를 수 있고
    그럼에도 불구하고 남는 애들은 sugar 0, 1, 2고 거기다가 5 더하면 이제 6되는 애들 걸러지고, 이런 식
    쭉 가서 결국 5키로짜리가 0까지 간다는 건 결국 3의 배수이거나 아니면 아예 안되는 애들이란 말이고
    
    print((fiveCount + threeCount) if sugar == 0 else -1)
    남은 설탕이 0이랑 일치하면 5키로 배달횟수 + 3키로 배달횟수 출력하고, 아니면 안 되는거니까 -1 출력하라는 inline statement



# # 인터넷 본 코드 -> 이러니까 3, 4, 6, 7일 때 모두 다 -1이 나옴...
# # 내가 안 쓴 줄은 fiveCount >= 0이랑
# # sugar = sugar % 3 이거랑
# # print 안에 (sugar == 0) 이것 뿐인데?

# # sugarList = list(range(3, 501))

# # for sugar in sugarList:
# #     fiveCount = sugar // 5
# #     sugar = sugar % 5
# #     threeCount = 0
# #     while fiveCount > 0 :
# #         if sugar % 3 == 0:
# #             threeCount = sugar // 3
# #             break
# #         fiveCount -= 1
# #         sugar += 5
# #     print((fiveCount + threeCount) or -1)


# # 남는 애들이 도저히 안 걸러진다...

# sugarList = list(range(3, 501))

# for sugar in sugarList:
#     if sugar % 5 == 0:
#         delivery = sugar//5
#         print(sugar, delivery, "5의 배수")
#     elif (sugar % 15) % 3 == 0:
#         delivery = (sugar//15) * 3 + (sugar % 15)//3
#         print(sugar, delivery, "15로 거름")
#     elif (sugar % 10) % 3 == 0:
#         delivery = (sugar//10) * 2 + (sugar % 10)//3
#         print(sugar, delivery, "10으로 거름")
#     elif (sugar % 5) % 3 == 0:
#         delivery = (sugar//5) + (sugar % 5)//3
#         print(sugar, delivery, "5로 거름")
#     else:
#         delivery = 0
#         while sugar > 0 :
#             sugar -= 5
#             fiveCount = 1
#             if sugar < 0 :
#                 delivery = -1
#                 break
#             elif sugar % 3 == 0:
#                 delivery = sugar//3 + fiveCount 
#             else:
#                 sugar -= 5
#                 fiveCount += 1 
#         print(sugar, delivery, "되나?")
