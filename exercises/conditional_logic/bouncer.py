age = input("How old are you? ")

if age:
    age = int(age)

    if age >= 21:
        print("You can come in and you can drink")
    elif age >= 18:
        print("You can come in but you can't drink and need a wristband")
    else:
        print("You can't come in, you're too young"
else:
    print("Please, enter a valid number")