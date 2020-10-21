from random import randint

num = randint(1, 1000)

if num % 2 == 1:
    print(f"Number {num} is odd")
elif num == 0:
    print(f"Number {num} is 0")
else:
    print(f"Number {num} is even")
