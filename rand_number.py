import random

n = random.randint(1,3)
while n!=0:
    if n == 2:
        print("Horray you found it")
        exit()
    else:
        print("Try again next time")
    n -= 1