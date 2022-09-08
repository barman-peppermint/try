import random

print("Generating a random number form 1 to 3")

n = random.randint(1,3)
while n!=0:
    if n == 2:
        print("Horray you found it")
        exit()
    else:
        print("Try again next time")
    n -= 1