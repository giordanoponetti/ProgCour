import random
x = 0
while abs(x)<3:
    print("position=", x)
    step = random.choice([-1, 1])
    x = x + step