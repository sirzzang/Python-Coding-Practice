# def fly(x, y):
#     for i in range(32):
#         if (y - x) == 1:
#             print(1)
#         elif (y - x) in range((2**i)+1, (2**(i+1))+1):
#             print(i+2)
    
#     return

# fly(1, 5)


d = 1
result = 1
distance = int(input())

while True:
    result += 1        
    if distance < d:
        break
    else:
        result += 1        
        d += (result//2)

print(result)