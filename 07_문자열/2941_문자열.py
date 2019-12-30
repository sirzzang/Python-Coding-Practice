# 문자열에서 croatian 안에 있는 애들 개수 찾고, 전체 문자열에서 그 개수 빼주면 될듯?
# "ddz=z="와 같이 dz=, z= 같이 있는 경우 -> 문제

# s = "ddz=z=" 
# # replace하면 ddz=z= -> dz=가 된다.
# # drop해줘야 하는데가능한가?

# # "ddz=z="와 같이 dz=, z= 같이 있는 경우 -> 문제

# num = 0

# while True:
#     if "dz=" in s:
#         s = s.replace("dz=",'')
#         num += 1
#     else:
#         break
# print(s)
# print(num)


# 다시 생각하자. while 이런거 돌리지 말고. 나눠야 하는데
# 문자열을 나누는 기준이 croatian 안에 들어있는 애 있으면 나누기

# 그냥 애초에 dz=가 z=보다 먼저 있기만 하면 되니까, croatian list를 그렇게 만들어주면된다.

import sys
user_input = sys.stdin.readline()
s = user_input.strip('\n')

croatian = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in range(len(croatian)):
    if croatian[i] in s:
        s = s.replace(croatian[i], ',')
print(len(s))



# 아래 코드는 너무 길다

# if "dz=" in s:        
#     s = s.replace("dz=",',')
#     comma_num = s.count(',') # dz=의 개수    
#     num = 0
#     for i in range(len(croatian)):
#         if croatian[i] in s:
#             num += s.count(croatian[i]) # dz=말고 크로아티아 알파벳의 개수
#     print(len(s) - num)
# else:
#     num = 0
#     for i in range(len(croatian)):
#         if croatian[i] in s:
#             num += s.count(croatian[i]) 
#     print(len(s) - num)







# while True:    
#     if "dz=" in s:        
#         s = s.replace("dz=",',')
#         num += 1
#     else:
#         break
  


# for i in range(len(croatian)):
#     if "dz=" in s:
#         # num += 1
#         s.replace("dz=",' ')        
#     else:
#         pass


#     if croatian[i] in s:
#         num += 1


# print(num)
# print(len(s))

# print(len(s) - num)

