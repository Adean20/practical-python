# bounce.py
#
# Exercise 1.5

bounce_height = 100
for i in range(10):
    bounce_height = bounce_height * (3/5)
    print(i+1, round(bounce_height, 4))
