skill = "CBDK"
skills = [skill[0:i] for i in range(1, len(skill)+1)]
print(skills)
skill_trees =  ['C', 'CA', 'AB', 'CB', 'CXYB', 'BD', 'AECD', 'ABC', 'AEX', 'CDB', 'CBKD', 'IJCB', 'LMDK']

# 스킬트리에 해당하지 않는 스킬들은 어떻게 배워도 상관 없음. 따라서, 스킬트리에 없는 스킬들로만 구성된 것도 가능.
cnt = 0
for st in skill_trees:
    st_skill = ""
    for s in st:
        if s in skill:
            st_skill += s
    print(st, st_skill)
    if (st_skill in skills) or st_skill == "":
        cnt+= 1
print(cnt)
# 4개/14개 : skill에서 나올 수 있는 조합 모두 구해 놓고 st_skill이 있으면 개수 세주기
# cnt = 0
# for st in skill_trees:
#     st_skill = ""
#     for s in st:
#         if s in skill:
#             st_skill += s
#     if st_skill in skills:
#         cnt += 1
#         print(st, st_skill)
# print(cnt)