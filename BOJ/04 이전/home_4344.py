import sys

s = sys.stdin

scores = s.readlines()

for i in range(1, len(scores)):
    input_list = [int(x) for x in scores[i].split()]
    score_list = input_list[1:]
    student_number = input_list[0]
    avg = sum(score_list)/student_number
    nCount = 0
    for x in score_list:
        if x > avg:
            nCount += 1
    percentage = (nCount/student_number)*100
    print(str('%.3f' % percentage) + "%")

    



# for score in scores:
#     print(score)
#     score_list = score
    

# for score in scores:    
#     score_list = [int(x) for x in score[1:].split()]
#     student_number = int(score[0])
#     avg = sum(score_list)/student_number
#     nCount = 0
#     for x in score_list:
#         if x > avg:
#             nCount += 1
#     percentage = (nCount/student_number)*100
#     print(str('%.3f' % round(percentage, 3)) + "%")


#     # answer = '%.3f' % percentage
#     # print(answer + "%")


#     # percentage = (nCount/len(score_list))*100