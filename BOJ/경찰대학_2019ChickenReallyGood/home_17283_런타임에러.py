L, R = map(int, input().split())

i = 0
z = 0
branch = []

while True:
    z = int(L * ((R/100)**i))
    branch.append(z)
    if z <= 5:
        break    
    i += 1
print(branch)

print(sum([value * (2**(index)) for index, value in enumerate(branch)][1:]))

    
