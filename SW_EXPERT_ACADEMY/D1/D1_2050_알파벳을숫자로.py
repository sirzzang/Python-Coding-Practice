# 접근 방법 : dictionary 만들고 저장해서 key로 접근하자.

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# mapping_dict = {idx+1 : value for idx, value in enumerate(alphabet)}
mapping_dict2 = {value : idx+1 for idx, value in enumerate(alphabet)}
# print(mapping_dict)
# print(mapping_dict2.keys())

myStr = input().upper()
for character in myStr:
    # print(character)
    if character in mapping_dict2.keys():
        num = mapping_dict2[character]
        print(num, end=" ")

