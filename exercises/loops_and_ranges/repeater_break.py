# Repeater exercise
# Get user input then repeat CLEAN UP YOUR ROOM! that many times
# Second version with 5 max repeats

times = input("How many times do I have to tell you? ")
max_repeats = 4

try:
    times = int(times)

    for x in range(times):
        print("CLEAN UP YOUR ROOM!")
        if x >= max_repeats:
            print("Do you even listen anymore?")
            break
except ValueError:
    print("You didn't enter a number")
