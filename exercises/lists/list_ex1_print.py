"""
    Create two separate lists:
        1. my_stuff - at least 4 elements long, 1 string and 1 float
        2. nums - list from 1 to 99
"""
# Define my_stuff
my_stuff = ["test string", 2, 4, 6.980]

# Print try
for elem in range(0, len(my_stuff)):
    print(f"Element {elem + 1} is {my_stuff[elem]}")

# Define nums
nums = list(range(1, 100))
