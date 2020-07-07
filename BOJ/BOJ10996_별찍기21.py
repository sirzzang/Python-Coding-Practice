N = int(input())

odd_stars, even_stars = "", ""

for i in range(N):
    if i % 2 == 0:
        even_stars += "*"
        odd_stars += " "
    else:
        even_stars += " "
        odd_stars += "*"

stars = even_stars + "\n" + odd_stars

for _ in range(N):
    print(stars)