# Create a list called instructors

# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"

# Remove the last value in the list

# Remove the first value in the list

# Add the string "Done" to the beginning of the list

instructors = []

instructors.extend(["Colt", "Blue", "Lisa"])
print(f"Beginning list: {instructors}")

print("Removing last value in list")
instructors.pop() # can do .remove(instructors[-1]) 
print(instructors)

print("Removing first value")
instructors.pop(0) # can do remove like above
print(instructors)

print("Adding 'Done' at the beginning of the list")
instructors.insert(0, "Done")
print(instructors)
