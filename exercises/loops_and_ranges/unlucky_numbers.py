# Loop through numbers from 1-20
# 4 and 13 are unlucky
# Print if the number is odd or even (not including 4 and 13)

for i in range(1, 21):
    if i == 4 or i == 13:
        print(f"{i} is unlucky!")
    elif i % 2 == 1:
        print(f"{i} is odd")
    else:
        print(f"{i} is even")
