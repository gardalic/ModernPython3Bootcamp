# Repeater exercise
# Get user input then repeat CLEAN UP YOUR ROOM! that many times

times = input("How many times do I have to tell you? ")

try:
    times = int(times)

    for x in range(0, times):
        print("CLEAN UP YOUR ROOM!")
except ValueError:
    print("You didn't enter a number")
