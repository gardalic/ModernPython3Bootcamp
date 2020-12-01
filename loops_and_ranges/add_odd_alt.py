# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0

for i in range(10, 21):
    if (i%2) == 1:
        x += i
        print(f"Adding {i} to X")

print(f"\nTotal result is: {x}")